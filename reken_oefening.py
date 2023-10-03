import os

def som(a, b):
    return a + b

def gemiddelde():
    total = 0
    count = 0

    while True:
        number = input("Type a number: ")

        if number.lower() == "stop":
            break

        try:
            total += int(number)
            count += 1

        except:
            print("Not a valid number!")


    if count == 0:
        print("Je hebt geen getallen ingevoerd!")

    else:
        average = total / count
        return average

def driehoek(basis, hoogte):
    return (basis * hoogte) / 2

def volume_cube(zijde):
    return zijde ** 3

def last_numbers(number):
    return number[-2:]



def main():
    while True:
        print("""Geef de keuze voor de bewerking die je wil doen:
        1) Som
        2) gemiddelde
        3) Oppervlak
        4) Volume kubus
        5) 2 laatste nummers""")
        keuze = int(input("Keuze: "))

        if keuze == 1:
            nummer1 = int(input("eerste waarde: "))
            nummer2 = int(input("Tweede waarde: "))
            print(som(nummer1, nummer2))
            input()
            os.system('clear')
        elif keuze == 2:
            average = gemiddelde()
            print(average)
            input()
            os.system('clear')
        elif keuze == 3:
            basis = int(input("Basis: "))
            hoogte = int(input('Hoogte: '))

            print(driehoek(basis, hoogte))
            input()
            os.system('clear')
        elif keuze == 4:
            zijde = int(input('zijde: '))
            print(volume_cube(zijde))
            input()
            os.system('clear')

        elif keuze == 5:
            nummer = input('Number: ')
            print(last_numbers(nummer))
            input()
            os.system('clear')
        else:
            print('Not a valid option!')
            input()
            break

if __name__ == "__main__":
    main()
