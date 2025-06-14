import streamlit as st
import pandas as pd
import os
from sentiment_utils import predict_sentiments
from preprocess import clean_text
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Insights Inside",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# --- Styles ---
st.markdown(
    """
    <style>
    body { background-color: #181818; }
    .stApp { background-color: #181818; color: #f3f3f3; }
    .css-ffhzg2 { background: #232526; }
    .st-c5, .st-dg, .st-c6 { background: #232526; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Centered Title & Subtitle ----
st.markdown(
    """
    <h1 style='text-align: center; color: #00e676; font-size: 3rem; margin-bottom: 0.5em;'>
        🧠 Insights Inside
    </h1>
    <h3 style='text-align: center; color: #fff; font-weight: 400;'>
        Product Review Sentiment Analysis Tool
    </h3>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='margin-bottom: 24px; font-size:18px; text-align: center;'>
        Upload your product review dataset (<b>CSV, XLSX, or TXT</b>), or enter a single review below.
        <br>
        The app will predict sentiment (<b>Positive/Negative/Neutral</b>) and visualize insights!
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Prediction for single review ---
st.header("Single Review Sentiment")
user_input = st.text_area("Type or paste a product review here:", height=80)
if st.button("Analyze Review", use_container_width=True):
    if not user_input.strip():
        st.warning("Please enter some review text.")
    else:
        pred = predict_sentiments([user_input])[0]
        st.markdown(f"<h3 style='color:#00e676'>Prediction: <span>{pred.capitalize()}</span></h3>", unsafe_allow_html=True)

# --- File upload for batch ---
st.header("Bulk Prediction from File")
uploaded_file = st.file_uploader(
    "Upload a CSV, Excel (.xlsx), or TXT file containing product reviews:",
    type=["csv", "xlsx", "txt"],
    key="file_uploader"
)

if uploaded_file is not None:
    # Try to read as CSV, Excel, or TXT
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(uploaded_file)
    elif ext == ".xlsx":
        df = pd.read_excel(uploaded_file)
    elif ext == ".txt":
        df = pd.DataFrame({"review": uploaded_file.read().decode("utf-8").splitlines()})
    else:
        st.error("Unsupported file format.")
        df = None

    if df is not None:
        st.write("**Data Preview:**")
        st.dataframe(df.head())

        # Try to guess text columns
        review_cols = [col for col in df.columns if "review" in col.lower() or "summary" in col.lower() or "text" in col.lower()]
        if not review_cols:
            st.warning("No obvious review/text column found. Please select the column below:")
            review_cols = list(df.columns)
        selected_col = st.selectbox("Select the column to analyze:", review_cols)

        if st.button("Run Sentiment Analysis", use_container_width=True):
            st.info("Analyzing... Please wait.")
            reviews = df[selected_col].astype(str).tolist()
            sentiments = predict_sentiments(reviews)
            df["Predicted_Sentiment"] = sentiments

            # Show sentiment counts
            sentiment_counts = df["Predicted_Sentiment"].value_counts().reindex(
                ["Positive", "Negative", "Neutral"], fill_value=0
            )
            st.subheader("Sentiment Distribution")
            fig, ax = plt.subplots()
            ax.pie(
                sentiment_counts,
                labels=sentiment_counts.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=["#2ec4b6", "#ff3a20", "#ffd166"],
                textprops={'color':'#222'}
            )
            ax.axis("equal")
            st.pyplot(fig)

            # Show word clouds per sentiment
            st.subheader("Word Clouds by Sentiment")
            col1, col2, col3 = st.columns(3)
            for sent, c in zip(["Positive", "Negative", "Neutral"], [col1, col2, col3]):
                text = " ".join(
                    df.loc[df["Predicted_Sentiment"] == sent, selected_col].dropna().astype(str)
                )
                if len(text) > 0:
                    wc = WordCloud(width=350, height=200, background_color="#232526", colormap="Set2").generate(text)
                    c.image(wc.to_array(), caption=f"{sent}", use_column_width=True)
                else:
                    c.write(f"No {sent.lower()} reviews found.")

            # Show top reviews
            st.subheader("Sample Reviews by Sentiment")
            for sent in ["Positive", "Negative", "Neutral"]:
                st.markdown(f"**{sent} Reviews:**")
                samples = df[df["Predicted_Sentiment"] == sent][selected_col].dropna().astype(str).head(3)
                if not samples.empty:
                    for idx, sample in enumerate(samples, 1):
                        st.write(f"{idx}. {sample}")
                else:
                    st.write(f"No {sent.lower()} reviews found.")

            # Download result
            st.markdown("### Download Results")
            out_csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download CSV with Sentiments",
                data=out_csv,
                file_name="predicted_reviews.csv",
                mime="text/csv",
            )

# --- Footer ---
st.markdown(
    """
    <hr>
    <div style='text-align:center; font-size:14px'>
        <b>Insights Inside</b> | Product Review Sentiment Analysis Tool<br>
        Built with ❤️ by Ashish Ranjan
    </div>
    """,
    unsafe_allow_html=True,
)
