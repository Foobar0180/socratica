import json

value = """{
    "title" : "Tron Legacy",
    "release_year" : 2010,
    "budget" : 170000000,
    "won_oscars" : false,
    "actors" : null
}"""

tron = json.loads(value)

print(tron)
