from human import Human
def main():
    human = Human("Alberth")
    human.introduce()
    human.breathe()
    human.move_arms()
    human.grab_object("Phone")
    human.walk()
    human.step()
    print(human)


if __name__ == "__main__":
    main()