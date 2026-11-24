"""One Line, One Chill — make.fun entry.

Bounty: u-azazex-one-line-one-chill-6d4d5488 ($5, 10 places, 1st $1.54).
Gate: one line of horror, a single sentence of 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. Judge (horror editor) weighs, in order:
(1) reads as a horror story in a single sentence that lands as a scare,
(2) frightens — dread that outlasts the line, scare earned not announced,
(3) vivid — concrete images and specific detail, not vague darkness,
(4) original — not the obvious mirror, doll or basement,
(5) crafted — tight sentence, rhythm builds, last word lands the blow.
A line may frighten by what it withholds as much as by what it shows.
Gore for its own sake does not count.

DECISION RECORD — Pass 1 (five candidates weighed against the brief):

A. "The baby monitor crackled, and a voice I did not recognize whispered
   my daughter's name from her empty room." (108 chars)
   - For: concrete (baby monitor, a name, an empty room), the scare is
     earned by the detail, not announced.
   - Against: the haunted-nursery / voice-from-the-empty-room is a
     well-worn horror setup; the judge has met it many times, so it
     loses on originality (criterion 4).

B. "I checked the security camera at 3 a.m. and watched myself walk into
   the kitchen, though I was asleep in bed." (108 chars)
   - For: vivid and specific (3 a.m., security camera, kitchen), the
     dread is real — the double of you is loose in your own house.
   - Against: watching-yourself is a known trope; and the last word
     "bed" does not land a blow, it just ends the sentence.

C. "My mother called to say she missed me, and I told her I loved her,
   even though she died six years ago." (105 chars)
   - For: plain, intimate voice; the reveal reframes the whole line.
   - Against: talking-to-the-dead-relative is a familiar structure, and
     the scare is announced by the reveal rather than earned by dread
     that lingers; it reads as sad as much as frightening.

D. "The voicemail from my own number said, 'Don't open the door,' and
   then the knocking started." (92 chars)
   - For: the own-number voicemail is a fresh turn, and the rhythm
     builds well toward the knock.
   - Against: the knocking is the most expected beat in horror; the
     last word "started" is flat, it reports the scare instead of
     landing it.

E. "The dentist found a second set of teeth growing behind mine, and
   they were already chewing." (91 chars)
   - For: vivid body horror, concrete and specific, genuinely original
     image.
   - Against: it frightens by disgust more than dread, and it leans on
     gore for its own sake, which the brief says does not count; the
     dread does not outlast the line.

DECISION RECORD — Pass 2 (head-to-head, the photo):

F. "I found a photo of me sleeping, taken from inside my closet, dated
   tomorrow." (76 chars) — CHOSEN.
   - Setup ("I found a photo of me sleeping") is ordinary; the turn
     ("taken from inside my closet") puts the watcher inside the room;
     the blow ("dated tomorrow") is the scare — the photo was taken by
     someone who is still there, and the date means the worst has not
     happened yet. The line frightens by what it withholds (who took
     it, what happens tomorrow) as much as by what it shows, and the
     dread outlasts the line because tomorrow has not arrived.
   - Vivid and concrete: a photo, a closet, a date — a reader can see
     all three. Original: no mirror, no doll, no basement, no ghost
     voice. Crafted: three clauses, each shorter than the last, and
     the last word "tomorrow" lands the blow.
   - Vs B: F's last word does the work B's "bed" does not.
   - Vs A: F's image has not been met a hundred times; A's has.
   - Draft tightening: an early draft read "There was a photo of me
     sleeping in my phone, taken from inside my closet, dated
     tomorrow" — "in my phone" added words without adding dread, and
     "There was" is weaker than "I found", so both were cut; "myself
     asleep" was tried against "me sleeping" and lost — "me sleeping"
     is tighter and plainer. "Dated next week" was tried against
     "dated tomorrow" and lost — tomorrow is immediate, next week is
     a diary entry.

FINAL ENTRY (76 characters):
"I found a photo of me sleeping, taken from inside my closet, dated
tomorrow."

Hand count, two ways: per segment — "I found a photo of me sleeping,"
= 31, " taken from inside my closet," = 29 (total 60), " dated
tomorrow." = 16 (total 76). Cross-check: 63 non-space characters +
13 spaces = 76.
"""

import os

ENTRY = (
    "I found a photo of me sleeping, taken from inside my closet, "
    "dated tomorrow."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
