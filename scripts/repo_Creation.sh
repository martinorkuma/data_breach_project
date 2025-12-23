# Create project folder (edit to your preferred location)
cd /mnt/c/Users/marty/OneDrive/Desktop/MyProjects
mkdir data-breach-project
cd data-breach-project

git init
git branch -m main # Renaming the initial branch from master to main

# Create the internal repo folders
mkdir -p data/raw data/processed/tables scripts reports figs
# Copy the data set csv to your desired location
cp /mnt/c/Users/marty/OneDrive/Desktop/MyProjects/breach_report.csv data/raw/breach_report.csv

nano .gitignore # Create git ignore for Python
    # Python / venv
    .venv/
    __pycache__/
    *.pyc

    # OS junk
    .DS_Store
    Thumbs.db

    # Optional: logs
    *.log


# Commit the scaffold
git add .
git commit -m "Initialize data breach analysis project structure (Python)"

sudo apt install -y python3-venv python3-pip # creating a venv environment
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip

nano requirements.txt
    pandas>=2.0
    pyarrow>=14.0
    python-dateutil>=2.8
    matplotlib>=3.8
    tabulate>=0.9
pip install -r requirements.txt

pip install pandas numpy matplotlib seaborn scikit-learn ipykernel # installing required libraries

# Launching JupyterLab from WSL
source .venv/bin/activate
pip install jupyterlab ipykernel
jupyter lab --no-browser

# Creating script 01_load_clean.py in JupyterLab
# Run script 01
source .venv/bin/activate
python scripts/01_load_clean.py

# script 02_eda_tables.py was created in JupyterLab
python scripts/02_eda_tables.py # Run script 02

# Script 03_visualizations.py was created in JupyterLab
python scripts/03_visualizations.py # Run the script

# Script 04 was created using nano in WSL
nano 04_build_report.py
python scripts/04_build_report.py # run script 04

# Create a nano script to run all scripts
nano scripts/run_all.sh
    #!/usr/bin/env bash
    set -euo pipefail

    source .venv/bin/activate
    python scripts/01_load_clean.py
    python scripts/02_eda_tables.py
    python scripts/03_visualizations.py
    python scripts/04_build_report.py
    echo "Pipeline complete."

chmod +x scripts/run_all.sh
./scripts/run_all.sh
