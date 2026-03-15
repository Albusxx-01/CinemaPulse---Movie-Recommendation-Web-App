import streamlit as st
import pickle
import pandas as pd

# Page setup
st.set_page_config(page_title="CinemaPulse", page_icon="🍿", layout="wide")

# UI Styling including centering logic
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* Center aligning the header section */
    .main-header {
        text-align: center;
        padding: 20px;
    }

    /* Glassmorphism Movie Cards */
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

    .movie-title {
        color: white;
        font-weight: bold;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)


# Helper function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]


# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- CENTERED HEADER SECTION ---
st.markdown("""
    <div class="main-header">
        <h1>🍿 CinemaPulse</h1>
        <p style='color: #00d2ff; font-size: 1.2rem;'>AI-Powered Movie Discovery & Recommendation Engine</p>
    </div>
    """, unsafe_allow_html=True)

# Using columns to center the selectbox and button
# The ratio [1, 2, 1] puts the content in the middle 50% of the screen
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    selected_movie_name = st.selectbox(
        "Which movie did you enjoy watching?",
        movies['title'].values,
        label_visibility="visible"
    )

    # Nested columns for the button to keep it centered within the center column
    b_col1, b_col2, b_col3 = st.columns([1, 1, 1])
    with b_col2:
        btn = st.button("Generate Picks")

# --- OUTPUT SECTION ---
if btn:
    recommendations = recommend(selected_movie_name)
    st.write("##")

    cols = st.columns(5)
    for idx, movie_title in enumerate(recommendations):
        with cols[idx]:
            st.markdown(f"""
                <div class="movie-card">
                    <div style="font-size: 20px;">🎬</div>
                    <p class="movie-title">{movie_title}</p>
                </div>
                """, unsafe_allow_html=True)