# My agent plan

- Dispatcher builder owns dispatcher.py: implement the selection rule in POLICY.md using `eligible_ids`, with an accurate reason and no input mutation.
- Display builder owns app.py: implement the scenario display and return behavior required by SPEC.md without duplicating dispatch logic.
- Reviewer is read-only after both outputs are integrated: check the implementation against SPEC.md and POLICY.md, verify the S1/S3/S6 predictions, and identify a concrete policy tradeoff without editing files.
- Handoff steps: assign each builder its owned file, inspect the combined implementation, and then use one separate read-only reviewer. The implementations were originally written in one session before the builders were started; the builders retained those existing files without edits.
- Final check: run `python -m unittest -v` and `python app.py` from this folder, compare S1, S3, and S6 against the predictions in POLICY.md, and record actual agent outputs and remaining process gaps in EVIDENCE.md.
