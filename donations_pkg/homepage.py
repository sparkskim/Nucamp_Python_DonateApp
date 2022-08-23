"""
Workshop 3 - Donation Applet
By Sung Kim
Date 8/20/2022
"""


def show_homepage():
    """
    function that prints graphics for homepage
    """
    print("\n" + "              === DonateMe Homepage ===          ")
    print("--------------------------------------------------------")
    print("| 1.        Login         | 2.        Register        | ")
    print("--------------------------------------------------------")
    print("| 3.        Donate        | 4.     Show Donations     | ")
    print("--------------------------------------------------------")
    print("| 5.                       Exit                       | ")
    print("--------------------------------------------------------")


def donate(username):
    """
    function that prompts users to donate
    """

    try:
        donation_amt = float(input("Enter amount to donate: $"))
    except ValueError:
        print(
            "Enter positive number only. Start the DonateMe application again from the top."
        )
    donation_string = f"{username} donated ${donation_amt}"
    print("Thank you for your donation!", donation_string)

    return donation_string


def show_donations(donations):
    """
    function that shows each and total donation amounts
    """

    print("\n---All Donations---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        total = 0
        for donation_string in donations:
            print(donation_string)
            # bonus task3 credit: Alvaro Monasterio's solution from 1/24/2022 (perhaps instructor) from onea-2022-01-03 via Slack
            # I don't expect credit for this but still wanted to see how bonus task3 can be done
            index = donation_string.find("$") + 1
            total += float(donation_string[index:])
        print(f"Total donation = ${total}")
