// Build the Word version of final-report.md, with the four exhibits placed at their markers.
// Run from the company folder:  NODE_PATH=<dir with the docx package>/node_modules node report-exhibits/build-report-docx.js <output.docx>
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, ImageRun,
        HeadingLevel, AlignmentType, LevelFormat, Footer, PageNumber } = require("docx");

const out = process.argv[2] || "final-report.docx";
const FONT = "Arial", W = 9360;
const EXHIBITS = [["total return", "exhibit-1-total-return.png"], ["cost of capital by debt ratio", "exhibit-2-cost-of-capital.png"],
                  ["cash returned against FCFE", "exhibit-3-cash-returned.png"], ["value per share by return", "exhibit-4-value-per-share.png"]];

let md = fs.readFileSync("final-report.md", "utf8").replace(/^---[\s\S]*?---\s*/, "");
const lines = md.split("\n");

function runs(text, base = {}) {
  const parts = []; const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g; let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const s = m[0];
    if (s.startsWith("**")) parts.push(new TextRun({ text: s.slice(2, -2), bold: true, font: FONT, ...base }));
    else parts.push(new TextRun({ text: s.slice(1, -1), italics: true, font: FONT, ...base }));
    last = m.index + s.length;
  }
  if (last < text.length) parts.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return parts;
}
const plain = s => s.replace(/\*\*/g, "").replace(/\*/g, "");
const border = { style: BorderStyle.SINGLE, size: 4, color: "BFBFBF" };
const borders = { top: border, bottom: border, left: border, right: border };

function table(rows) {
  const n = rows[0].length;
  const weight = Array.from({ length: n }, (_, c) => Math.min(60, Math.max(8, ...rows.map(r => plain(r[c] || "").length))));
  const tot = weight.reduce((a, b) => a + b, 0);
  let widths = weight.map(w => Math.round(W * w / tot)); widths[n - 1] += W - widths.reduce((a, b) => a + b, 0);
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ tableHeader: i === 0, cantSplit: true, children: r.map((cell, c) => new TableCell({
      width: { size: widths[c], type: WidthType.DXA }, borders, margins: { top: 50, bottom: 50, left: 90, right: 90 },
      shading: i === 0 && rows.length > 2 && !/^\$?[\d.]/.test(plain(r[1] || "")) ? { type: ShadingType.CLEAR, fill: "E7ECF4", color: "auto" } : undefined,
      children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: runs(cell, { size: 18, bold: (i === 0 && !/^\$?[\d.]/.test(plain(r[1] || ""))) ? true : undefined }) })] })) })) });
}

const body = []; let i = 0;
while (i < lines.length) {
  const l = lines[i];
  if (!l.trim()) { i++; continue; }
  if (l.startsWith("# ")) { body.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun({ text: l.slice(2), font: FONT, bold: true, size: 34 })] })); body.push(new Paragraph({ spacing: { before: 0, after: 160 }, children: [new TextRun({ text: "Charlcye Mitchell · Corporate Finance, Fall 2026 · Final project", font: FONT, size: 20, color: "555555" })] })); i++; continue; }
  if (l.startsWith("## ")) { body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: l.slice(3), font: FONT, bold: true, size: 26 })] })); i++; continue; }
  if (l.startsWith("|")) {
    const rows = []; while (i < lines.length && lines[i].startsWith("|")) { const cells = lines[i].split("|").slice(1, -1).map(s => s.trim()); if (!/^[-: ]+$/.test(cells.join("")) && cells.join("").trim() !== "") rows.push(cells); i++; }
    body.push(table(rows)); body.push(new Paragraph({ spacing: { before: 0, after: 80 }, children: [] })); continue;
  }
  if (l.startsWith("- ")) { body.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { before: 0, after: 80 }, children: runs(l.slice(2), { size: 22 }) })); i++; continue; }
  const ex = /^\[Exhibit: (.*)\]$/.exec(l.trim());
  if (ex) {
    const hit = EXHIBITS.find(e => ex[1].includes(e[0])); if (!hit) throw new Error("no image for " + ex[1]);
    body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 160 }, keepNext: false,
      children: [new ImageRun({ type: "png", data: fs.readFileSync("report-exhibits/" + hit[1]), transformation: { width: 468, height: 245 },
        altText: { title: hit[1], description: ex[1], name: hit[1] } })] })); i++; continue;
  }
  const isSource = /^\*[^*].*\*$/.test(l.trim());
  body.push(new Paragraph({ spacing: { before: 0, after: isSource ? 160 : 120, line: 276 }, children: runs(isSource ? l.trim().slice(1, -1) : l, isSource ? { size: 17, italics: true, color: "555555" } : { size: 22 }) })); i++;
}

const doc = new Document({
  creator: "Charlcye Mitchell", title: "Colgate-Palmolive (CL): Corporate Finance Assessment and Valuation",
  styles: { default: { document: { run: { font: FONT, size: 22 } },
    title: { run: { font: FONT, size: 34, bold: true }, paragraph: { spacing: { before: 0, after: 160 }, keepNext: true } },
    heading1: { run: { font: FONT, size: 26, bold: true, color: "1F2A44" }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true } } } },
  numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: "555555" })] })] }) },
    children: body }] });
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log("wrote", out, b.length, "bytes;", body.length, "blocks"); });
