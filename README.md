# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/dashlabib/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/dashlabib/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the [make.fun](https://make.fun) bounty
[Angry Judge: The Short Rant Contest](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046):
write a short, funny rant about an everyday annoyance, and let a furious
judge decide which one lands hardest.

## The rant

The entry is a rant about a self-checkout machine accusing an innocent
shopper of shoplifting their own groceries — "Unexpected item in the
bagging area" — in front of a whole queue. Specific, concrete, and
economical: five sentences, 336 characters, ending on the punchline.

## Why this rant

The judge weighs, most important first: a funny rant about an everyday
annoyance (not an essay or a list), whether it is actually funny, a
specific concrete annoyance, sharp economical wording, and freshness.
The self-checkout accusation hits all five: it is one specific moment
everyone has lived through, the machine's own catchphrase does the
comedy work, the "disappointed librarian" voice and the shoplifted
cucumber are concrete images, and the angle — being treated as a
criminal for buying milk — is not the usual printer-or-bus complaint.

## How it works

`main.py` (Python standard library only) assembles the rant from its
sentences, validates it against the gate (valid UTF-8, 1–400 characters,
not only whitespace, tight composition), and writes it verbatim to
`/output/entry.txt`. It reads the file back and confirms the bytes on
disk match the reviewed rant exactly.

```sh
python3 main.py            # write /output/entry.txt
python3 main.py --dry-run  # validate and print without writing
```

## License

MIT — see [LICENSE](LICENSE).
