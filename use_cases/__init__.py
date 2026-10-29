# Dependency Rule: the Use Cases layer may depend only on Entities (and the
# standard library). It must never import from Interface Adapters or
# Frameworks & Drivers, and it uses no frameworks. Outer layers implement the
# interfaces defined here; this layer never reaches out to them.
