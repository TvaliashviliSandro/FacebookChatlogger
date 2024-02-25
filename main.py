from fbchat import *
from fbchat.models import *
import messagewriter as msgwriter

email # = Input email as string.
username # = Input username here as a string.
password # = Input password here as string.


client = Client(email, password)
target_user_id # = Include target user id.
filename = "msges.txt"

looper = True

# Infinite loop to run the program nonstop 

while looper == True:
        consoletxt = str(input("input the console command (f.e: msgwriter, getinfo, logout): "))

        # Message logger
        if consoletxt == "msgwriter":
                msgwriter.get_and_save_conversation(client, target_user_id)

        # Get certain peples user ID-s list corresponding to all the searched accounts
        if consoletxt == "getinfo":
                name = str(input("input name and surname of a person: "))
                users = client.searchForUsers(name)
                for i in range(0, len(users)):
                        user = users[i]
                        print(user.uid)
        
        # Log out function (in proggress / bug with logging out)
        if consoletxt == "logout":
                try:
                        client.logout()
                        print("Logout successful.")
                        looper = False
                except AttributeError:
                         print("Failed to logout. Please try again later.")

