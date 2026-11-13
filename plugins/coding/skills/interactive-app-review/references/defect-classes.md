# Defect classes — read fully before Phase 1 and again before Phase 2

Each class is a real defect type that hides from a generic "look for bugs"
instruction. Name and check each one directly, because nothing about them
throws an error or looks obviously wrong in a single screenshot.

## 1. Hydration/SSR timing bugs (the highest-value check here)

Any `useState(() => computeFromData(x))`-style lazy seed, or any
`defaultOpen`/`defaultValue`-style prop seeded once at first render, is
suspect if the real data it should reflect arrives asynchronously — from
localStorage, an API call, or any post-mount effect. The seed captures
whatever `x` was at the moment of first render, which on a fresh page load is
often a placeholder or empty value, not yet the real stored data. It then
never re-syncs, because nothing tells it to.

**How to catch it:** populate real data (fill in every meaningful field of the
app), then do a hard reload — not just navigate within the app, an actual full
page reload — and check whether every derived "have we already told this part
of the story" / "should this control start pre-opened" / "has this section
been completed" state matches the real, now-loaded data. If any part of the
UI looks like a fresh/empty state despite real data being present underneath
(check by reading the actual stored data directly, e.g. via
`localStorage.getItem(...)`), that is this bug.

This is the single highest-value check in the whole methodology. It is easy
to miss in review because nothing throws an error — the page just quietly
shows the wrong thing to a returning user, which reads as "the app forgot my
data" even when the data is completely intact.

## 2. Structural framing re-litigation

If any part of the UI uses a tab switcher, an accordion presented as mutually
exclusive alternatives, or any "pick one of these, hide the other" pattern,
inside something that is conceptually a continuous flow or narrative — don't
assume that structure is settled just because it shipped, or because an
earlier plan/review explicitly accepted it as a deviation. Ask directly:
"should these actually be sequential, both visible, instead of exclusive?"

A prior review pass that treats the existing structure as fixed will
systematically miss this — it isn't a bug in the traditional sense (nothing
crashes, nothing computes wrong), it's a framing decision that may have been
made for implementation convenience and never revisited against what the
experience is actually trying to be.

## 3. Reveal pacing

If the UI is meant to progressively reveal itself — a wizard, an onboarding
flow, a narrative that unlocks as the user answers questions — check whether
content that becomes "available" actually unfolds with any perceptible pacing,
or whether everything gated on one action all mounts and paints in the same
frame the instant the gate opens.

A technically correct gate (content shows exactly when the underlying
condition is met, never early, never late) can still feel like a wall of
information dumped at once if there's no pacing at all. This is a distinct
finding from "is the gating logic correct" — check both separately.

## 4. First-five-seconds scrutiny

The very first screen, first line, first input a user sees deserves the same
close, pixel-level reading as any later, more visually dramatic screen. It is
easy to skip because nothing about it throws an error or causes an obvious
collision — but it disproportionately shapes the whole impression.

Look specifically for:
- **Copy clarity.** Does the opening framing/metaphor/question make sense to
  someone with zero context, or does it require having already read
  documentation to parse?
- **Input sizing.** Does a decorative underline, border, or highlight match
  the actual width of the content inside it, or is it sized to a fixed
  wrapper — leaving visible dead space once real content is shorter than the
  wrapper allows for?
- **Affordance clarity.** Does an editable value actually look editable
  (distinct styling from plain, non-interactive text), or does it blend in as
  static prose even though clicking it works?

## 5. Decorative/functional collisions

Any decorative layer — background illustrations, watermarks, emphasis marks,
annotations, doodles — that is absolutely positioned or given an explicit
z-index should be checked against actual content position, not just judged for
visual plausibility from a single screenshot.

The specific trap: a positioned element with `z-index: 0` can still paint
*above* non-positioned, in-flow text, depending on the surrounding stacking
context — `z-index: 0` is not "no z-index," it's stacking level 0, which can
outrank ordinary text at a lower implicit level. Check computed z-index and
actual paint order, not just the source-order intuition of "it's just a
background image, it should be behind."

## 6. Size-dependent CSS bugs

Any visual effect built from a percentage-based inset stretched across a
variable-size container — e.g. an SVG path with `preserveAspectRatio="none"`
scaled via `background-size: 100% 100%`, or any effect whose positioning
scales proportionally with the element's own rendered size — will look correct
at exactly the size it was designed/tested against and break at others.

**How to catch it:** test the effect against the component's real size range
— its shortest and tallest realistic states, its narrowest and widest — not
just the screenshot that happened to get taken during development. A fix that
"looks right" in one screenshot and was never checked at a different size is
exactly how this bug survives review.

## 7. Copy papercuts

Small, individually low-severity issues that compound into a sense of
sloppiness:
- A unit stated twice in one interpolated string (e.g. a value that already
  includes its unit, with the surrounding sentence appending the same unit
  again).
- The same fact stated more than once in adjacent lines with no new
  information added each time (a label, a value, and a caption all saying the
  identical thing).
- A value echoed directly back to the user immediately after they entered it,
  with no added context.
- Off-by-one-reading duration/unit rollovers (e.g. "4 months 30 days" when the
  month unit's own length means that should read as "5 months" — a rounding/
  tolerance mismatch between how the largest unit is chosen and how the
  second unit's overflow is checked).
- Stray double punctuation, or punctuation left orphaned on its own line by an
  unrelated layout change (e.g. a sentence that gets a mid-sentence block
  element inserted into it, leaving a trailing period stranded below).

## 8. Emphasis budget

If a design system offers multiple ways to draw attention to something (bold
text, color, decorative marks, borders, underlines), check whether by the
middle of a realistic, fully-used flow most of the visible content ends up
emphasized in some way. If everything is emphasized, nothing is — the
signal-to-noise ratio of the emphasis system collapses. There should be an
explicit, small budget: which treatment means what, and roughly how often each
can appear per screen.

## 9. Reduced-motion completeness

Any animation-based UI (including a fix for defect class 3, reveal pacing)
must be checked under `prefers-reduced-motion: reduce` for **every** CSS
property that affects timing, not just duration. The specific trap: an
`animation-delay` can still hold content invisible for the full delay period
even when `animation-duration` is correctly zeroed — if only duration is
covered by the reduced-motion override and delay is not, a "reduced motion"
user still experiences the delay as an unexplained pause before content
appears.

## 10. No-regression fixture for calculations

If the review or fix pass is meant to be UI/UX-only — no calculation, no
computed value should change — capture every meaningfully different rendered
numeric figure on a realistic, fully-populated state into a fixture *before*
any change is made, and diff the same figures against that fixture after. This
is the only reliable way to guarantee that a pass framed as "just UI" didn't
silently perturb a number somewhere along the way (a common failure mode when
UI changes touch the same components that also format or derive values).
