import fresh_tomatoes
import media

lion_king = media.Movie("Lion King",
                        "The story of a lion cub's journey to adulthood and acceptance of his royal destiny.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=V6jOvVf05aQ")
five_hundred_days_of_summer = media.Movie("500 Days of Summer",
                                 "An offbeat romantic comedy about a woman who doesn't believe true love exists, and the young man who falls for her.",
                                 "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
                                 "https://www.youtube.com/watch?v=PsD0NpFSADM")
                                 
ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "A high school wise guy is determined to have a day off from school, despite what the Principal thinks of that.",
                             "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
                             "https://www.youtube.com/watch?v=D6gABQFR94U")

spirited_away = media.Movie("Spirited Away",
                            "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

movies = [lion_king, five_hundred_days_of_summer, ferris_bueller, spirited_away]
fresh_tomatoes.open_movies_page(movies)
