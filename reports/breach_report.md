# Data Breach Analysis (Healthcare) — Exploratory Report

## How to reproduce

Run: `python scripts/01_load_clean.py`, `02_eda_tables.py`, `03_visualizations.py`, `04_build_report.py`

## Breach Type Landscape

| breach_type                    |   n |        pct |
|:-------------------------------|----:|-----------:|
| Hacking/IT Incident            | 625 | 0.842318   |
| Unauthorized Access/Disclosure | 106 | 0.142857   |
| Theft                          |   7 | 0.00943396 |
| Loss                           |   2 | 0.00269542 |
| Improper Disposal              |   2 | 0.00269542 |

## Breach Location Patterns

| breach_location                           |   n |        pct |
|:------------------------------------------|----:|-----------:|
| Network Server                            | 480 | 0.6469     |
| Email                                     | 167 | 0.225067   |
| Paper/Films                               |  27 | 0.0363881  |
| Electronic Medical Record                 |  22 | 0.0296496  |
| Other                                     |  13 | 0.0175202  |
| Desktop Computer, Network Server          |   5 | 0.00673854 |
| Desktop Computer                          |   4 | 0.00539084 |
| Laptop                                    |   4 | 0.00539084 |
| Electronic Medical Record, Network Server |   4 | 0.00539084 |
| Desktop Computer, Laptop                  |   2 | 0.00269542 |

## Business Associate Involvement

| ba_present   |   events |   total_affected |   median_affected |
|:-------------|---------:|-----------------:|------------------:|
| No           |      522 |         65762906 |            6622.5 |
| Yes          |      220 |        228129583 |            4242.5 |

## Time Trend (Monthly)

| month      |   events |   total_affected |   median_affected |
|:-----------|---------:|-----------------:|------------------:|
| 2023-02-01 |        1 |              566 |             566   |
| 2023-03-01 |        1 |            39674 |           39674   |
| 2023-08-01 |        2 |           579168 |          289584   |
| 2023-10-01 |        1 |            10833 |           10833   |
| 2023-11-01 |        5 |           144898 |            9240   |
| 2023-12-01 |       11 |          4977376 |           63776   |
| 2024-01-01 |       15 |          3275724 |           23686   |
| 2024-02-01 |       11 |           921501 |            3640   |
| 2024-03-01 |       16 |           754256 |            3617.5 |
| 2024-04-01 |       20 |         15804872 |           36214   |
| 2024-05-01 |       21 |          8506307 |           81588   |
| 2024-06-01 |       14 |          2215483 |           15099.5 |

## Top 10 Largest Events

| submission_date   | month      | state   | covered_entity                           | entity_type         | breach_type                    | breach_location   | ba_present   |   individuals_affected |
|:------------------|:-----------|:--------|:-----------------------------------------|:--------------------|:-------------------------------|:------------------|:-------------|-----------------------:|
| 2024-07-19        | 2024-07-01 | MN      | Change Healthcare, Inc.                  | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |              192700000 |
| 2024-04-12        | 2024-04-01 | CA      | Kaiser Foundation Health Plan, Inc.      | Health Plan         | Unauthorized Access/Disclosure | Network Server    | No           |               13400000 |
| 2024-07-03        | 2024-07-01 | MO      | Ascension Health                         | Healthcare Provider | Hacking/IT Incident            | Network Server    | No           |                5466931 |
| 2025-06-06        | 2025-06-01 | CA      | Episource, LLC                           | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |                5418866 |
| 2025-04-09        | 2025-04-01 | CA      | Blue Shield of California                | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |                4700000 |
| 2024-08-09        | 2024-08-01 | UT      | HealthEquity, Inc.                       | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |                4300000 |
| 2024-08-20        | 2024-08-01 | LA      | Acadian Ambulance Service, Inc.          | Healthcare Provider | Hacking/IT Incident            | Network Server    | No           |                2896985 |
| 2024-05-24        | 2024-05-01 | NE      | A&A Services d/b/a Sav-Rx                | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |                2812336 |
| 2025-08-01        | 2025-08-01 | CO      | DaVita Inc.                              | Healthcare Provider | Hacking/IT Incident            | Network Server    | No           |                2689826 |
| 2024-05-08        | 2024-05-01 | TX      | WebTPA Employer Services, LLC (“WebTPA”) | Business Associate  | Hacking/IT Incident            | Network Server    | Yes          |                2518533 |

## Figures

- `figs/breach_type_counts.png`

- `figs/monthly_events_trend.png`

- `figs/affected_by_type_log.png`
