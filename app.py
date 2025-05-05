import streamlit as st
import json

# Load command mappings
with open("commands.json", "r") as file:
    command_map = json.load(file)

st.set_page_config(page_title="Multi-Vendor CLI Reference", layout="centered")

st.title("📟 Multi-Vendor CLI Command Reference")
st.markdown("Compare network CLI commands across Cisco, Fortinet, Palo Alto, and Juniper.")

# Dropdown to choose a task
task = st.selectbox("Select a common network task", list(command_map.keys()))

if task:
    st.subheader(f"🔍 Command for: {task}")
    comparison = command_map[task]
    st.table({vendor: [cmd] for vendor, cmd in comparison.items()})

st.markdown("---")
st.caption("Built by Ama · Powered by Streamlit 🚀")