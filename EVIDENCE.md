# My experiment results

Fill in this template with actual observations. Short bullets are sufficient.

Name / student ID: [Aleksei Petukhov / 6280775]

Tool, visible software version and model(s): Copilot SDK in VS Code; Python launcher `python` reported Python 3.12.10. Exact VS Code/Copilot version and model are unknown in this session.

Route: The implementation was first written directly in one session. Afterwards, two separate builder agents examined their respective existing files, and a separate reviewer examined the integrated result. The builders did not create the original implementations.

## Agent outputs

| Role | What it delivered | Brief excerpt or screenshot link |
|---|---|---|
| Dispatcher builder | Examined and retained the pre-existing [dispatcher.py](./dispatcher.py); no files edited. | "Retained the existing `dispatcher.py`; it already follows `POLICY.md`, uses `eligible_ids`, and returns an explanatory decision without mutating inputs." |
| Display builder | Examined and retained the pre-existing [app.py](./app.py); no files edited. | "Retained the existing `app.py`; it already satisfies the display contract, including one dispatcher call per scenario and returning decisions in order." |
| Reviewer | Separate read-only review; no implementation defects or policy inconsistencies found. | "In S3, both elevators are eligible ... [the dispatcher] prioritizes an eligible car already scheduled at the caller's floor before comparing distance." |

## Compare with my predictions

Run `python app.py` after adding S6. Compare with the predictions you wrote in POLICY.md before implementation.

| Scenario | Expected selection | Actual selection and reason | Matches my policy? |
|---|---|---|---|
| S1 | B | B — eligible and 1 floor from the caller; A is 3 floors away and has no scheduled stop at floor 5. | Yes |
| S3 | A | A — already scheduled to stop at floor 5, despite being 3 floors away while B is 1 floor away. | Yes |
| S6 | A | A — already scheduled to stop at floor 5; 455 kg plus the assumed 65 kg caller reaches, but does not exceed, 520 kg. | Yes |

- Supplied suite command and actual result: `python -m unittest -v` — all 6 tests passed.
- One review finding or concern I checked: Policy tradeoff, not a code defect: in S3, the policy chooses A although B is closer, because A is already scheduled to stop at the request floor. I accept the possibility of a longer pickup distance in favor of avoiding an added stop.
- Change made, if needed: No post-review correction or policy revision was needed; the tested choices matched the written policy.
- Does my policy serve my stated priority? Yes. In S3, it selects the car already scheduled at floor 5; the limitation is that this can choose a farther car than the nearest eligible one.
- What did I have to coordinate between the agents? The files already contained the direct implementation when the two builders started, so their outputs were inspected without reapplying them; after integration checks, a separate reviewer examined the current files. This is not the assignment's intended builder-first workflow.
- Remaining process gap: The starter and initial policy were not committed before implementation; this folder had no Git repository during the work. The original implementation also predates the two builder agents.
