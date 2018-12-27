class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (ing): THe duration of the song in seconds. may be zero
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): A artist object representing the song's creator.
            duration (Optional(int)): initial value for the 'duration' attribute.
                will default to zero if specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song.__init__)
# print(Song.__init__.__doc__)

class Album:
    """" Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist: (Artist): The artist responsible for the album.
            if not specified the artist will default to an artist with the name
            "Various Artists".
        tracks (list(Song)): A list of the song on the album.

    Methods:
        add_song: Used to add a new song to the album's tracklist
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song(Song): a song to add.
            position(Optional(int)): if specified, the song wil lbe added to that position
                in the tracklist - inserted it between other song if necessar.
                otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (list(Album)): A list of the album by this artist.
            The list inculudes only those albums in this collection, if is
            not an exhaustive list of the artist's polished album.

    Methods:
        add_album: to add a new album tho the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a album to the list

        Args:
              album (Album): Album object to add to the list.
                If the album is already present it will not be added again (although this is yet to implemented).
        """
        self.albums.append(album)
