# ML Dataset Doctor

A Python CLI tool that profiles CSV datasets and identifies common data-quality issues.

## Features

- Dataset dimensions (rows and columns)
- Missing-value counts and percentages
- Duplicate-row detection
- Numeric and categorical column statistics
- Potential numeric outlier detection using the IQR method
- Console reports and JSON output

## Requirements

- Python 3.10+
- pandas

## Setup

```bash
git clone https://github.com/IshanA1803/ml-dataset-doctor
cd ml-dataset-doctor

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## Usage

Generate a console report:

```bash
python -m dataset_doctor data/customers.csv
```

Generate JSON:

```bash
python -m dataset_doctor data/customers.csv --format json
```

Display help:

```bash
python -m dataset_doctor --help
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Limitations

This is an incremental learning project. Numeric type inference is heuristic, and detected outliers are warnings rather than proof of invalid data.