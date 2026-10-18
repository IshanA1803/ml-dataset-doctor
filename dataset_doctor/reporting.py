def print_report(
    dimensions: dict[str, int],
    missing_values: dict[str, dict[str, int | float]],
    duplicate_count: int,
    column_statistics: dict[str, dict],
    outliers: dict[str, dict],
) -> None:
    print("=" * 45)
    print("           ML DATASET DOCTOR")
    print("=" * 45)

    print("\nDataset Overview")
    print(f"  Rows: {dimensions['rows']}")
    print(f"  Columns: {dimensions['columns']}")

    print("\nMissing Values")
    for column, stats in missing_values.items():
        print(
            f"  {column}: {stats['count']} "
            f"({stats['percentage']:.1f}%)"
        )

    print(f"\nDuplicate Rows: {duplicate_count}")

    print("\nColumn Statistics")
    for column, stats in column_statistics.items():
        print(f"\n  {column} ({stats['type']})")

        for name, value in stats.items():
            if name == "type":
                continue

            if isinstance(value, float):
                print(f"    {name}: {value:.2f}")
            else:
                print(f"    {name}: {value}")

    print("\nPotential Outliers")
    if not outliers:
        print("  No numeric columns available for outlier analysis.")

    for column, stats in outliers.items():
        print(f"  {column}: {stats['count']}")

        if stats["count"] > 0:
            print(f"    Values: {stats['values']}")