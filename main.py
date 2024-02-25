from fbchat import *
from fbchat.models import *
import messagewriter as msgwriter

email # = Input email as string.
username # = Input username here as a string.
password # = Input password here as string.


client = Client(email, password)
target_user_id # = Include target user id.
filename = "msges.txt"

fetched_user_ids = []  # List to store fetched user IDs

looper = True

# Infinite loop to run the program nonstop
while looper:
    
    consoletxt = input("input the console command (e.g., msgwriter, getinfo, logout): ")

    # Message logger
    if consoletxt == "msgwriter":
        if fetched_user_ids:
            target_user_id = input("Enter the user ID of the person whose messages you want to fetch: ")
            if target_user_id in fetched_user_ids:
                msgwriter.get_and_save_conversation(client, target_user_id)
            else:
                print("Invalid user ID. Please use 'getinfo' command to fetch user IDs.")
        else:
            print("No user IDs fetched yet. Please use 'getinfo' command first.")

    # Get certain people's user ID-s list corresponding to all the searched accounts
    elif consoletxt == "getinfo":
        name = input("input name and surname of a person: ")
        users = client.searchForUsers(name)
        for user in users:
            print(user.uid)
            fetched_user_ids.append(user.uid)  # Add fetched user ID to the list

    # Log out function
    elif consoletxt == "logout":
        try:
            client.logout()
            print("Logout successful.")
            looper = False
        except AttributeError:
            print("Failed to logout. Please try again later.")