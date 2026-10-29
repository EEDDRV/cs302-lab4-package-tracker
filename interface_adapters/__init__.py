# Dependency Rule: the Interface Adapters layer may depend only on Use Cases
# and Entities (and the standard library). It must never import from
# Frameworks & Drivers. It converts data between the form the use cases use
# and the form the outside world uses.
