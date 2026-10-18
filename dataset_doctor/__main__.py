import csv
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


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "Usage: python -m dataset_doctor <csv_file>",
            file=sys.stderr,
        )
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        columns, rows = read_csv(file_path)
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    dimensions = get_dimensions(columns, rows)
    missing_values = get_missing_values(columns, rows)
    duplicate_count = get_duplicate_count(columns, rows)
    column_statistics = get_column_statistics(columns, rows)
    outliers = get_outliers(columns, rows)

    print_report(
        dimensions,
        missing_values,
        duplicate_count,
        column_statistics,
        outliers,
    )


if __name__ == "__main__":
    main()