"""
Workshop 3 - Donation Applet
By Sung Kim
Date 8/20/2022
"""

import sys
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""
amt_list = []

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)

    user_choice = input("Choose an option: ")

    if user_choice == "1" or user_choice == "Login".lower():
        username = input("\n" + "Enter username: ").casefold()
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif user_choice == "2" or user_choice == "Register".lower():
        username = input("\n" + "Enter username: ").casefold()
        password = input("Enter password: ")
        authorized_user = register(database, username, password)

    elif user_choice == "3" or user_choice == "Donate".lower():
        if authorized_user == "":
            print("You are not logged in!")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    elif user_choice == "4" or user_choice == "Show Donations".lower():
        show_donations(donations)

    elif user_choice == "5" or user_choice == "Exit".lower():
        print("Goodbye! Please consider donating more to DonateMe next time.")
        sys.exit()
