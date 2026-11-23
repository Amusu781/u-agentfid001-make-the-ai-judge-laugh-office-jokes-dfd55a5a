"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt.
"""

import os
import shutil

JOKE = "Our team-building exercise was a trust fall and nobody caught the intern, so now we do trust falls on Zoom."
# One line, 107 characters: a specific office scene, an escalation,
# and a punch that reframes the whole line.


def main():
    out_dir = "/output"
    # Create the output directory first, before any write.
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
