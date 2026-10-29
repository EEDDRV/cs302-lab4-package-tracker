from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from package_tracker.entities.package import Package


# --- DTOs -------------------------------------------------------------------

@dataclass(frozen=True)
class TrackPackageRequest:
    """Data going into the use case."""

    tracking_number: str


@dataclass(frozen=True)
class TrackPackageResponse:
    """Data coming out of the use case."""

    found: bool
    tracking_number: str
    status: Optional[str] = None
    destination: Optional[str] = None


# --- Boundaries and ports ---------------------------------------------------

class TrackPackageInputBoundary(ABC):
    """What the controller calls to run the use case."""

    @abstractmethod
    def execute(self, request: TrackPackageRequest) -> None:
        ...


class TrackPackageOutputBoundary(ABC):
    """What the interactor calls to hand back its result (implemented by the presenter)."""

    @abstractmethod
    def present(self, response: TrackPackageResponse) -> None:
        ...


class PackageGateway(ABC):
    """Persistence port (implemented by an outer layer)."""

    @abstractmethod
    def find_by_tracking_number(self, tracking_number: str) -> Optional[Package]:
        ...


# --- Interactor -------------------------------------------------------------

class TrackPackageInteractor(TrackPackageInputBoundary):
    def __init__(self, gateway: PackageGateway, output_boundary: TrackPackageOutputBoundary):
        self._gateway = gateway
        self._output_boundary = output_boundary

    def execute(self, request: TrackPackageRequest) -> None:
        package = self._gateway.find_by_tracking_number(request.tracking_number)

        if package is None:
            response = TrackPackageResponse(
                found=False,
                tracking_number=request.tracking_number,
            )
        else:
            response = TrackPackageResponse(
                found=True,
                tracking_number=package.tracking_number,
                status=package.status,
                destination=package.destination,
            )

        self._output_boundary.present(response)
