import json

movie = {}
movie["title"] = "Minority Report"
movie["director"] = "Steven Spielberg"
movie["composer"] = "John Williams"
movie["actors"] = ["Tom Cruise", "Colin Farrel", 
                   "Samantha Morton", "Max von Sydow"]
movie["won_oscars"] = False
movie["budget"] = 1020000000
movie["cinematographer"] = "Janusz Kami\u0144ski"

json_file = open("movie_2.txt", "w", encoding="utf-8")
json.dump(movie, file, ensure_ascii=False)
json_file.close()
