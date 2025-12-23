#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

IN_PATH = Path("data/processed/breach_clean.parquet")
OUT_DIR = Path("data/processed/tables")

def main() -> None:
    df = pd.read_parquet(IN_PATH)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    tab_breach_type = (
        df.groupby("breach_type", dropna=False)
          .size()
          .reset_index(name="n")
          .sort_values("n", ascending=False)
    )
    tab_breach_type["pct"] = tab_breach_type["n"] / tab_breach_type["n"].sum()
    tab_breach_type.to_csv(OUT_DIR / "tab_breach_type.csv", index=False)

    tab_location = (
        df.groupby("breach_location", dropna=False)
          .size()
          .reset_index(name="n")
          .sort_values("n", ascending=False)
    )
    tab_location["pct"] = tab_location["n"] / tab_location["n"].sum()
    tab_location.to_csv(OUT_DIR / "tab_location.csv", index=False)

    impact_summary = {
        "n_events": int(len(df)),
        "total_individuals": float(df["individuals_affected"].sum(skipna=True)),
        "median_affected": float(df["individuals_affected"].median(skipna=True)),
        "p90_affected": float(df["individuals_affected"].quantile(0.90)),
        "max_affected": float(df["individuals_affected"].max(skipna=True)),
    }
    print("Impact summary:", impact_summary)

    tab_monthly = (
        df.groupby("month", dropna=False)
          .agg(
              events=("month", "size"),
              total_affected=("individuals_affected", "sum"),
              median_affected=("individuals_affected", "median"),
          )
          .reset_index()
          .sort_values("month")
    )
    tab_monthly.to_csv(OUT_DIR / "tab_monthly.csv", index=False)

    tab_ba = (
        df.groupby("ba_present", dropna=False)
          .agg(
              events=("ba_present", "size"),
              total_affected=("individuals_affected", "sum"),
              median_affected=("individuals_affected", "median"),
          )
          .reset_index()
          .sort_values("events", ascending=False)
    )
    tab_ba.to_csv(OUT_DIR / "tab_ba.csv", index=False)

    cols = [c for c in [
        "submission_date","month","state","covered_entity","entity_type",
        "breach_type","breach_location","ba_present","individuals_affected"
    ] if c in df.columns]

    tab_top10 = (
        df.loc[df["individuals_affected"].notna(), cols]
          .sort_values("individuals_affected", ascending=False)
          .head(10)
    )
    tab_top10.to_csv(OUT_DIR / "tab_top10_events.csv", index=False)

if __name__ == "__main__":
    main()
