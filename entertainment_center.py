from media import Movie
from fresh_tomatoes import open_movies_page

"""This program compiles a list of movies, then executes a command to create a
    a website with poster image and trailers."""

space_is_the_place = Movie("Space is the Place",
        "https://www.residentadvisor.net/images/events/flyer/2013/7/de-0720-496345-front.jpg",  # NOQA
        "https://www.youtube.com/watch?v=4sOIs1u8iwg&t=1s")

europa_report = Movie("Europa Report",
        "http://www.slate.com/content/dam/slate/blogs/bad_astronomy/2013/05/20/Europa-Report-poster.jpg.CROP.original-original.jpg",  # NOQA
        "https://www.youtube.com/watch?v=w2BfobyYOmU")

alien = Movie("Alien",
        "https://secure.i.telegraph.co.uk/multimedia/archive/03064/Alien-intro_3064438b.jpg",  # NOQA
        "https://www.youtube.com/watch?v=LjLamj-b0I8")

blade_runner = Movie("Blade Runner",
        "https://images-na.ssl-images-amazon.com/images/I/51ZmDpb2QfL.jpg",  # NOQA
        "https://www.youtube.com/watch?v=eogpIG53Cis")

moon = Movie("Moon",
        "https://static.rogerebert.com/uploads/movie/movie_poster/moon-2009/large_uXvYBgbuJhySVqshcgrfeqQkK7y.jpg",  # NOQA
        "https://www.youtube.com/watch?v=twuScTcDP_Q")

event_horizon = Movie("Event Horizon",
        "http://img.moviepostershop.com/event-horizon-movie-poster-1997-1020255488.jpg",  # NOQA
        "https://www.youtube.com/watch?v=OVlnER8SxfQ")

movies_list = [space_is_the_place, europa_report, alien, blade_runner,
               moon, event_horizon]

open_movies_page(movies_list)
