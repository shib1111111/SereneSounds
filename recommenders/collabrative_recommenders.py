import pickle
from poster_maker import get_song_album_cover_url
from music import music

def recommend_song(user_song_name,song_data):
    # Sort song_data by popularity, time_signature, and other relevant features
    sorted_song_data = song_data.sort_values(by=['popularity', 'time_signature', 'duration_ms', 'explicit'], ascending=[False, True, True, False])

    # Filter song_data similar to the user's song
    user_song = song_data[song_data['name'].str.lower() == user_song_name.lower()]

    if user_song.empty:
        return ["Sorry, the provided song name is not in the dataset."]

    user_song_signature = user_song['time_signature'].values[0]
    user_song_duration = user_song['duration_ms'].values[0]
    user_song_explicit = user_song['explicit'].values[0]

    # Filter song_data with similar time_signature, higher popularity, similar duration, and opposite explicit value
    recommended_songs = sorted_song_data[
        (sorted_song_data['time_signature'] == user_song_signature) &
        (sorted_song_data['popularity'] > user_song['popularity'].values[0]) &
        (abs(sorted_song_data['duration_ms'] - user_song_duration) < sorted_song_data['duration_ms'].median()) &  
        (sorted_song_data['explicit'] != user_song_explicit)
    ]

    # Exclude redundant and same-name songs
    recommended_songs = recommended_songs[recommended_songs['name'].str.lower() != user_song_name.lower()]
    if not recommended_songs.empty:
        unique_recommended_song_names = set(recommended_songs['name'].head(1000).tolist())
        return list(unique_recommended_song_names)[:10]
    else:
        return ["Sorry, no similar songs found with higher popularity."]


# Recommendation System
def collabrative_recommend(song_title, song_data=music):
    recommended_songs = recommend_song(song_title,song_data)
    # Create a list of dictionaries with music link and poster
    collabrative_recommendations = []
    for recommended_song in recommended_songs:
        index = music[music['name'] == recommended_song].index[0]
        link = music.iloc[index].link
        poster = get_song_album_cover_url(recommended_song)
        
        collabrative_recommendations.append({
            'name': recommended_song,
            'link': link,
            'poster': poster
        })

    return collabrative_recommendations
