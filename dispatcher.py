"""Builder 1 implements the student's policy here."""
from models import Elevator, Request, Decision
from rules import eligible_ids


def choose_elevator(elevators: tuple[Elevator, Elevator], request: Request) -> Decision:
    """Choose one eligible elevator according to POLICY.md; never mutate inputs."""
    eligible = eligible_ids(elevators, request)
    if not eligible:
        return Decision(
            None,
            "Neither elevator is eligible under the capacity and route rules; the request will wait.",
        )

    eligible_elevators = [elevator for elevator in elevators if elevator.id in eligible]
    already_stopping = [
        elevator for elevator in eligible_elevators if request.floor in elevator.stops
    ]
    candidates = already_stopping or eligible_elevators
    selected = min(
        candidates,
        key=lambda elevator: (abs(elevator.floor - request.floor), elevator.id),
    )
    distance = abs(selected.floor - request.floor)
    distance_unit = "floor" if distance == 1 else "floors"
    tied = [
        elevator
        for elevator in candidates
        if abs(elevator.floor - request.floor) == distance
    ]
    tie_note = " The distance tie was resolved in favor of elevator A." if len(tied) > 1 else ""

    if already_stopping:
        reason = (
            f"Elevator {selected.id} is eligible and already scheduled to stop at "
            f"floor {request.floor}; among eligible cars with that stop, it is "
            f"{distance} {distance_unit} from the caller.{tie_note}"
        )
    else:
        reason = (
            f"Elevator {selected.id} is eligible and is {distance} {distance_unit} from "
            f"the caller, the shortest distance among eligible cars.{tie_note}"
        )
    return Decision(selected.id, reason)
