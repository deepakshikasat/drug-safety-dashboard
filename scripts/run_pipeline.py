from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
events = pd.read_csv(root / "data/openfda_drug_event_counts.csv")
print(events.groupby("drug").report_count.sum().sort_values(ascending=False))
