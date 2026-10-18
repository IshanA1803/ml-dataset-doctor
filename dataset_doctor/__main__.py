import csv
import sys

from dataset_doctor.csv_reader import read_csv
from dataset_doctor.profiling import (
    get_dimensions,
    get_duplicate_count,
    get_missing_values,
    get_column_statistics,
)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m dataset_doctor <csv_file>", file=sys.stderr)
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

    print(f"Rows: {dimensions['rows']}")
    print(f"Columns: {dimensions['columns']}")

    print("\nMissing values:")

    for column, stats in missing_values.items():
        print(
            f"  {column}: {stats['count']} "
            f"({stats['percentage']:.1f}%)"
        )
    
    print(f"\nDuplicate rows: {duplicate_count}")

    print("\nColumn statistics:")

    for column, stats in column_statistics.items():
        print(f"\n{column} ({stats['type']}):")
    
        for name, value in stats.items():
            if name != "type":
                print(f"  {name}: {value}")


if __name__ == "__main__":
    main()