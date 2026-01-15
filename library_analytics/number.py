def main_menu():
    eve_nums = []
    while True:
        print("1,Find a number between 1 and 15")
        print("2,Show the result")
        print("3,Quit")

        choice = input("Please choose a number:")
        if choice == "1":
            eve_nums = find_the_num()
        elif choice == "2":
            if eve_nums:
                print("Find the even numbers list")
            else:
                print("Please execute choice 1")
        else:
            print("Byebye")
            break
def find_the_num():
    counter = 0
    eve_nums = []
    while counter <= 15:
        if counter % 2 == 0:
            eve_nums.append(counter)
        counter += 1
    return eve_nums

if __name__ == "__main__":
    main_menu()