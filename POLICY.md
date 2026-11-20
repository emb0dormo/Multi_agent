# My dispatch policy

## Priorities

- What I prioritise: Avoiding an additional scheduled stop, then minimizing floor distance to the caller.
- My exact selection rule: First use `eligible_ids`. If any eligible elevator already has the caller's floor in its scheduled stops, choose among those elevators by smallest floor distance to the caller. Otherwise, choose among all eligible elevators by smallest floor distance.
- My deterministic tie-breaker: If the remaining candidates are still tied, choose elevator A.
- A tradeoff I accept: A farther car may be chosen when it is already scheduled to stop at the caller's floor. Floor distance is only a rough proxy for waiting time.

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | B | B is one floor from the caller; A is three floors away and is not scheduled to stop at floor 5. | The closer idle car is used; passengers in A are not affected by a new stop. |
| S3 | A | A is already scheduled to stop at floor 5, so it wins before distance is compared. | Avoids adding a stop for A's passengers, though B is closer to the caller. |
| S6: Scheduled stop at capacity limit | A | A has a scheduled stop at floor 5 and its 455 kg load leaves exactly 65 kg for the caller. | Uses the car already stopping there, but it will reach the model capacity after pickup. |

## Another defensible policy

- An alternative priority: Always choose the eligible elevator with the smallest floor distance, regardless of scheduled stops.
- A scenario where it could choose differently, and why: In S3, this alternative would choose B because it is one floor from the caller, while A is three floors away, even though A is scheduled to stop at floor 5.

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.
