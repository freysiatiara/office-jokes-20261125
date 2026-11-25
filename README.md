# One-Line Office Jokes

A single-line joke about office life, written for the
[One-Line Office Jokes bounty](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
on make.fun.

[![Bounty](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/freysiatiara/office-jokes-20261125/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)
[![Reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/freysiatiara/office-jokes-20261125/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc)

## The joke

> The printer jammed at 4:59 on Friday, so I listed it as my emergency contact in my out-of-office reply.

## How it works

`main.py` (Python standard library only) writes that one line to the output
file — `$ENTRY_OUTPUT`, or `$OUTPUT_DIR/entry.txt`, or
`$MAKEFUN_OUTPUT_DIR/entry.txt`, or `/output/entry.txt` by default — and sets
the file mode to `0644`. The text is checked first: UTF-8, 1–199 characters,
a single line.

## Run it

```sh
python3 main.py
```
