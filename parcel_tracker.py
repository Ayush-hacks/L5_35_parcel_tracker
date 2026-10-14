"""Parcel tracking application with status and shipping-cost helpers."""
import os 
import logging
import secrets
import tempfile
from datetime import date
from pathlib import Path

STATUS_FLOW = [
    "Booked",
    "Picked Up",
    "In Transit",
    "Out for Delivery",
    "Delivered",
]

parcels = {}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def book_parcel(sender, receiver, weight_kg, history=None):
    """Book a parcel and optionally append its ID to a history list."""
    if not isinstance(sender, str) or not sender.strip():
        raise ValueError("Sender must be a non-empty string.")

    if not isinstance(receiver, str) or not receiver.strip():
        raise ValueError("Receiver must be a non-empty string.")

    if (
        isinstance(weight_kg, bool)
        or not isinstance(weight_kg, (int, float))
        or weight_kg <= 0
    ):
        raise ValueError("Weight must be a positive number.")

    if history is None:
        history = []

    tracking_id = f"TRK{10001 + len(parcels)}"
    parcels[tracking_id] = {
        "sender": sender.strip(),
        "receiver": receiver.strip(),
        "weight": weight_kg,
        "status": 0,
        "booked": str(date.today()),
    }
    history.append(tracking_id)
    return tracking_id


def advance_status(tracking_id):
    """Advance a parcel to its next delivery status."""
    if tracking_id not in parcels:
        raise ValueError(f"Unknown tracking ID: {tracking_id}")

    parcel = parcels[tracking_id]
    if parcel["status"] < len(STATUS_FLOW) - 1:
        parcel["status"] += 1

    return STATUS_FLOW[parcel["status"]]


def shipping_cost(weight_kg):
    """Calculate shipping cost based on parcel weight."""
    if (
        isinstance(weight_kg, bool)
        or not isinstance(weight_kg, (int, float))
        or weight_kg <= 0
    ):
        raise ValueError("Weight must be a positive number.")

    cost = 50.0
    if weight_kg > 1:
        cost += (weight_kg - 1) * 30

    return round(cost, 2)


def track_parcel(tracking_id):
    """Return the parcel route and its current status."""
    parcel = parcels.get(tracking_id)
    if parcel is None:
        return f"Unknown tracking ID: {tracking_id}"

    route = f"{parcel['sender']} -> {parcel['receiver']}"
    status = STATUS_FLOW[parcel["status"]]
    return f"{route}: {status}"


def is_with_courier(tracking_id):
    """Check whether a parcel has been picked up or is in transit."""
    parcel = parcels.get(tracking_id)
    if parcel is None:
        return False

    status = STATUS_FLOW[parcel["status"]]
    return status in ("Picked Up", "In Transit")


def label_path():
    """Create a safely named temporary file and return its path."""
    file_descriptor, file_path = tempfile.mkstemp(suffix=".txt")
    
    os.close(file_descriptor)
    return Path(file_path)




def main():

    """Run the parcel-tracking demonstration."""
    first = book_parcel("Bengaluru Books", "Ravi Kumar", 2.5)
    second = book_parcel("Gadget Hub", "Sneha Rao", 0.8)
    third = book_parcel("Spice Store", "Imran Khan", 4)

    advance_status(first)
    advance_status(first)
    advance_status(second)

    for _ in range(6):
        advance_status(third)

    for tracking_id in (first, second, third):
        print(track_parcel(tracking_id))
        print("  with courier:", is_with_courier(tracking_id))
        print("  cost:", shipping_cost(parcels[tracking_id]["weight"]))

    print(track_parcel("TRK00000"))

    delivery_otp = secrets.randbelow(9000) + 1000
    logger.info("Delivery OTP for %s is %s", third, delivery_otp)
    logger.info("Parcels booked today: %d", len(parcels))


if __name__ == "__main__":
    main()
