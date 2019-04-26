import webbrowser


# 1 follow the comments numbers for this one 
# 3 you will need to import your webbrowser to go with your default browser directly, but the actual behavior may depend on your browsers settings
# 4 if you want your browser to open a new window instead of a tab you may change webbrowser.open to webbrowser.open_new 



# init works as a reserve to create space and memory to remember the list details.
# init will work by initialize pieces of information for the list below in our class.
# but to specifiy how to make it initialize (for example) self.title (we add = to specifiy that the title is for movie title) = movie title
class Movie():
     def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_youtube

     def show_trailer(self):
     	webbrowser.open(self.trailer_youtube_url)
# 2 this function webbrowser is a method to open the link provided here which will will be recieved thru self.trailer_youtube_url
# 3 when it recieve the necessary it'll open the webbrowser (But wait ! )
