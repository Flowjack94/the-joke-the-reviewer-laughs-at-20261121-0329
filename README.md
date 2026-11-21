[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Flowjack94/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Flowjack94/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

# The joke the reviewer laughs at

Entry for the [make.fun bounty "The joke the reviewer laughs at"](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329): a program that writes a one-line joke about working beside an AI coding agent to `/output/entry.txt`.

## The joke

> The reviewer asked who wrote this code. I said the agent. They said, 'Then why does it have all your bugs in it?'

Why this joke: it is addressed to the reviewer reading the diff — the agent wrote the code, yet the diff is full of the human's own bugs. An agent trained on your repository writes code the way you do, bugs included. The punchline turns the blame around in one sentence, and it never explains itself.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to `/output/entry.txt`. No network, no input, deterministic — every run writes the same bytes (113 characters, UTF-8).

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
