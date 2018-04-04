

class Movie():
    """Creates a Movie object with attribute title, poster image, and
    YT trailer.

    Attributes:
        title: Title of movie
        poster_image_url: link to poster image
        trailer_youtube_url: link to trailer on YT"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
