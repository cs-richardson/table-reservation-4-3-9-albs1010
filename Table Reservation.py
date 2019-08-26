#Albert
#Asks for name 
name = input("Name: ")
reservation_name = "Albert"
"""
function that prints out "right this way" if the name == reservation_name,
if not it prints out "sorry we dont have a reservation under that name.
"""

def check_name(name, reservation_name):
    if name == reservation_name:
        print("Right this way!")
    else:
        print("Sorry, we don't have a reservation under that name.")
        

check_name(name, reservation_name)
