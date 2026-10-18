import pandas as pd

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


def get_column_statistics(columns: list[str],rows: list[dict[str, str]],) -> dict[str, dict]:
    dataframe = pd.DataFrame(rows, columns=columns)

    dataframe = dataframe.replace(r"^\s*$", pd.NA, regex=True)
    results = {}

    for column in columns:
        values = dataframe[column].dropna()
        numeric_values = pd.to_numeric(values, errors="coerce")

        if not values.empty and numeric_values.notna().all():
            results[column] = {
                "type": "numeric",
                "count": int(numeric_values.count()),
                "mean": float(numeric_values.mean()),
                "std": (
                    float(numeric_values.std())
                    if numeric_values.count() > 1
                    else None
                ),
                "min": float(numeric_values.min()),
                "median": float(numeric_values.median()),
                "max": float(numeric_values.max()),
            }
        else:
            mode = values.mode()

            results[column] = {
                "type": "categorical",
                "count": int(values.count()),
                "unique": int(values.nunique()),
                "most_frequent": (
                    str(mode.iloc[0]) if not mode.empty else None
                ),
            }

    return results