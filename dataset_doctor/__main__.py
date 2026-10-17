import sys

from dataset_doctor.csv_reader import read_csv


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m dataset_doctor <csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    rows = read_csv(file_path)

    if rows:
        print("Columns:", list(rows[0].keys()))

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()