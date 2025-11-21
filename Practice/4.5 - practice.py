osowskis_favs = {
    "video_game": "Elden Ring",
    "food": "Eggs Bennedict",
    "color": "Black",
    "city": "Park City",
    "class": "Intro to Programming",
}

print(osowskis_favs["food"])

#Add a new entry
osowskis_favs["pokemon"] = "Hawlucha"

#Modify an entry
osowskis_favs["color"] = "Yellow"

#Remove an entry
osowskis_favs.pop("city")

#Looping through a dictionary
'''for key, value in osowskis_favs:
    print(f"{key}: {str(value)}")'''


print("---------")

print(osowskis_favs.keys())
print(osowskis_favs.values())
print(osowskis_favs.items())
osowskis_favs.clear()
print(osowskis_favs)


