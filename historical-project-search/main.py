
import csv
import time
import traceback
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

SUPPLIER_COLUMNS = [
    "supplier_id",
    "supplier_name",
    "industry",
    "capability",
    "location"
]

PROJECT_COLUMNS = [
    "project_id",
    "industry",
    "capability",
    "location"
]


# STEP 1: Load CSV files
def load_csv(filename, required_columns):

    file_path = DATA_DIR / filename

    print(f"[INFO] Looking for: {file_path}", flush=True)

    if not file_path.is_file():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    with open(
        file_path,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError(
                f"{filename} is empty or has no headers."
            )

        # Clean CSV column headings
        reader.fieldnames = [
            name.strip().lower()
            for name in reader.fieldnames
        ]

        # Check required columns
        missing = [
            column for column in required_columns
            if column not in reader.fieldnames
        ]

        if missing:
            raise ValueError(
                f"Missing columns in {filename}: {missing}\n"
                f"Columns found: {reader.fieldnames}"
            )

        rows = []

        for row in reader:

            clean_row = {
                key.strip().lower(): value.strip()
                for key, value in row.items()
                if key is not None and value is not None
            }

            if any(clean_row.values()):
                rows.append(clean_row)

    print(
        f"[OK] Loaded {len(rows)} rows from {filename}",
        flush=True
    )

    return rows


# STEP 2: Calculate matching score
def calculate_score(supplier, project):

    score = 0

    if supplier["industry"].casefold() == project["industry"].casefold():
        score += 1

    if supplier["capability"].casefold() == project["capability"].casefold():
        score += 1

    if supplier["location"].casefold() == project["location"].casefold():
        score += 1

    return (score / 3) * 100


# STEP 3: Search historical projects
def search_projects(supplier, projects):

    matches = []

    for project in projects:

        score = calculate_score(supplier, project)

        if score > 0:

            matches.append({
                "supplier": supplier["supplier_name"],
                "project_id": project["project_id"],
                "score": score
            })

    return matches


# STEP 4: Run serial processing
def run_serial_search(suppliers, projects):

    all_results = []

    start_time = time.perf_counter()

    for supplier in suppliers:

        results = search_projects(supplier, projects)

        all_results.extend(results)

    execution_time = time.perf_counter() - start_time

    return all_results, execution_time


# STEP 5: Main program
def main():

    print("=" * 60)
    print("HISTORICAL PROJECT SEARCH SYSTEM")
    print("=" * 60)

    print("\n[STEP 1] Starting data loading...")

    suppliers = load_csv(
        "suppliers.csv",
        SUPPLIER_COLUMNS
    )

    print("\n[STEP 2] Loading historical project data...")

    projects = load_csv(
        "historical_projects.csv",
        PROJECT_COLUMNS
    )

    print("\n[STEP 3] Checking loaded data...")

    print("Total suppliers:", len(suppliers))
    print("Historical projects:", len(projects))

    if not suppliers or not projects:
        print("\n[WARNING] No data available for searching.")
        return

    print("\n[STEP 4] Starting serial search...")

    results, execution_time = run_serial_search(
        suppliers,
        projects
    )

    print("\n" + "-" * 65)

    print(
        f"{'SUPPLIER':<25}"
        f"{'PROJECT ID':<15}"
        f"{'SCORE':<15}"
    )

    print("-" * 65)

    if results:

        for result in results:

            print(
                f"{result['supplier']:<25}"
                f"{result['project_id']:<15}"
                f"{result['score']:.2f}%"
            )

    else:
        print("No matching records found.")

    print("-" * 65)

    print("\nSEARCH SUMMARY")

    print("Total suppliers:", len(suppliers))
    print("Total historical projects:", len(projects))
    print("Total matching records:", len(results))

    print(
        f"Execution time: {execution_time:.6f} seconds"
    )

    print("\nSerial search completed successfully!")


# STEP 6: Execute program
if __name__ == "__main__":

    try:
        main()

    except Exception:

        print("\n[ERROR] Program stopped:")
        traceback.print_exc()
