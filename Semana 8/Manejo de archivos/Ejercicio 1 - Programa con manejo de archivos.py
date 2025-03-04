""" 1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente. """

def save_songs_alphabetically(song):
    path = "ordered_songs.txt"
    try:    
        with open(path, "a", encoding="utf-8") as file:
            file.write(song)
    except:
        print("An error ocurred when saving the songs into the new .txt file.!")


def read_and_order_songs(path):
    
    my_list_of_songs = []
    try:
        with open(path,"r", encoding="utf-8") as file:
            
            for song in file.readlines():
                my_list_of_songs.append(song)

            my_list_of_songs.sort()

            for ordered_song in my_list_of_songs:                
                save_songs_alphabetically(ordered_song)
    except:
        print("An error ocurred when reading and ordering the songs.!")


def print_ordered_songs(path="ordered_songs.txt"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for song in file.readlines():
                print(song)
    except:
        print("An error ocurred when printing the songs that were ordered alphabetically.!")


def main(path):
    try:
        read_and_order_songs(path)
        print_ordered_songs()
    except Exception as ex:
        print("An error ocurred when printing the ordered songs.!!!")
        print(ex)


if __name__ == "__main__":
    main("songs.txt")