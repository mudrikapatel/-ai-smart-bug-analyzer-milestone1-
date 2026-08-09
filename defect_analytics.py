import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "submitted_bugs.csv"
)


# =========================================================
# SAVE ANALYSIS
# =========================================================

def save_bug_analysis(data):

    triage = data.get(
        "triage",
        {}
    )

    root = data.get(
        "root_cause",
        {}
    )

    log = data.get(
        "log_analysis",
        {}
    )

    row = {

        "date":
            pd.Timestamp.now(),

        "bug_id":
            data.get(
                "bug_id",
                "BUG-" + pd.Timestamp.now().strftime(
                    "%Y%m%d%H%M%S%f"
                )
            ),

        "severity":
            triage.get(
                "severity",
                log.get(
                    "severity",
                    "Unknown"
                )
            ),

        "priority":
            triage.get(
                "priority",
                "Unknown"
            ),

        "component":
            triage.get(
                "component",
                "Unknown"
            ),

        "category":
            triage.get(
                "category",
                "Unknown"
            ),

        "root_cause":
            root.get(
                "cause",
                log.get(
                    "root_cause",
                    "Unknown"
                )
            ),

        "root_cause_confidence":
            root.get(
                "confidence",
                0
            ),

        "duplicate_count":
            len(
                data.get(
                    "duplicates",
                    []
                )
            ),

        "recommendation_available":
            bool(
                data.get(
                    "remediation",
                    {}
                ).get(
                    "recommended_fix",
                    []
                )
            )
    }

    new_df = pd.DataFrame(
        [row]
    )

    if os.path.exists(DATA_FILE):

        old_df = pd.read_csv(
            DATA_FILE
        )

        df = pd.concat(
            [
                old_df,
                new_df
            ],
            ignore_index=True
        )

    else:

        df = new_df

    df.to_csv(
        DATA_FILE,
        index=False
    )


# =========================================================
# LOAD DATA
# =========================================================

def load_analytics_data():

    if not os.path.exists(
        DATA_FILE
    ):

        return pd.DataFrame(
            columns=[
                "date",
                "bug_id",
                "severity",
                "priority",
                "component",
                "category",
                "root_cause",
                "root_cause_confidence",
                "duplicate_count",
                "recommendation_available"
            ]
        )

    df = pd.read_csv(
        DATA_FILE
    )

    if "date" in df.columns:

        df["date"] = pd.to_datetime(
            df["date"],
            errors="coerce"
        )

    return df


# =========================================================
# ANALYTICS DASHBOARD
# =========================================================

def analytics_dashboard():

    st.title(
        "📊 Defect Pattern Analytics Dashboard"
    )

    df = load_analytics_data()

    if df.empty:

        st.info(
            "No submitted bugs available yet. "
            "Analyze bug reports from the Bug Analyzer page."
        )

        return

    # -----------------------------------------------------
    # KPI
    # -----------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Bugs",
            len(df)
        )

    with c2:
        st.metric(
            "High Severity",
            int(
                (
                    df["severity"]
                    .astype(str)
                    .str.lower()
                    == "high"
                ).sum()
            )
        )

    with c3:
        st.metric(
            "Components",
            df["component"].nunique()
        )

    with c4:
        st.metric(
            "Root Cause Types",
            df["root_cause"].nunique()
        )

    st.divider()

    # -----------------------------------------------------
    # SEVERITY
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🔥 Severity Distribution"
        )

        severity = (
            df["severity"]
            .value_counts()
        )

        st.bar_chart(
            severity
        )

    # -----------------------------------------------------
    # COMPONENT
    # -----------------------------------------------------

    with col2:

        st.subheader(
            "🧩 Frequently Affected Components"
        )

        components = (
            df["component"]
            .value_counts()
            .head(10)
        )

        st.bar_chart(
            components
        )

    st.divider()

    # -----------------------------------------------------
    # ROOT CAUSE
    # -----------------------------------------------------

    st.subheader(
        "🧠 Most Frequent Root Causes"
    )

    root_causes = (
        df["root_cause"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(
        root_causes
    )

    st.divider()

    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    st.subheader(
        "🔁 Recurring Bug Categories"
    )

    categories = (
        df["category"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(
        categories
    )

    st.divider()

    # -----------------------------------------------------
    # SYSTEMIC TREND
    # -----------------------------------------------------

    st.subheader(
        "📈 Systemic Issue Trend"
    )

    if "date" in df.columns:

        trend_df = df.dropna(
            subset=["date"]
        ).copy()

        if not trend_df.empty:

            trend = (
                trend_df
                .set_index("date")
                .resample("ME")
                .size()
            )

            st.line_chart(
                trend
            )

    st.divider()

    # -----------------------------------------------------
    # RAW DATA
    # -----------------------------------------------------

    with st.expander(
        "📋 View Submitted Bug Dataset"
    ):

        st.dataframe(
            df,
            use_container_width=True
        )