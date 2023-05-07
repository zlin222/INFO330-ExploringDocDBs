from pymongo import MongoClient
import sqlite3

conn = sqlite3.connect('pokemon.sqlite')
cur = conn.cursor()

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon']

cur.execute("SELECT name, pokedex_number, type1, type2, \
            hp, attack, \
            defense, speed, sp_defense, sp_attack, \
            abilities FROM imported_pokemon_data")
result_set = cur.fetchall()

for row in result_set:
    general_query = list(row[:3])
    general_query.extend(row[4:10])

    cur.execute("""
                SELECT ability.name \
                FROM pokemon_abilities \
                JOIN ability ON pokemon_abilities.ability_id = ability.id \
                WHERE pokemon_abilities.pokemon_id = ?""", (row[1],))
    abilities_query = cur.fetchall()

    ability_query = [a[0] for a in abilities_query]

    pokemon = {
        "name": str(row[0]),
        "pokedex_number": row[1],
        "type1": row[2],
        "type2": row[3],
        "hp": row[4],
        "attack": int(row[5]),
        "defense": int(row[6]),
        "speed": int(row[7]),
        "sp_speed": int(row[8]),
        "sp_attack": int(row[9]),
        "abilities": ability_query
    }
    print(pokemon)
    pokemonColl.insert_one(pokemon)

count = pokemonColl.count_documents({})
print("Number of documents in the collection: ", count)


cur.close()
conn.close()
