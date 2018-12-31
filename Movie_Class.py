import fresh_tomatoes2
Movies_list = []


class Movie:
	"""this class contains all Movie data needed like trailer, Movie title,
	poster ....."""
	def __init__(self, title, poster_image_url, trailer_youtube_id):
		"""the init function is the first called function in class"""
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_id

# godfather Movie : movie title , storyline , poster image and movie trailer
example_godfather = Movie(
	'The GodFather',
	'http://static.metacritic.com/images/products/movies/3/47c2b1f35087fc23c5ce261bbc3ad9e0.jpg',  # NOQA
	'https://www.youtube.com/watch?v=sY1S34973zA')

# Shawshanek Movie: movie title , storyline , poster image and movie trailer
example_shawshank = Movie(
	'Shawshank redemption',
	'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',  # NOQA
	'https://www.youtube.com/watch?v=NmzuHjWmXOc')

# green mile Movie: movie title , storyline , poster image and movie trailer
example_greenmile = Movie(
	'The Green Mile',
	'http://t3.gstatic.com/images?q=tbn:ANd9GcRzAo286udsv_uTTpuBmSc3_h-nlUaWHYcUYG6VMAhhPcSDLJF7',  # NOQA
	'https://www.youtube.com/watch?v=Ki4haFrqSrw')

# Avengers Movie : movie title , storyline , poster image and movie trailer
example_avengers = Movie(
	'Avengers:infinity war',
	'http://wegotthiscovered.com/wp-content/uploads/2017/09/avengers__infinity_war__2018__poster_by_midiya42-dbihe3f.jpg',  # NOQA
	'https://www.youtube.com/watch?v=6ZfuNTqbHE8')

# Forrest Gump Movie : movie title , storyline , poster image and movie trailer
example_forrest = Movie(
	'Forrest Gump',
	'https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg',  # NOQA
	'https://www.youtube.com/watch?v=uPIEn0M8su0')

# Pulp Fiction Movie : movie title , storyline , poster image and movie trailer
example_pulp = Movie(
	'Pulp Fiction',
	'http://is5.mzstatic.com/image/thumb/Video3/v4/b7/30/8b/b7308b8f-d9ce-41fc-928a-76a87de7d966/source/1200x630bb.jpg',  # NOQA
	'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

# Set the movies that will be passed to the media file
Movies_list = [
	example_godfather,
	example_shawshank,
	example_greenmile,
	example_avengers,
	example_forrest,
	example_pulp
	]

# Calling media method from media file
fresh_tomatoes2.open_movies_page(Movies_list)