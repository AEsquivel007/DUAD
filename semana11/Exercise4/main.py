from human import Human
def main():
    human = Human("Alberth")
    human.presentarse()
    human.respirar()
    human.mover_brazos()
    human.agarrar_objeto("Teléfono")
    human.caminar()
    human.dar_paso()
    print(human)


if __name__ == "__main__":
    main()