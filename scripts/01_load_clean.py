# 01_load_clean.py

#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

IN_PATH = Path("data/raw/breach_report.csv")
OUT_PARQUET = Path("data/processed/breach_clean.parquet")
OUT_CSV = Path("data/processed/breach_clean.csv")

def main() -> None:
    df = pd.read_csv(IN_PATH)

    df = df.rename(columns={
        "Name of Covered Entity": "covered_entity",
        "State": "state",
        "Covered Entity Type": "entity_type",
        "Individuals Affected": "individuals_affected",
        "Breach Submission Date": "submission_date",
        "Type of Breach": "breach_type",
        "Location of Breached Information": "breach_location",
        "Business Associate Present": "ba_present",
        "Web Description": "web_description",
    })

    # Normalize text fields
    for col in ["covered_entity", "state", "entity_type", "breach_type", "breach_location", "ba_present"]:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip().replace({"": pd.NA})

    # Numeric + date parsing
    df["individuals_affected"] = pd.to_numeric(df["individuals_affected"], errors="coerce")

    # Most datasets are M/D/YYYY; infer if possible
    df["submission_date"] = pd.to_datetime(df["submission_date"], errors="coerce", infer_datetime_format=True)

    df["year"] = df["submission_date"].dt.year
    df["month"] = df["submission_date"].dt.to_period("M").dt.to_timestamp()

    qa = {
        "n_rows": int(len(df)),
        "min_date": str(df["submission_date"].min()),
        "max_date": str(df["submission_date"].max()),
        "missing_dates": int(df["submission_date"].isna().sum()),
        "missing_state": int(df["state"].isna().sum()) if "state" in df.columns else None,
        "web_description_all_missing": bool(df["web_description"].isna().all()) if "web_description" in df.columns else None
    }
    print("QA:", qa)

    OUT_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT_PARQUET, index=False)
    df.to_csv(OUT_CSV, index=False)

if __name__ == "__main__":
    main()
