import csv
import sys

from dataset_doctor.csv_reader import read_csv
from dataset_doctor.profiling import get_dimensions


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

    print(f"Rows: {dimensions['rows']}")
    print(f"Columns: {dimensions['columns']}")


if __name__ == "__main__":
    main()