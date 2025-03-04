""" 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
    2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
        1. Debe leer el archivo para importar los Pokémones existentes.
        2. Luego debe pedir la información del Pokémon a agregar.
        3. Finalmente debe guardar el nuevo Pokémon en el archivo. """

import json


def import_existing_pokemons():
  
    pokemons = [
    {
      "name": {
        "english": "Pikachu"
      },
      "type": [
        "Electric"
      ],
      "base": {
        "HP": 35,
        "Attack": 55,
        "Defense": 40,
        "Sp. Attack": 50,
        "Sp. Defense": 50,
        "Speed": 90
      }
    },
    {
      "name": {
        "english": "Charmander"
      },
      "type": [
        "Fire"
      ],
      "base": {
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Sp. Attack": 60,
        "Sp. Defense": 50,
        "Speed": 65
      }
    },
    {
      "name": {
        "english": "Squirtle"
      },
      "type": [
        "Water"
      ],
      "base": {
        "HP": 44,
        "Attack": 48,
        "Defense": 65,
        "Sp. Attack": 50,
        "Sp. Defense": 64,
        "Speed": 43
      }
    }
    ]

    try:
        path = "pokemons.json"
        with open(path, "w", encoding="utf-8", newline="") as json_file:
            pokemons_in_json = json.dumps(pokemons, indent = 4, separators= (",", ":"))
            json_file.write(pokemons_in_json)

    except Exception as ex:
        print("An error ocurred when importing existing pokemons.!!!")
        print(f"The obtained error is: {ex}")


def save_pokemon(name, type, hp, attack, defense, sp_attack, sp_defense, speed):
    path = "pokemons.json"
    
    try:
        pokemon_info = {
            "name": {
              "english": name
            },
            "type": [
              type
            ],
            "base": {
              "HP": hp,
              "Attack": attack,
              "Defense": defense,
              "Sp. Attack": sp_attack,
              "Sp. Defense": sp_defense,
              "Speed": speed
            }
          }
        
        with open(path, "r", encoding="utf-8") as file:
            json_content = file.read()
            data = json.loads(json_content)
        data.append(pokemon_info)

        with open(path, "w", encoding="utf-8", newline="") as json_file:
            pokemon_in_json = json.dumps(data, indent = 4, separators = (",", ":"))
            json_file.write(pokemon_in_json)
            
    except Exception as ex:
        print("An error ocurred when saving the given Pokemon!!!")
        print(f"Obtained error {ex}")


def main():
    counter = 0
    try:
        import_existing_pokemons()
        
        total_pokemons = int(input("How many Pokemons would you like to register?: "))
        while counter < total_pokemons:
            pokemon_name = input(f"What's the 'Name' of the {counter + 1}° Pokemon?: ")
            pokemon_type = input(f"What is the 'Type' of {pokemon_name}?: ")
            pokemon_hp = input(f"Which is the 'HP' of {pokemon_name}?: ")
            pokemon_attack = input(f"Which is the 'Attack' of {pokemon_name}?: ")
            pokemon_defense = input(f"Which is the 'Defense' of {pokemon_name}?: ")
            pokemon_sp_attack = input(f"Which is the 'S.p Attack' of {pokemon_name}?: ")
            pokemon_sp_defense = input(f"Which is the 'S.p Defense' of {pokemon_name}?: ")
            pokemon_speed = input(f"Which is the 'Speed' of {pokemon_name}?: ")

            save_pokemon(pokemon_name, pokemon_type, pokemon_hp, pokemon_attack, 
                pokemon_defense, pokemon_sp_attack, pokemon_sp_defense, pokemon_speed)

            counter += 1

    except Exception as ex:
        print("Something went wrong.!!!")
        exit()
    


if __name__ == "__main__":
    main()