class Supplier:
    """A supplier can be associated with many inventory products."""

    def __init__(self, supplier_id: str, name: str) -> None:
        if not supplier_id or not name:
            raise ValueError("Supplier ID and name must not be empty.")
        self.supplier_id = supplier_id
        self.name = name

    def __repr__(self) -> str:
        return f"Supplier({self.supplier_id!r}, {self.name!r})"
