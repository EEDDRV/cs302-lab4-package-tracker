from dataclasses import dataclass


@dataclass(frozen=True)
class Package:
    """The core business object: a package being shipped to a destination."""

    tracking_number: str
    status: str
    destination: str
