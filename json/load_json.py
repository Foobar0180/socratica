import json

json_file = open("movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie)
print(type(movie))

json.dumps(movie, ensure_ascii=False)
