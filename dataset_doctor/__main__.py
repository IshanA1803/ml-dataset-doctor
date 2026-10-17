import sys
import csv
from dataset_doctor.csv_reader import read_csv


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m dataset_doctor <csv_file>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        rows = read_csv(file_path)
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    if rows:
        print("Columns:", list(rows[0].keys()))

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()