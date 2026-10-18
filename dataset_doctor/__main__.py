
import argparse
import csv
import json
import sys

from dataset_doctor.csv_reader import read_csv
from dataset_doctor.profiling import (
    get_dimensions,
    get_duplicate_count,
    get_missing_values,
    get_column_statistics,
    get_outliers,
)
from dataset_doctor.reporting import print_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ml-dataset-doctor",
        description="Profile a CSV dataset and detect data-quality issues.",
    )
    parser.add_argument(
        "csv_file",
        help="Path to the CSV file to analyze.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text).",
    )
    args = parser.parse_args(argv)

    try:
        columns, rows = read_csv(args.csv_file)
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    result = {
        "dimensions": get_dimensions(columns, rows),
        "missing_values": get_missing_values(columns, rows),
        "duplicate_count": get_duplicate_count(columns, rows),
        "column_statistics": get_column_statistics(columns, rows),
        "outliers": get_outliers(columns, rows),
    }

    if args.format == "json":
        json.dump(result, sys.stdout, indent=2, allow_nan=False)
        print()
    else:
        print_report(
            result["dimensions"],
            result["missing_values"],
            result["duplicate_count"],
            result["column_statistics"],
            result["outliers"],
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())