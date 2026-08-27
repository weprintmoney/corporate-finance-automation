# Kebab-case naming

**All files and folders in this repo use kebab-case** — lowercase letters and digits joined by single hyphens. This makes paths safe on any filesystem, easy to type, easy to grep, and free of URL escaping (`%20` in links).

## Rule

- **Files:** `present-value-notes.md`, `session-27-part-2.txt`, `fetch-archive.py` — not `Present Value Notes.md`, not `presentValueNotes.md`, not `present_value_notes.md`.
- **Folders:** `corporate-finance/`, `course-overview/` — not `Corporate Finance/`, not `CorporateFinance/`.

Single-word names are already kebab-compliant: `statistics/`, `blogs/`, `syllabus.md`.

## Exceptions

The following ALL-CAPS names are allowed at any level:

- `CLAUDE.md` — folder-scoped agent context
- `README.md` — repo/folder entry point
- `LICENSE`

Dotfiles and dotfolders (`.claude/`, `.github/`, `.gitignore`) are allowed as-is.

**Python note:** If you ever add a Python module that other Python code needs to `import`, that specific file must use snake_case (hyphens are illegal in Python identifiers). Standalone scripts run as `python3 script.py` should stay kebab-case — e.g. `fetch-archive.py` is fine because nothing imports it.

## Enforcement

- `.claude/hooks/enforce-kebab-case.sh` — PreToolUse hook on `Write`/`Edit`. Blocks any create/edit whose filename basename isn't kebab-case (or in the allow-list above). Wired via `.claude/settings.json`.
- The hook only inspects the basename it's about to write, so it doesn't retro-check existing files or folder names. Enforce those manually via `git mv` when renaming.

## Renaming existing paths

```bash
git mv "Old Folder Name" old-folder-name
# Update any wiki-style links in CLAUDE.md / README.md that referenced the old name.
```

On case-insensitive filesystems (macOS default APFS), pure case-only renames need a two-step `git mv`:

```bash
git mv Statistics statistics-tmp && git mv statistics-tmp statistics
```

Renames that change more than just case (spaces → hyphens, capitals → lowercase mixed in) work in one step.
