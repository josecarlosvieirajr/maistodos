class CRUDUpdateError(Exception):
    def __init__(self, *, obj_id) -> None:
        super().__init__(
            f"Not updated, reference object not found, ReferenceObject<{obj_id}>"
        )
