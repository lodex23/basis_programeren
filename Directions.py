def Direction(a):
    if a == "up":
        print("up")
    elif a == "left":
        print('left')
    elif a == "down":
        print("down")
    elif a == "right":
        print("down")

def main():
    direction = input("Give a direction: ")

    Direction(direction)



if __name__ == "__main__":
    main()

