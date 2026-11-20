"""Builder 2 implements a readable scenario display here."""
from collections.abc import Callable, Iterable

from dispatcher import choose_elevator
from scenarios import SCENARIOS
from models import Decision, Scenario


def run_scenarios(
    scenarios: Iterable[Scenario], output_fn: Callable[[str], None] = print
) -> list[Decision]:
    """Show each snapshot, call the dispatcher once, display and return decisions."""
    decisions = []
    for scenario in scenarios:
        output_fn(scenario.name)
        for elevator in scenario.elevators:
            stops = ", ".join(str(stop) for stop in elevator.stops) or "none"
            output_fn(
                f"  Elevator {elevator.id}: floor {elevator.floor}, "
                f"direction {elevator.direction}, load {elevator.load_kg} kg, "
                f"stops {stops}"
            )
        output_fn(
            f"  Request: floor {scenario.request.floor}, "
            f"direction {scenario.request.direction}"
        )

        decision = choose_elevator(scenario.elevators, scenario.request)
        decisions.append(decision)
        output_fn(f"  Selected: {decision.elevator_id or 'WAIT'}")
        output_fn(f"  Reason: {decision.reason}")
    return decisions

if __name__ == "__main__":
    run_scenarios(SCENARIOS)
