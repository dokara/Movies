import fresh_tomatoes
import media

# 3 import fresh_tomatoes will import the HTML/css code that will be used to
# stylize our webbrowser BUT!
# 4 import fresh_tomatoes simply will import the needed information ,
# fresh_tomatoes.open_movies_page(movies) is the actual function that will OPEN
# the browser and run the code

# This contain all movies
avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"
)


a_silent_voice = media.Movie("A silent voice",
	                         "Shōya Ishida sets his affairs in order and walks to a bridge, intending to commit suicide. Coming to his senses at the last minute, he hears fireworks as he recalls his days in elementary school and the events that have led him to this point in his life.",
	                         "http://t1.gstatic.com/images?q=tbn:ANd9GcS8UCCpFFEMlwHJs0iJGAdLG5FCVh07rzox9pU3Sw6OBE4Qxs5u",
	                         "https://www.youtube.com/watch?v=nfK6UgLra7g")

my_neighbor_totoro = media.Movie("My neighbor totoro",
	                         "In 1958 Japan, university professor Tatsuo Kusakabe and his two daughters, Satsuki and Mei, move into an old house to be closer to the hospital where the girls' mother, Yasuko, is recovering from a long-term illness. Satsuki and Mei find that the house is inhabited by tiny creatures called susuwatari—small, dark, dust-like house spirits seen when moving from light to dark places.[note 1] When the girls become comfortable in their new house and laugh with Tatsuo, the soot spirits leave the house to drift away on the wind and find another empty house.",
	                         "https://images-na.ssl-images-amazon.com/images/I/91DoU3%2BT-6L._SL1500_.jpg",
	                         "https://www.youtube.com/watch?v=92a7Hj0ijLs")


grave_of_the_fireflies = media.Movie("Grave of the Fireflies",
	                         "On September 21, 1945, shortly after the end of World War II, a teenage boy, Seita, dies of starvation in a Kobe train station. A janitor sorts through his possessions and finds a candy tin, which he throws into a field. The spirit of Seita's younger sister, Setsuko, springs from the tin and is joined by Seita's spirit and a cloud of fireflies. They board a train.",
	                         "https://vignette.wikia.nocookie.net/studio-ghibli/images/4/4c/Ghibli_grave_of_the_fireflies_film_poster.jpg/revision/latest?cb=20171214173909",
	                         "https://www.youtube.com/watch?v=4vPeTSRd580")


spirited_away = media.Movie("Spirited Away",
	                         "Ten-year-old Chihiro Ogino and her parents are traveling to their new home when her father takes a wrong turn. They unknowingly enter a magical world that Chihiro's father insists on exploring. While Chihiro's parents begin to devour the food at an empty restaurant stall, Chihiro finds an exquisite bathhouse and meets a young boy named Haku who warns her to return across the river before sunset. However, Chihiro discovers too late that her parents have turned into pigs and she is unable to cross the flooded river, becoming trapped in the spirit world.",
	                         "https://qvcinema.com.au/wp-content/uploads/2018/01/spirited-away-poster-8d1d74e77422295ed279ea54f454d84b-560x829.jpg",
	                         "https://www.youtube.com/watch?v=ByXuk9QqQkk")


howls_moving_castle = media.Movie("Howls Moving Castle",
	                         "Sophie, a young milliner, encounters a wizard named Howl on her way to visit her sister Lettie. Upon returning home, she meets the Witch of the Waste, who transforms her into a ninety-year-old woman. Seeking to break the curse, Sophie leaves home and sets off through the countryside; she meets a living scarecrow, whom she decides to call 'Turnip Head'. He leads her to Howl's moving castle, where she meets Howl's young apprentice Markl, and the fire-demon Calcifer, who is the source of the castle's magic. When Howl appears, Sophie announces that she has hired herself as a cleaning lady.",
	                         "https://vignette.wikia.nocookie.net/studio-ghibli/images/d/dc/Howl%27s_Moving_Castle_Poster.jpeg/revision/latest?cb=20180108143752",
	                         "https://www.youtube.com/watch?v=iwROgK94zcM")


# 2 so we defined movies with a list of our movies listed above
movies = [avatar, a_silent_voice, my_neighbor_totoro, grave_of_the_fireflies, spirited_away, howls_moving_castle]
fresh_tomatoes.open_movies_page(movies)
# 1 thru this we made freshtomatoes open a movie page with our movies 
# (follow comments numbers)
