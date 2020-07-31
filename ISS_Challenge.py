astro= {"message": "success", "number": 5, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}, {"craft": "ISS", "name": "Doug Hurley"}, {"craft": "ISS", "name": "Bob Behnken"}]}

x = "People in space:"
(astro["number"])
print(x, (astro["number"]))
y = "is on the "
for z in astro["people"]:
    print(f'{z["name"]} is on the {z["craft"]}')