# Package Tracker

A small Clean Architecture example in plain Python (standard library only).
It does one thing: look up a package by its tracking number.

## Structure

```
package_tracker/
├── entities/                 # Layer 1: business objects
│   └── package.py            #   Package (tracking number, status, destination)
├── use_cases/                # Layer 2: application logic
│   └── track_package.py      #   DTOs, input/output boundaries, gateway port, interactor
├── interface_adapters/       # Layer 3: converters between use cases and the outside
│   ├── package_controller.py #   raw input -> request
│   ├── package_presenter.py  #   response -> view model (also defines the view model)
│   └── in_memory_package_gateway.py  # dict-backed PackageGateway
├── frameworks_and_drivers/   # Layer 4: outermost shell
│   └── main.py               #   wiring (manual DI) and console I/O
└── README.md
```

## The Dependency Rule

Source code dependencies point inward only:

    Frameworks & Drivers -> Interface Adapters -> Use Cases -> Entities

Each layer's `__init__.py` states the rule for that layer. The inner two
layers (Entities, Use Cases) import only the standard library.

## Flow

    Controller -> Input Boundary -> Interactor -> Entity
               -> Output Boundary -> Presenter -> View Model -> Console

The use case defines `PackageGateway` and `TrackPackageOutputBoundary`, and
the outer layers implement them. That is how control flows outward at runtime
while the imports still point inward.

## Run it

Requires Python 3.8+. From the directory that **contains** the `package_tracker`
folder:

    python -m package_tracker.frameworks_and_drivers.main

Then enter a tracking number. Predefined packages:

| Tracking number | Status         | Destination |
|-----------------|----------------|-------------|
| PK1001          | In Transit     | Austin, TX  |
| PK1002          | Delivered      | Seattle, WA |
| PK1003          | Label Created  | Boston, MA  |

Anything else shows "Package not found". Press Enter on an empty line to quit.

Example session:

    Package Tracker (press Enter on an empty line to quit)
    Try: PK1001, PK1002, PK1003
    Tracking number: PK1001

    Package found
      Tracking number: PK1001
      Status: In Transit
      Destination: Austin, TX
