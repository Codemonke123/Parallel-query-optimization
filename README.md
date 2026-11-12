# Historical Project Search Optimization System

A Python-based mini project that simulates searching historical project records to identify potential supplier matches. The project focuses on understanding search execution, performance measurement, and optimization techniques relevant to Cloud & DevOps engineering.

## Project Overview

Manufacturing companies often need to identify suppliers based on specific requirements such as industry, technical capabilities, and geographical location.

This project simulates a historical project search system that compares supplier information against previously completed project records and calculates a matching score.

The initial implementation uses **serial processing**, where suppliers are searched one at a time against the historical project dataset.

The long-term objective is to improve search performance through parallel processing, intelligent caching, and AWS cloud services.

## Objectives

- Build a Python-based historical project search engine.
- Load and process structured CSV datasets.
- Compare supplier information with historical project records.
- Calculate matching scores based on multiple criteria.
- Measure execution time using Python's `time` module.
- Understand the limitations of serial processing.
- Explore parallel execution and caching for performance optimization.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CSV | Dataset storage and management |
| Python `csv` module | Reading structured records |
| Python `time` module | Measuring execution time |
| pathlib | File and directory management |

## Project Structure

```text
historical-project-search/
│
├── data/
│   ├── suppliers.csv
│   └── historical_projects.csv
│
├── results/
│
├── main.py
│
└── README.md
```

## How the System Works

1. **Data Loading:** Reads supplier and historical project records from CSV files.
2. **Data Validation:** Checks required columns and handles formatting inconsistencies.
3. **Matching Process:** Compares each supplier against historical project records.
4. **Score Calculation:** Calculates a matching percentage based on three criteria.
5. **Performance Measurement:** Measures the total execution time of the serial search.
6. **Results:** Displays matching suppliers, project IDs, scores, and execution time.

## Matching Logic

The system evaluates three criteria:

- Industry Match
- Technical Capability Match
- Location Match

Each matching criterion contributes one point.

**Matching Score Formula:**

```text
Matching Score = (Matched Criteria / 3) × 100
```

Example:

| Criteria | Supplier | Historical Project | Match |
|---|---|---|---|
| Industry | Automotive | Automotive | Yes |
| Capability | CNC | CNC | Yes |
| Location | Pune | Pune | Yes |

**Final Matching Score: 100%**

A higher score indicates a closer match based on the three criteria used in this simulation.

## Getting Started

### Prerequisites

- Python 3 installed.
- Visual Studio Code or another Python editor.
- Basic knowledge of Python and CSV files.

### Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd historical-project-search
```

### Run the Application

Execute the following command:

```bash
python main.py
```

The program loads both CSV datasets, performs serial searches, and displays matching results with execution time.

## Current Implementation

The current version implements:

- CSV-based data loading.
- Supplier and historical project comparison.
- Matching score calculation.
- Serial search execution.
- Execution time measurement.
- Basic CSV validation and error handling.

## Planned Improvements

The project will be developed in multiple stages:

**Phase 1 – Basic Search Engine**
- [x] Create supplier dataset.
- [x] Create historical project dataset.
- [x] Implement serial search.
- [x] Calculate matching scores.
- [x] Measure execution time.

**Phase 2 – Performance Optimization**
- [ ] Generate larger datasets.
- [ ] Implement parallel processing using Python `ThreadPoolExecutor`.
- [ ] Implement caching to reuse previously calculated results.
- [ ] Compare serial and parallel execution times.

**Phase 3 – AWS Cloud Integration**
- [ ] Store datasets in Amazon S3.
- [ ] Explore AWS Lambda for distributed processing.
- [ ] Use Amazon SQS for task distribution.
- [ ] Explore DynamoDB for caching.
- [ ] Use Amazon CloudWatch for monitoring.

## Learning Outcomes

This project is designed to develop practical understanding of:

- Python programming and data processing.
- Serial versus parallel execution.
- Search performance optimization.
- Caching concepts.
- AWS cloud infrastructure fundamentals.
- Monitoring and performance measurement.

## Disclaimer

This is an educational simulation inspired by common supplier-matching and historical-data search optimization challenges. It does not use proprietary code, datasets, scoring algorithms, or internal infrastructure from Vulcury or Trustbridge.

---

**Project Status:** Initial Python implementation – Serial Search Engine

**Future Direction:** Parallel Processing, Caching, and AWS Cloud Integration.
