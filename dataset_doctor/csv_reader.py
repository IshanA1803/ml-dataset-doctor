import csv
from pathlib import Path


def read_csv(file_path: str) -> list[dict[str, str]]:
    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or missing a header row.")

        return list(reader)