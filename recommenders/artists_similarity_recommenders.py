import pickle
from poster_maker import get_song_album_cover_url
from music import music


# Loading data
artists_similarity = pickle.load(open('./data/graph_data.pkl', 'rb'))


def recommend_songs(input_song_name, graph,song_data, num_recommendations=15):
    # Find the artist(s) for the input song
    input_song_artist = song_data[song_data['name'] == input_song_name]['artists'].iloc[0]

    # Find similar artists based on the network
    similar_artists = []
    for artist in input_song_artist:
        similar_artists.extend([neighbor for neighbor, _ in graph[artist].items()])

    # Remove input song artist(s) from the list
    similar_artists = list(set(similar_artists) - set(input_song_artist))

    # Get songs by similar artists
    recommendations = song_data[song_data['artists'].apply(lambda x: any(artist in x for artist in similar_artists))]

    # Exclude input song from recommendations
    recommendations = recommendations[recommendations['name'] != input_song_name]

    # Sort by popularity and select top recommendations
    recommendations = recommendations.sort_values(by='popularity', ascending=False).head(num_recommendations)

    # Use set to uniquify the list of song names
    unique_recommendations = set(recommendations['name'])

    # Convert set to list before returning
    return list(unique_recommendations)

# Recommendation System
def artists_similarity_based_recommend(song_title,graph=artists_similarity, song_data=music):
    recommended_songs = recommend_songs(song_title,graph,song_data)
    # Create a list of dictionaries with music link and poster
    artists_similarity_based_recommendations = []
    for recommended_song in recommended_songs:
        index = music[music['name'] == recommended_song].index[0]
        link = music.iloc[index].link
        poster = get_song_album_cover_url(recommended_song)
        
        artists_similarity_based_recommendations.append({
            'name': recommended_song,
            'link': link,
            'poster': poster
        })

    return artists_similarity_based_recommendations
