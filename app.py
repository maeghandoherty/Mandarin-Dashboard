import streamlit as st
import pandas as pd
import random

# Load HSK files
hsk1 = pd.read_csv("data/New-HSK-1-Word-List.csv")
hsk2 = pd.read_csv("data/New-HSK-2-Word-List.csv")
hsk3 = pd.read_csv("data/New-HSK-3-Word-List.csv")
hsk4 = pd.read_csv("data/New-HSK-4-Word-List.csv")
hsk5 = pd.read_csv("data/New-HSK-5-Word-List.csv")
hsk6 = pd.read_csv("data/New-HSK-6-Word-List.csv")


# Add level labels
hsk1["level"] = "HSK 1"
hsk2["level"] = "HSK 2"
hsk3["level"] = "HSK 3"
hsk4["level"] = "HSK 4"
hsk5["level"] = "HSK 5"
hsk6["level"] = "HSK 6"


# Combine all vocabulary
vocab = pd.concat(
    [hsk1, hsk2, hsk3, hsk4, hsk5, hsk6],
    ignore_index=True
)


# Sidebar
st.sidebar.title("📚 Study Settings")

levels = st.sidebar.multiselect(
    "Choose HSK levels",
    options=[
        "HSK 1",
        "HSK 2",
        "HSK 3",
        "HSK 4",
        "HSK 5",
        "HSK 6"
    ],
    default=[
        "HSK 1",
        "HSK 2"
    ]
)


# Filter vocabulary  ← THIS MUST COME BEFORE USING filtered_vocab
filtered_vocab = vocab[
    vocab["level"].isin(levels)
]
st.divider()

#Flashcards
st.header("🃏 Flashcards")

if len(filtered_vocab) > 0:

    card = filtered_vocab.sample(1).iloc[0]

    st.subheader(card["Chinese"])

if st.button("Show Answer"):

    st.write(card["Pingyin"])
    st.write(card["English"])   

 if st.button("Again"):
    st.warning("Review this word more often")

if st.button("Good"):
    st.success("Nice!")

# Display
st.title("📚 Mandarin Dashboard")

st.write(
    f"You have {len(filtered_vocab)} words available"
)

st.dataframe(filtered_vocab)
#website columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cards Due", 24)

with col2:
    st.metric("Current Streak", "8 days")

with col3:
    st.metric("Words Learned", 156)

st.divider()

if st.button("🃏 Start Studying"):
    st.success("Study mode coming soon!")