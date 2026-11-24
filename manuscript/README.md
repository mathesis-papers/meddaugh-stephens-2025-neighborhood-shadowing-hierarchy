# Finite neighborhood-shadowing levels

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

For every integer `m >= 3`, the binary two-sided subshift with at most two ones on each translated `m`-term progression of step `(m+1)^k`, `k >= 0`, has least neighborhood-shadowing bound `m-1`. It is mixing, has dense periodic points, and is not of quasi-finite type or sofic. The tracers can all follow the pseudo-orbit at common periodic times; thus uniform syndetic tracing by both points does not characterize quasi-finite type.

The posing source is Jonathan Meddaugh and Elyssa Stephens, *Shadowing with small diameter sets of bounded cardinality*, arXiv:2509.04312v1 (4 September 2025), Section 5, Questions 5.1–5.3, printed page 11. The level `N=1` extends their Examples 3.4 and 3.6 and Theorem 3.7. A companion Ma–Zhang note, *Neighborhood two-shadowing without quasi-finite type* (October 2026), treats a different return-distance example. This note supplies the progression family and its structural consequences.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a LaTeX distribution providing the packages named in `note.tex`:

```sh
pdflatex note.tex
pdflatex note.tex
```

The bibliography is included in the main source, so BibTeX is unnecessary.

## Mathematical coverage

- Theorem 1 proves the hierarchy for all `m >= 3`. The declaration `D5.S1.Dynamics.Shadowing.lacunary_shadowing_hierarchy` states nonemptiness, compactness, continuity, bijectivity, neighborhood `(N+1)`-shadowing and failure of neighborhood `N`-shadowing for `m=N+2`, `N>=1`, in the [pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/147008bff5524a3dccf0efa3ed9e76fb6b168a50/D5/S1/Dynamics/Shadowing/LacunaryShadowingHierarchy.lean).
- The fixed finite tracing set has small initial diameter; its matching member can depend on time. The compatible product metric and the first-disagreement metric give the same property by the uniform-equivalence argument in the note.
- Corollary 5 gives a written proof of failure of exact-length quasi-finite type for every member.
- Corollary 6 gives a written proof of common periodic tracing times, with period depending on the accuracy but not on the pseudo-orbit. The example `X_3` therefore has uniform syndetic tracing by each of two points and fails quasi-finite type. The source does not assert the converse disproved by this example.
- Corollary 7 gives written proofs of mixing, dense periodic points and nonsoficity. The gap length for gluing two words depends on their lengths; it is not a uniform mixing number.
- The separate powers-of-two return-distance declaration and the separate weak-mixing example for Question 5.6 are linked in the PDF with their individual scopes. Questions 5.4 and 5.5 are not characterized here.

## Finite checks

Run with Python 3, using only the standard library:

```sh
python3 verify.py > phase-results.json
python3 verify-structure.py > structure-results.json
```

Compare these JSON files with `verification.json` and `structure-verification.json`. The first program uses exact rational arithmetic for the phase cover, polygon occupancy, and eroded-cover geometry for `3 <= m <= 20`. The second uses exact integer arithmetic for all allowed binary words of lengths 1 through 6 for `3 <= m <= 6`, their specified gluing gaps, every translated progression in the proposed periodic extensions at the representative scales, and three exact-length bridge obstructions per parameter. The note gives the all-parameter written arguments; the computations cover the stated finite ranges.

## Files and license

`note.tex` is the main source. `metadata.json` gives bibliographic data. `verify.py`, `verify-structure.py`, and their expected JSON outputs give the finite checks. `source-manifest.json` records exact member hashes.

Copyright 2026 Haobo Ma and Wenlin Zhang. Licensed under Creative Commons Attribution 4.0 International (`cc-by-4.0`).
