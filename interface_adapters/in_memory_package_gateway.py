from typing import Dict, Optional

from package_tracker.entities.package import Package
from package_tracker.use_cases.track_package import PackageGateway


class InMemoryPackageGateway(PackageGateway):
    """Keeps a few predefined packages in a dict. No database involved."""

    def __init__(self):
        self._packages: Dict[str, Package] = {
            "PK1001": Package("PK1001", "In Transit", "Austin, TX"),
            "PK1002": Package("PK1002", "Delivered", "Seattle, WA"),
            "PK1003": Package("PK1003", "Label Created", "Boston, MA"),
        }

    def find_by_tracking_number(self, tracking_number: str) -> Optional[Package]:
        return self._packages.get(tracking_number)
