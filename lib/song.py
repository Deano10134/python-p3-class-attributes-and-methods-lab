class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    def play(self):
        return f"Playing '{self.name}' by {self.artist}."
    
    def __str__(self):
        return f"'{self.name}' by {self.artist}, Genre: {self.genre}"



