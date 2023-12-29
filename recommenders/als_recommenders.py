import pickle
from poster_maker import get_song_album_cover_url
from music import music


# Loading data
als_similarity = pickle.load(open('./data/als_model.pkl', 'rb'))


def get_recommendations(track_name, model, song_data, num_recommendations=100000):
    track_index = song_data[song_data['name'] == track_name].index[0]
    user_vector = model.user_factors[track_index]

    # Calculate the dot product between the user vector and item factors
    scores = user_vector.dot(model.item_factors.T)

    # Get track indices with highest scores
    recommended_track_indices = scores.argsort()[-num_recommendations * 2:][::-1]

    # Filter out redundant and same-name tracks
    recommendations = []
    seen_names = set()
    for idx in recommended_track_indices:
        if len(recommendations) >= num_recommendations:
            break
        recommended_track_name = song_data.loc[idx, 'name']
        if recommended_track_name not in seen_names and recommended_track_name != track_name:
            recommendations.append(recommended_track_name)
            seen_names.add(recommended_track_name)

    return recommendations[:num_recommendations][::-1]

# Recommendation System
def als_similarity_based_recommend(song_title,model=als_similarity, song_data=music):
    recommended_songs = get_recommendations(song_title,model,song_data)
    # Create a list of dictionaries with music link and poster
    als_similarity_based_recommendations = []
    for recommended_song in recommended_songs:
        index = music[music['name'] == recommended_song].index[0]
        link = music.iloc[index].link
        poster = get_song_album_cover_url(recommended_song)
        
        als_similarity_based_recommendations.append({
            'name': recommended_song,
            'link': link,
            'poster': poster
        })

    return als_similarity_based_recommendations
