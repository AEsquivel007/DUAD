""" 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB """

import csv

def save_a_game_in_csv(games_data):
    path_file = "games.csv"
    try:
        games_data_keys = games_data[0].keys()

        with open(path_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, games_data_keys)
            writer.writeheader()
            writer.writerows(games_data)

    except Exception as ex:
        print("An error ocurred when saving the games into CSV file!!!")


def print_saved_games_in_csv():
    path = "games.csv"
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for game in reader:
            print(game)


def main():
    counter = 0
    games_data = []
    
    try:
        total_of_video_games = int(input("How many video games would you like to save in a CSV file?: "))
        while counter < total_of_video_games:
            name = input(f"What's the name of the {counter + 1}° video game to save?: ")
            gender = input(f"What's the gender of the video game {name}?: ")
            developer = input(f"Which company developed {name}?: ")
            classification = input("What's its classification?: ")

            dict_game = {"Name":name,"Gender":gender,"Developer":developer,"Classification":classification}

            games_data.append(dict_game)

            save_a_game_in_csv(games_data)

            counter += 1
    except Exception as ex:
        print(f"Sorry, something went wrong!!! Obtained error: {ex}")


    inputUser:str = input("Would you like to see the saved information? (yes/no)?: ")
    input_lower_case = inputUser.lower()

    if input_lower_case == "yes":
        print_saved_games_in_csv()
    else:
        print("Thank you, bye!!!")
        exit()


if __name__ == "__main__":
    main()