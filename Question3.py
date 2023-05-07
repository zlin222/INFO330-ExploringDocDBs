from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon']

overgrow_pokemon = pokemonColl.find({"abilities": {"$in": ['Overgrow']}})
for overgrow in overgrow_pokemon:
    print(overgrow)
