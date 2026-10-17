def get_dimensions(columns: list[str],rows: list[dict[str, str]],) -> dict[str, int]:
    return {
        "rows": len(rows),
        "columns": len(columns),
    }

def get_missing_values(columns: list[str],rows: list[dict[str, str]],) -> dict[str, dict[str, int | float]]:
    results = {}

    for column in columns:
        missing_count = sum(
            1
            for row in rows
            if not row[column] or not row[column].strip()
        )

        percentage = (
            missing_count / len(rows) * 100
            if rows
            else 0.0
        )

        results[column] = {
            "count": missing_count,
            "percentage": percentage,
        }

    return results