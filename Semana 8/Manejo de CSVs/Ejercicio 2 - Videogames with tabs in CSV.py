""" Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de 
        arriba que guarde el archivo separado por tabulaciones en vez de por comas. """

import csv

def save_a_game_in_csv_with_delimiter(games_data):
    path = "games_with_delimiter.csv"
    field_names = ["Name", "Gender", "Developer", "Classification"]
    try:
        with open(path, "w", encoding="utf-8", newline= "") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(field_names)
            writer.writerows(games_data)
    except Exception as ex:
        print("Something went wrong when writing the games into the .CSV file.!!!")
        print("The obtained error was :{ex}")

def print_saved_games_with_delimiter():
    path = "games_with_delimiter.csv"
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="\t")

            next(reader)

            for row in reader:
                print(f"Video game: {row[0]}, Gender: {row[1]}, Developer: {row[2]}, Classification: {row[3]}")

    except Exception as ex:
        print("Something went wrong when reading the games into the .CSV file.!!!")
        print("The obtained error was :{ex}")


def main():
    counter = 0
    games_data = []

    try:
        total_of_games = int(input("How many video games would you like to save?: "))

        while counter < total_of_games:
            name = input(f"What's the name of the {counter + 1}° video game to save?: ")
            gender = input(f"What's the gender of the video game {name}?: ")
            developer = input(f"Which company developed {name}?: ")
            classification = input("What's its classification?: ")

            list_game = [name, gender, developer, classification]
            games_data.append(list_game)

            save_a_game_in_csv_with_delimiter(games_data)

            counter += 1

    except Exception as ex:
        print(f"Something went wrong, the obtained error was :{ex}")

    inputUser:str = input("Would you like to see the saved information? (yes/no)?: ")
    input_lower_case = inputUser.lower()

    if input_lower_case == "yes":
        print_saved_games_with_delimiter()
    else:
        print("Thank you, bye!!!")
        exit()
    

if __name__ == "__main__":
    main()