import csv
from pathlib import Path


def read_csv(file_path: str) -> list[dict[str, str]]:
    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)