name = input("Name: ")
reservation_name = "Albert"

def check_name(name, reservation_name):
    if name == reservation_name:
        print("Right this way!")
    else:
        print("Sorry, we don't have a reservation under that name.")
        

check_name(name, reservation_name)
