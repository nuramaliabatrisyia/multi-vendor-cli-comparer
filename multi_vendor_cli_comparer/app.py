import streamlit as st
import json
from rapidfuzz import process

# Load command mappings
with open("commands.json", "r") as file:
    command_map = json.load(file)

st.set_page_config(page_title="Multi-Vendor CLI Reference", layout="centered")

st.title("📟 Multi-Vendor CLI Command Reference")
st.markdown("Type a common network task or command and see the equivalent across Cisco, Fortinet, Palo Alto, and Juniper.")

# Text input for user search
user_input = st.text_input("🔍 Enter a task or partial command (e.g. 'interface summary', 'routing table')")

if user_input:
    best_match = process.extractOne(user_input, command_map.keys())

    if best_match and best_match[1] >= 60:
        task = best_match[0]
        st.success(f"Best match: **{task}**")
        comparison = command_map[task]
        st.subheader("🛠️ Equivalent Commands")
        st.table({vendor: [cmd] for vendor, cmd in comparison.items()})
    else:
        st.warning("❌ No close match found. Try a different description.")

st.markdown("---")
st.caption("Built by Ama · Powered by Streamlit 🚀")
