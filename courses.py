import maincourse

def menu():

    menu = True
    while menu:
        print("Welcome to the S6C prospectus")
        print("Please select one of the following: ")
        print("1 - Look at available courses")
        print("2 - Add a new course")
        print("3- Exit the prospectus")

        option = input("What do you want to do?")
        if option == '1':
            print()
            print_courses()

        elif option == '2':
            print()
            new_course()

        elif option == '3':
            print("Goodbye for now....")
            exit()














































