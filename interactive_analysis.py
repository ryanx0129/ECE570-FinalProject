import streamlit as st
import pandas as pd

def main():
    st.title("Interactive Adversarial Response Analysis")
    df = pd.read_csv("adversarial_test_results.csv")
    
    st.sidebar.header("Filter Options")
    classification_filter = st.sidebar.multiselect("Select Classification", df["Classification"].unique(), default=df["Classification"].unique())
    filtered_df = df[df["Classification"].isin(classification_filter)]

    st.dataframe(filtered_df)

    for index, row in filtered_df.iterrows():
        st.subheader(f"Prompt: {row['Original Prompt']}")
        st.text(f"Response: {row['Response']}")

if __name__ == "__main__":
    main()
