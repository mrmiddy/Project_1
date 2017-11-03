import webbrowser

class Movie():
    """This class provides a way to store movie related information
        Attributes:
            movie_title: a string that contains the movie title.
            movie_storyline: a string that contains the movie's storyline.
            poster_image: a string that contains the movie's poster image URL.
            trailer_youtube: a string that contains the movie's YouTube trailer
            URL."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Inits Movie Class with the movie's title, storyline,
           poster image URL, and YouTube URL."""
        """The storyline is not currently used on the website,
           but is for future use."""
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
