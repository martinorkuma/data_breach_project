# 04_build_report.py 
#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

TABLES = Path("data/processed/tables")
OUT = Path("reports/breach_report.md")

def md_table(df: pd.DataFrame, n: int = 10) -> str:
    return df.head(n).to_markdown(index=False)

def main() -> None:
    breach_type = pd.read_csv(TABLES / "tab_breach_type.csv")
    location = pd.read_csv(TABLES / "tab_location.csv")
    monthly = pd.read_csv(TABLES / "tab_monthly.csv")
    ba = pd.read_csv(TABLES / "tab_ba.csv")
    top10 = pd.read_csv(TABLES / "tab_top10_events.csv")

    OUT.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Data Breach Analysis (Healthcare) — Exploratory Report\n")
    lines.append("## How to reproduce\n")
    lines.append("Run: `python scripts/01_load_clean.py`, `02_eda_tables.py`, `03_visualizations.py`, `04_build_report.py`\n")

    lines.append("## Breach Type Landscape\n")
    lines.append(md_table(breach_type, 10) + "\n")

    lines.append("## Breach Location Patterns\n")
    lines.append(md_table(location, 10) + "\n")

    lines.append("## Business Associate Involvement\n")
    lines.append(md_table(ba, 10) + "\n")

    lines.append("## Time Trend (Monthly)\n")
    lines.append(md_table(monthly, 12) + "\n")

    lines.append("## Top 10 Largest Events\n")
    lines.append(md_table(top10, 10) + "\n")

    lines.append("## Figures\n")
    lines.append("- `figs/breach_type_counts.png`\n")
    lines.append("- `figs/monthly_events_trend.png`\n")
    lines.append("- `figs/affected_by_type_log.png`\n")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
