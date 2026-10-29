# Dependency Rule: the Entities layer is the innermost layer. It depends on
# nothing outside itself: it must not import from Use Cases, Interface
# Adapters, or Frameworks & Drivers, and it uses no frameworks (standard
# library only).
