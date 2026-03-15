import streamlit as st
import pickle
import pandas as pd
import bz2


# --- 1. DATA LOADING (Optimized) ---
@st.cache_resource
def load_data():
    with bz2.BZ2File('similarity_sparse.pbz2', 'rb') as f:
        similarity_indices = pickle.load(f)
    with bz2.BZ2File('movie_dict.pbz2', 'rb') as f:
        movies_dict = pickle.load(f)
    movies = pd.DataFrame(movies_dict)
    return similarity_indices, movies

similarity_indices, movies = load_data()


# Initialize data
try:
    similarity, movies = load_data()
except FileNotFoundError:
    st.error("Compressed files not found! Please run the compression script first.")
    st.stop()


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    # We already stored the best indices, so just grab the first 5 (excluding itself)
    # The first index [0] is usually the movie itself, so we take [1:6]
    top_indices = similarity_indices[movie_index][1:6]

    return [movies.iloc[i].title for i in top_indices]


# --- 3. UI & STYLING ---
st.set_page_config(page_title="CinemaPulse", page_icon="🍿", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
    .main-header { text-align: center; padding: 20px; }
    .movie-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: all 0.4s ease;
    }
    .movie-card:hover {
        transform: scale(1.05);
        border: 1px solid #00d2ff;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.5);
    }
    .movie-title { color: white; font-weight: bold; margin: 0; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>🍿 CinemaPulse</h1>
        <p style='color: #00d2ff; font-size: 1.2rem;'>AI-Powered Movie Discovery & Recommendation Engine</p>
    </div>
    """, unsafe_allow_html=True)

# Centered Dropdown and Button
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    selected_movie_name = st.selectbox(
        "Which movie did you enjoy watching?",
        movies['title'].values
    )

    # Center the button
    b_col1, b_col2, b_col3 = st.columns([1, 1, 1])
    with b_col2:
        btn = st.button("Generate Picks")

# --- 4. OUTPUT ---
if btn:
    recommendations = recommend(selected_movie_name)
    st.write("##")

    cols = st.columns(5)
    for idx, movie_title in enumerate(recommendations):
        with cols[idx]:
            st.markdown(f"""
                <div class="movie-card">
                    <div style="font-size: 20px; margin-bottom: 10px;">🎬</div>
                    <p class="movie-title">{movie_title}</p>
                </div>
                """, unsafe_allow_html=True)
