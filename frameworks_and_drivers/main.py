from package_tracker.interface_adapters.in_memory_package_gateway import InMemoryPackageGateway
from package_tracker.interface_adapters.package_controller import PackageController
from package_tracker.interface_adapters.package_presenter import (
    PackagePresenter,
    TrackPackageViewModel,
)
from package_tracker.use_cases.track_package import TrackPackageInteractor


def read_tracking_number() -> str:
    try:
        text = input("Tracking number: ")
    except EOFError:
        text = ""
    return text


def print_view_model(view_model: TrackPackageViewModel) -> None:
    print()
    print(view_model.headline)
    for line in view_model.details:
        print("  " + line)
    print()


def main() -> None:
    # Manual dependency injection: build every object here, innermost first.
    gateway = InMemoryPackageGateway()
    presenter = PackagePresenter()
    interactor = TrackPackageInteractor(gateway, presenter)
    controller = PackageController(interactor)

    print("Package Tracker (press Enter on an empty line to quit)")
    print("Try: PK1001, PK1002, PK1003")

    raw_input_text = read_tracking_number()
    while raw_input_text.strip() != "":
        controller.track_package(raw_input_text)
        print_view_model(presenter.view_model)
        raw_input_text = read_tracking_number()


if __name__ == "__main__":
    main()
