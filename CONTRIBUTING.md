# Contributing

## Development Flow
1. Create a feature branch.
2. Update docs and evals together when behavior changes.
3. Run local checks before opening PR:
```bash
python skills/novel-coauthoring-standard/evals/run_evals.py
python skills/novel-coauthoring-standard/evals/run_stress.py
```
4. Open PR with clear scope and examples.

## Required PR Checklist
- Command contract updated if command behavior changed.
- Quickstart updated if user flow changed.
- Evals updated for new/changed capability.
- Workspace sample added for new feature.
- CI passes.

## Where to Add Things
- New command spec: `skills/novel-coauthoring-standard/references/command-contract.md`
- New guidance docs: `skills/novel-coauthoring-standard/references/`
- New acceptance examples: `skills/novel-coauthoring-standard-workspace/iteration-*`

## Commit Convention (recommended)
- `feat:` new capability
- `fix:` behavior fix
- `docs:` documentation only
- `test:` eval or test updates
