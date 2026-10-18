import unittest

from dataset_doctor.profiling import (
    get_dimensions,
    get_missing_values,
    get_duplicate_count,
    get_column_statistics,
    get_outliers,
)


class TestProfiling(unittest.TestCase):
    def setUp(self):
        self.columns = ["age", "income"]
        self.rows = [
            {"age": "22", "income": "35000"},
            {"age": "35", "income": "62000"},
            {"age": "22", "income": "35000"},
        ]

    def test_get_dimensions(self):
        self.assertEqual(
            get_dimensions(self.columns, self.rows),
            {"rows": 3, "columns": 2},
        )

    def test_get_missing_values(self):
        rows = [
            {"age": "22", "income": "35000"},
            {"age": "", "income": "62000"},
            {"age": "35", "income": " "},
        ]

        result = get_missing_values(self.columns, rows)

        self.assertEqual(result["age"]["count"], 1)
        self.assertAlmostEqual(result["age"]["percentage"], 100 / 3)
        self.assertEqual(result["income"]["count"], 1)

    def test_get_duplicate_count(self):
        self.assertEqual(
            get_duplicate_count(self.columns, self.rows),
            1,
        )

    def test_get_column_statistics(self):
        result = get_column_statistics(self.columns, self.rows)

        self.assertEqual(result["age"]["type"], "numeric")
        self.assertEqual(result["age"]["count"], 3)
        self.assertAlmostEqual(result["age"]["mean"], 79 / 3)

    def test_get_outliers(self):
        columns = ["value"]
        rows = [{"value": str(value)} for value in [10, 11, 12, 13, 14, 100]]

        result = get_outliers(columns, rows)

        self.assertEqual(result["value"]["count"], 1)
        self.assertEqual(result["value"]["values"], [100.0])

    def test_empty_dataset(self):
        self.assertEqual(get_dimensions(self.columns, []), {
            "rows": 0,
            "columns": 2,
        })
        self.assertEqual(get_duplicate_count(self.columns, []), 0)
        self.assertEqual(
            get_missing_values(self.columns, []),
            {
                "age": {"count": 0, "percentage": 0.0},
                "income": {"count": 0, "percentage": 0.0},
            },
        )


if __name__ == "__main__":
    unittest.main()
