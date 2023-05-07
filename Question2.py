from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon']

strong_pokemon = pokemonColl.find({"attack": {"$gt": 150}})
for everypokemon in strong_pokemon:
    print(everypokemon)
