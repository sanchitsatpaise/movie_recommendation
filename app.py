import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🎬 Movie Recommendation System",
    page_icon="🎥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main { background-color: #0f1117; }
h1,h2,h3 { color: white; }
.movie-box {
    background: #1c1e26;
    padding: 15px 20px;
    border-radius: 12px;
    margin-bottom: 12px;
    font-size: 18px;
    font-weight: 600;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_df = pd.DataFrame(movies)

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    index = movies_df[movies_df["title"] == movie].index[0]
    distances = similarity[index]

    recommended_movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies_df.iloc[i[0]].title for i in recommended_movies]

# ---------------- UI ----------------
st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Content-Based Recommendation</h3>", unsafe_allow_html=True)
st.markdown("---")

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movies_df["title"].values
)

if st.button("✨ Recommend Movies"):
    recommendations = recommend(selected_movie)

    st.markdown("## 🔥 Recommended Movies")
    for movie in recommendations:
        st.markdown(f"<div class='movie-box'>🎬 {movie}</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Streamlit | Simple & Robust</p>",
    unsafe_allow_html=True
)
