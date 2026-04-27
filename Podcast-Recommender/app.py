import streamlit as st
from model import recommend, data

st.set_page_config(page_title="Podcast Recommender", layout="wide")

# 🌌 Custom CSS (NEON THEME)
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

/* Title glow */
.title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
    text-shadow: 0 0 20px #38bdf8, 0 0 40px #0ea5e9;
}

/* Card style */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
    transition: 0.3s;
}

/* Hover effect */
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.8);
}

/* Button glow */
.stButton>button {
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    box-shadow: 0 0 15px #0ea5e9;
}

.stButton>button:hover {
    box-shadow: 0 0 25px #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# 🌟 Title
st.markdown('<div class="title">🎧 Podcast Recommendation System</div>', unsafe_allow_html=True)

st.write("")

# 🎯 Dropdown
podcast_list = data['title'].values
selected = st.selectbox("Choose a podcast", podcast_list)

# 🚀 Button
if st.button("✨ Get Recommendations"):
    results = recommend(selected)

    st.write("## 🔥 Recommended Podcasts")

    for r in results:
        st.markdown(f'<div class="card">🎙️ {r}</div>', unsafe_allow_html=True)