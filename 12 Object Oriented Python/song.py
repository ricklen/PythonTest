class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (str): An artist name representing the songs creator.
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

    def get_title(self):
        return self.title

    name = property(get_title)


# help(Song.__init__)
# print(Song.__init__.__doc__)

class Album:
    """" Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist: (str): The name of the artist responsible for the album.
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
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (str): The title of a song to add.
            position(Optional(int)): if specified, the song wil lbe added to that position
                in the track list - inserted it between other song if necessary.
                otherwise, the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


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

    def add_song(self, name, year, title):
        """"Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't allready exist.

        Args:
              name (str): The name of the album
              year (int): The year the album was produced
              title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exist,
    return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # Data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artists_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artists_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)
