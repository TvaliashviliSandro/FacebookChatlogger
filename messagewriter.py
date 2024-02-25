#Gathering and logging the texts in the chat.
def get_and_save_conversation(client, target_user_id, filename="msges.txt"):
    
    try:
        # Fetch the user's thread (conversation)
        thread_info = client.fetchThreadInfo(target_user_id)
        thread = thread_info[target_user_id]
        
        # Get the conversation messages
        messages = client.fetchThreadMessages(thread_id=target_user_id, limit=1000)  # Adjust the limit as needed

        # Open the file for writing
        with open(filename, 'w', encoding='utf-8') as file:

            # Iterate through messages and write them to the file
            for message in messages:
                if message.author == client.uid:  # Check if the message is sent by you
                    sender_name = "You"
                else:
                    sender_name = client.fetchUserInfo(message.author)[message.author].name

                # Write message to file
                file.write(f"{sender_name}: {message.text} time:{message.timestamp}\n")

        print(f"Conversation saved to {filename}") #Console conformation for the log
    except Exception as e:
        print(f"Error: {e}")