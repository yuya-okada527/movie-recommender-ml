import dataclasses


@dataclasses.dataclass
class Movie:
    movie_id: str
    tmdb_id: str
    overview: str
