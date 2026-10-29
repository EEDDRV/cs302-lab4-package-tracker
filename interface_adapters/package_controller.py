from package_tracker.use_cases.track_package import (
    TrackPackageInputBoundary,
    TrackPackageRequest,
)


class PackageController:
    """Turns raw user input into a request and sends it to the input boundary."""

    def __init__(self, input_boundary: TrackPackageInputBoundary):
        self._input_boundary = input_boundary

    def track_package(self, raw_tracking_number: str) -> None:
        request = TrackPackageRequest(tracking_number=raw_tracking_number.strip())
        self._input_boundary.execute(request)
