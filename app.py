import streamlit as st

st.set_page_config(page_title="Nexora AI", layout="centered")

st.title("🏗️ Nexora AI")
st.subheader("Global Infrastructure Resilience Audit")

location = st.text_input("Enter Project Coordinates (e.g., 31.5204, 74.3587):")

if st.button("Generate Resilience Audit"):
    if location:
        st.write(f"Analyzing infrastructure risk for: {location}")
        st.success("Analysis report generated successfully!")
    else:
        st.error("Please enter coordinates first.")

st.markdown("---")
st.write("Nexora AI - Professional Audit in Seconds")
