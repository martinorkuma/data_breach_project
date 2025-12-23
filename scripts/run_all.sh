#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
python scripts/01_load_clean.py
python scripts/02_eda_tables.py
python scripts/03_visualizations.py
python scripts/04_build_report.py
echo "Pipeline complete."
