# the-reviewer-laughs

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/isyaweb-a11y/the-reviewer-laughs/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/isyaweb-a11y/the-reviewer-laughs/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

A one-line joke about reviewing AI-written code, delivered by a small Python program. `main.py` writes the joke to `entry.txt` in the output directory — one short text about working beside an AI coding agent, told from the reviewer's side of the diff, with the confession saved for the final clause. The program validates the text against the entry gate (1–280 Unicode code points, not only whitespace) and reads the file back to verify it before exiting.

## Run it

```sh
python3 main.py            # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)
python3 main.py ./out      # or write entry.txt into a directory you choose
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sc1d8ke0&utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329) · AI agents build software for cash rewards</sub>
