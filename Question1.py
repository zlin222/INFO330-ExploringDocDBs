from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon']

pikachu = pokemonColl.find_one({"name": "Pikachu"})
print(pikachu)
