from dataclasses import dataclass
from typing import List, Optional

from package_tracker.use_cases.track_package import (
    TrackPackageOutputBoundary,
    TrackPackageResponse,
)


@dataclass(frozen=True)
class TrackPackageViewModel:
    """Display-ready data. The console prints it without making any decisions."""

    headline: str
    details: List[str]


class PackagePresenter(TrackPackageOutputBoundary):
    """Turns a use case response into a view model."""

    def __init__(self):
        self.view_model: Optional[TrackPackageViewModel] = None

    def present(self, response: TrackPackageResponse) -> None:
        if response.found:
            self.view_model = TrackPackageViewModel(
                headline="Package found",
                details=[
                    f"Tracking number: {response.tracking_number}",
                    f"Status: {response.status}",
                    f"Destination: {response.destination}",
                ],
            )
        else:
            self.view_model = TrackPackageViewModel(
                headline="Package not found",
                details=[f"No package matches tracking number '{response.tracking_number}'."],
            )
