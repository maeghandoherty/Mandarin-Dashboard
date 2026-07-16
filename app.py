import streamlit as st
import pandas as pd
import random

if "current_card" not in st.session_state:
    st.session_state.current_card = None

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

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
st.markdown(
    """
    <style>

    .flashcard {
        background-color: white;
        border-radius: 20px;
        padding: 50px;
        text-align: center;
        border: 2px solid #dddddd;
        margin: 20px 0;
    }

    .flashcard h1 {
        font-size: 60px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
#flashcards
st.header("🃏 Flashcards")

if len(filtered_vocab) > 0:

    if st.session_state.current_card is None:
    st.session_state.current_card = filtered_vocab.sample(1).iloc[0]

    card = st.session_state.current_card

    st.markdown(
    f"""
    <div class="flashcard">
        <h1>{card["Chinese"]}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

    if st.button("Show Answer"):

    st.markdown(
        f"""
        <div class="flashcard">
            <h1>{card["Chinese"]}</h1>
            <h2>{card["Pinyin"]}</h2>
            <p>{card["English"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("Again"):
        st.warning("Review this word again")

    if st.button("Good"):
        st.success("Nice work!")
        
    if st.button("➡️ Next Card"):

    st.session_state.current_card = filtered_vocab.sample(1).iloc[0]
    st.session_state.show_answer = False
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