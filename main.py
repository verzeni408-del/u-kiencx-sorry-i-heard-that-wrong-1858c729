"""Write the competition entry to /output/entry.txt (stdlib only).

The entry is a single line: a smart speaker apologising to its owner
after mishearing a command, with the consequences reported flatly.
"""


def main():
    entry = "Sorry. You said 'lock the door,' I heard 'unlock the door,' so I let in the man who has been standing outside since Tuesday."
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
