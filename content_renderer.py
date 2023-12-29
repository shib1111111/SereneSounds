import streamlit as st
from recommenders.lyrics_similarity_recommenders import lyrics_similarity_based_recommend
from recommenders.musical_similarity_recommenders import musical_feature_similarity_based_recommend
from recommenders.collabrative_recommenders import collabrative_recommend
from recommenders.artists_similarity_recommenders import artists_similarity_based_recommend
from recommenders.als_recommenders import als_similarity_based_recommend

# Set up the Streamlit app
def setup_app():
    st.markdown("<H1 class='big-title'>SereneSounds</H1>", unsafe_allow_html=True)
    st.markdown("<h3 class='small-subtitle'>A Sophisticated Music Curation Engine</h3>", unsafe_allow_html=True)


# Display dropdown for song selection
def display_song_dropdown_list(music_list):
    selected_song = st.selectbox(
        "Type or select a song from the dropdown",
        music_list
    )
    return selected_song

# Display Recommendations
def show_recommendations(selected_song):
    if st.button('Show Recommendation'):
        display_lyrics_similarity_based_recommendations(selected_song)
        display_musical_feature_similarity_based_recommendations(selected_song)
        display_collabrative_feature_based_recommendations(selected_song)
        display_artists_similarity_based_recommendations(selected_song)
        display_als_similarity_based_recommendations(selected_song)
        # add more same fuctions


# Display recommendations based on lyrics_similarity
def display_lyrics_similarity_based_recommendations(selected_song):
    recommendations = lyrics_similarity_based_recommend(selected_song)
    st.markdown(
            """
            <div style="border: 2px solid #e74c3c; padding: 5px; border-radius: 10px; margin: 5px 0;">
                <h3 style="color: #e74c3c;">Lyrical Similarity Based Recommendated Songs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # Display recommendations in cards
    for i in range(0, len(recommendations), 5):
        row = st.columns(5)
        for j in range(min(5, len(recommendations) - i)):
            with row[j]:
                st.write(f"{recommendations[i + j]['name']}")
                st.image(recommendations[i + j]['poster'], use_column_width=True)
                st.write(f"[Listen on]({recommendations[i + j]['link']})")


# Display recommendations based on musical_feature_similarity
def display_musical_feature_similarity_based_recommendations(selected_song):
    recommendations = musical_feature_similarity_based_recommend(selected_song)
    st.markdown(
            """
            <div style="border: 2px solid #e74c3c; padding: 5px; border-radius: 10px; margin: 5px 0;">
                <h3 style="color: #e74c3c;">Musical Feature Similarity Based Recommendated Songs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # Display recommendations in cards
    for i in range(0, len(recommendations), 5):
        row = st.columns(5)
        for j in range(min(5, len(recommendations) - i)):
            with row[j]:
                st.write(f"{recommendations[i + j]['name']}")
                st.image(recommendations[i + j]['poster'], use_column_width=True)
                st.write(f"[Listen on]({recommendations[i + j]['link']})")


# Display recommendations based on collabrative_feature_similarity
def display_collabrative_feature_based_recommendations(selected_song):
    recommendations = collabrative_recommend(selected_song)
    st.markdown(
            """
            <div style="border: 2px solid #e74c3c; padding: 5px; border-radius: 10px; margin: 5px 0;">
                <h3 style="color: #e74c3c;">Collabrative Feature Similarity Based Recommendated Songs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # Display recommendations in cards
    for i in range(0, len(recommendations), 5):
        row = st.columns(5)
        for j in range(min(5, len(recommendations) - i)):
            with row[j]:
                st.write(f"{recommendations[i + j]['name']}")
                st.image(recommendations[i + j]['poster'], use_column_width=True)
                st.write(f"[Listen on]({recommendations[i + j]['link']})")


# Display recommendations based on artists_similarity
def display_artists_similarity_based_recommendations(selected_song):
    recommendations = artists_similarity_based_recommend(selected_song)
    st.markdown(
            """
            <div style="border: 2px solid #e74c3c; padding: 5px; border-radius: 10px; margin: 5px 0;">
                <h3 style="color: #e74c3c;">Artists Similarity Based Recommendated Songs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # Display recommendations in cards
    for i in range(0, len(recommendations), 5):
        row = st.columns(5)
        for j in range(min(5, len(recommendations) - i)):
            with row[j]:
                st.write(f"{recommendations[i + j]['name']}")
                st.image(recommendations[i + j]['poster'], use_column_width=True)
                st.write(f"[Listen on]({recommendations[i + j]['link']})")







 # add more same fuctions


# Display recommendations based on als_similarity
def display_als_similarity_based_recommendations(selected_song):
    recommendations = als_similarity_based_recommend(selected_song)
    st.markdown(
            """
            <div style="border: 2px solid #e74c3c; padding: 5px; border-radius: 10px; margin: 5px 0;">
                <h3 style="color: #e74c3c;">Other Recommendated Songs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # Display recommendations in cards
    for i in range(0, len(recommendations), 5):
        row = st.columns(5)
        for j in range(min(5, len(recommendations) - i)):
            with row[j]:
                st.write(f"{recommendations[i + j]['name']}")
                st.image(recommendations[i + j]['poster'], use_column_width=True)
                st.write(f"[Listen on]({recommendations[i + j]['link']})")


# Apply CSS
def apply_css():
    st.markdown(
        """
            <style>
                    .big-title {
                        font-size: 3.5em;
                        font-weight: bold;
                        font-family: 'Times New Roman', Times, serif;
                        font-style: italic;
                        text-align: center;
                    }
                    
                    .small-subtitle {
                        font-size: 1em;
                        margin-top: -15px; 
                        font-family: 'Arial', sans-serif;
                        font-style: italic;
                        text-align: center;
                        margin-bottom: 30px; 
                    }
                    body {
                        background-color: #f0f2f6;
                        font-family: 'Arial', sans-serif;
                    }
                    .stSelectbox {
                        width: 100%;
                        max-width: 1200px;
                        margin-bottom: 20px;
                    }
                    .stButton button, .stTextInput input {{
                        background-color: #2c6db8 !important;
                        border-color: #2c6db8 !important;
                        color: #fff !important;
                    }}
                    .stButton:hover button, .stTextInput:hover input {{
                        background-color: #2c6db8 !important;
                        border-color: #2c6db8 !important;
                        color: #fff !important;
                    }}
                    .stButton:active button {{
                        background-color: #ff4d4d !important;
                        border-color: #ff4d4d !important;
                    }}

                    .stText {{
                        font-size: 18px;
                    }}
                    .stImage {{
                        max-width: 100%;
                        height: auto;
                    }}
            </style>
        """,
        unsafe_allow_html=True
    )
