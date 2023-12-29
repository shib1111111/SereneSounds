import pickle
from poster_maker import get_song_album_cover_url
from music import music


# Loading data
lyrics_similarity = pickle.load(open('./data/lyrics_similarity.pkl', 'rb'))




# Recommendation System
def lyrics_similarity_based_recommend(song_title, cosine_sim=lyrics_similarity):
    idx = music[music['name'] == song_title].index[0]
    sim_scores = sorted(enumerate(cosine_sim[idx]), key=lambda x: x[1], reverse=True)
    
    # Filter out songs with the same name as the input song
    sim_scores = [(i, score) for i, score in sim_scores if music['name'].iloc[i] != song_title]
    
    # Getting the top 10 most similar songs
    sim_scores = sim_scores[:10]
    
    # Get the indices and names of the recommended songs
    song_indices = [i[0] for i in sim_scores]
    recommended_songs = list(set(music['name'].iloc[song_indices]))
    
    # Create a list of dictionaries with music link and poster
    lyrics_similarity_based_recommendations = []
    for recommended_song in recommended_songs:
        index = music[music['name'] == recommended_song].index[0]
        link = music.iloc[index].link
        poster = get_song_album_cover_url(recommended_song)
        
        lyrics_similarity_based_recommendations.append({
            'name': recommended_song,
            'link': link,
            'poster': poster
        })

    return lyrics_similarity_based_recommendations
