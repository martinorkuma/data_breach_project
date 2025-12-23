## **Healthcare Data Breach Analysis (Python, WSL)**

### **Project Overview**

This project performs an end-to-end exploratory analysis of a healthcare data breach dataset using a reproducible Python pipeline executed entirely in WSL (Windows Subsystem for Linux). The analysis examines breach types, breach locations, individuals affected, business associate involvement, and temporal trends.

The repository is intentionally structured to mirror production-style data analysis and data engineering workflows, emphasizing environment isolation, version control, and automation.

### Key Skills Demonstrated

-   Linux-based development via WSL

-   Python virtual environments (venv)

-   Secure GitHub authentication using SSH

-   Data cleaning and transformation using pandas

-   Exploratory data analysis

-   Command-line-driven analysis

```{bash}
data-breach-project/
├── data/
│   ├── raw/                  # Original, immutable data
│   │   └── breach_report.csv
│   └── processed/
│       ├── breach_clean.parquet
│       ├── breach_clean.csv
│       └── tables/            # EDA summary tables
├── scripts/                   # Executable analysis pipeline
│   ├── 01_load_clean.py
│   ├── 02_eda_tables.py
│   ├── 03_visualizations.py
│   ├── 04_build_report.py
│   └── run_all.sh
├── figs/                      # Generated visualizations
├── reports/                   # Generated markdown report
├── requirements.txt
├── .gitignore
└── README.md

```

### Environment Setup (WSL)

All commands were run from a WSL (Ubuntu) terminal.

```{bash}
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Python dependencies include: pandas, pyarrow, matplotlib, and tabulate.

### Analysis Pipeline

The analysis is organized as a numbered, linear pipeline to ensure clarity and reproducibility.

1.  Data loading and cleaning:

```{bash}
python scripts/01_load_clean.py
```

Outputs cleaned datasets (`.parquet` and `.csv`)

2.  Exploratory data analysis (Tables):

```{bash}
python scripts/02_eda_tables.py
```

Output: Tables saved to data/processed/tables/

3.  Visualizations:

```{bash}
    python scripts/03_visualizations.py 
```

Output: Figures saved to figs/

4.  Report generation:

```{bash}
python scripts/04_build_report.py
```

Output: Report saved to reports/breach_report.md

I also created a shell script to easily run all commands:

```{bash}
./scripts/run_all.sh
```

### Version Control and Security

-   Git initialized and managed entirely within WSL.

-   SSH-based GitHub authentication (no passwords or tokens).

-   Clean `.gitignore` to prevent committing virtual environments or OS artifacts.

-   Repository pushed and tracked on main.

### Reproducibility

-   Raw data remains unchanged in data/raw/

-   All derived outputs were generated programmatically.

-   The project can be reproduced on any Linux system (WSL) with Python 3.


