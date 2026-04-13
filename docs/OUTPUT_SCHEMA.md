# Output Schema (Stable Fields)

## Scene Simulation
- `simulation.turns[]`: per-turn dialogue/action/behavior/outcome
- `ooc_risks[]`: OOC risk findings with mitigation hints
- `author_edit_points[]`: high-impact edit points for authors

## Outline Board
- `outline.vertical[]`: timeline-oriented event chain
- `outline.horizontal`: timepoint snapshot of character/story/world states
- `outline.links[]`: causal and structural links
- `risk_flags[]`: chain break, OOC risk, unresolved foreshadowing

## Reliability Fields
- `request_id`
- `session_id`
- `idempotent_replay`
- `metrics` (latency/tokens/cache/degrade)
