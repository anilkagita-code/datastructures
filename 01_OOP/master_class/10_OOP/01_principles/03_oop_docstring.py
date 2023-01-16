class Song:
    """Class represents the song

    Attributes: this are teh attributes
        title:
        artist:
        duration:
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method
        :param title: Initiates the title
        :param artist: song creator
        :param duration: duration of song
        :return:
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent the Album using its track list

    Attributes:
        name (str):
        year (int):
        artist:
        tracks(List[Song])

    Methods:
        addSong: Used to add a new song
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song: Song, position: None):
        """Adds a song to the track list

        Args:
            song(Song):
            position (Optional):
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store Artist

    Attributes:
        name (str): The name of the artist
        albums (List[Albums]): A list of albums

    Methods:
        add_album: User to add a new album to the artist's album list
    """
    def __int__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album(Album)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data consists of (artist, album, year, song) as tuple
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field:35}, {album_field:50}, {year_field:5}, {song_field:20}")


if __name__ == '__main__':
    load_data()

help(Song)
print('********** Help Init **************')
help(Song.__init__)

print('********** Print Init **************')

print(Song.__init__)
print('********** Doc **************')
print(Song.__doc__)

print('********** Init.Doc **************')
print(Song.__init__.__doc__)
