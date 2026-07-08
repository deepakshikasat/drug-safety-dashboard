import pandas as pd
import streamlit as st

st.title("Drug Safety Dashboard")
st.caption("Public openFDA FAERS reaction counts for selected drugs. Counts are spontaneous reports, not incidence rates.")
events = pd.read_csv("data/openfda_drug_event_counts.csv")
drug = st.selectbox("Drug", sorted(events.drug.unique()))
st.bar_chart(events[events.drug == drug].set_index("reaction_term")["report_count"].head(20))
st.dataframe(events)
