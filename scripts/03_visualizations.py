#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

IN_PATH = Path("data/processed/breach_clean.parquet")
FIG_DIR = Path("figs")

def comma_fmt(x, pos):
    try:
        return f"{int(x):,}"
    except Exception:
        return str(x)

def main() -> None:
    df = pd.read_parquet(IN_PATH)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Breach type counts
    tab = df.groupby("breach_type", dropna=False).size().sort_values(ascending=True)
    plt.figure()
    tab.plot(kind="barh")
    plt.title("Breach Events by Type")
    plt.xlabel("Number of events")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "breach_type_counts.png", dpi=300)
    plt.close()

    # 2) Monthly events trend
    tab_m = df.groupby("month", dropna=False).size().sort_index()
    plt.figure()
    plt.plot(tab_m.index, tab_m.values, marker="o")
    plt.title("Monthly Trend in Reported Breaches")
    plt.xlabel("")
    plt.ylabel("Events")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "monthly_events_trend.png", dpi=300)
    plt.close()

    # 3) Individuals affected by breach type (log scale)
    df_pos = df[(df["individuals_affected"].notna()) & (df["individuals_affected"] > 0)]
    groups, labels = [], []
    for k, g in df_pos.groupby("breach_type"):
        groups.append(g["individuals_affected"].values)
        labels.append(str(k))

    plt.figure(figsize=(10, 5))
    plt.boxplot(groups, tick_labels=labels, showfliers=True)
    plt.yscale("log")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_fmt))
    plt.title("Individuals Affected by Breach Type (log scale)")
    plt.xlabel("")
    plt.ylabel("Individuals affected")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "affected_by_type_log.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    main()
