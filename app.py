from music import music
from signature import display_signature
from content_renderer import setup_app,display_song_dropdown_list,show_recommendations,apply_css

# Main function to run the app
def main():
    setup_app()
    music_list = music['name'].values
    selected_song = display_song_dropdown_list(music_list)
    show_recommendations(selected_song)
    apply_css()

    # Adding the signature
    display_signature()

# Run the app
if __name__ == "__main__":
    main()
