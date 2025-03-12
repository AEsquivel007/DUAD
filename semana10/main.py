import utilities


def main():
    try:
        while True:
            utilities.display_menu()
            result = utilities.ask_if_continue()
            
            if not result:
                print("Muchas gracias por usar el Sistema de Control de Estudiantes de Lyfter. Adiós...")
                break
        
    except Exception as ex:
        print("ERROR: Ha ocurrido un error.")
        print(f"Error obtenido por el sistema: {ex}")
        exit()


if __name__ == '__main__':
    main()