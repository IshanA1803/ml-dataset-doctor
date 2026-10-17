def get_dimensions(columns: list[str],rows: list[dict[str, str]],) -> dict[str, int]:
    return {
        "rows": len(rows),
        "columns": len(columns),
    }