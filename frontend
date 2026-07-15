import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon="🐞",
    layout="wide"
)


BACKEND_URL = "http://127.0.0.1:8000/analyze"



st.title("🐞 AI Smart Bug Analyzer & Fix Advisor")

st.write("Upload a Bug Report (TXT, LOG or PDF)")

uploaded_file = st.file_uploader(
    "Choose File",
    type=["txt","pdf","log"]
)
if uploaded_file:

    if st.button("Analyze Bug"):

        with st.spinner("Analyzing..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue()
                )
            }

            try:
                response = requests.post(
                    BACKEND_URL,
                    files=files
                )

                response.raise_for_status()

                data = response.json()


            except Exception as e:
                st.error(f"Backend Error: {e}")
                st.stop()

        st.success("Analysis Completed")

        st.header("Triage Agent")

        c1,c2,c3,c4 = st.columns(4)

        c1.metric(
            "Severity",
            data["triage"]["severity"]
        )

        c2.metric(
            "Priority",
            data["triage"]["priority"]
        )

        c3.metric(
            "Component",
            data["triage"]["component"]
        )

        c4.metric(
            "Confidence",
            str(data["triage"]["confidence"])+"%"
        )

        st.info(data["triage"]["reasoning"])

        st.header("Log Analysis")

        st.write("Exception")

        st.code(data["log_analysis"]["exception"])

        st.write("Failure Point")

        st.code(data["log_analysis"]["failure_point"])

        st.write("Code Path")

        st.code(data["log_analysis"]["code_path"])

        st.write("Message")

        st.code(data["log_analysis"]["message"])

        st.header("Similar Bugs")

        df = pd.DataFrame(data["similar_bugs"])

        st.dataframe(df,use_container_width=True)

