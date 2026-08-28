# No reading .mp4 files

**Never attempt to read a `.mp4` file.** They are Git LFS pointers — reading them returns binary garbage, not video content.

Every `.mp4` in this repo has a matching `.md` transcript in the same folder with the same stem:

```
session-5-part-1.mp4  →  session-5-part-1.md   (use this)
```

This is also enforced by the `block-read-mp4` PreToolUse hook, which will block the Read call and redirect you to the transcript path.
