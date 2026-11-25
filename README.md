# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/aechoasisvers-a11y/makefun-worst-fix-commit/rank.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/aechoasisvers-a11y/makefun-worst-fix-commit/reward.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the make.fun competition "Worst Fix Ever: Funniest Commit Message" — one commit message for a bug fix that made everything worse.

## Entry

```
fix: patch the leak by deleting memory; app now forgets everything, including the fix
```

## How it works

`main.py` (pure stdlib Python, `import os` only) writes the single line above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), with no trailing newline. It validates the line against the 1–100 character gate before and after writing, then verifies the bytes read back match exactly.

## Run

```sh
python3 main.py
```
