import streamlit as st
from graphs.workflow import build_graph
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="Software Dev Agent",
    layout="wide"
)

st.title("🚀 Software Development Agent")

requirement = st.text_area("Project Requirement",height=150)

if st.button("Generate Project"):

    graph = build_graph()

    with st.spinner("Generating..."):

        result = graph.invoke({"user_requirement":requirement,"review_iterations": 0})

    st.success("Project Generated")

    st.write(result)