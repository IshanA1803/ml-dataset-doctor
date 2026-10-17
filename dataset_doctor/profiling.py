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

def get_duplicate_count(columns: list[str],rows: list[dict[str, str]],) -> int:
    seen = set()
    duplicate_count = 0

    for row in rows:
        row_values = tuple(row[column] for column in columns)

        if row_values in seen:
            duplicate_count += 1
        else:
            seen.add(row_values)

    return duplicate_count