print("-TODO 1-")
User1 = (input("What is the name of the first user ? "))
User2 = (input("What is the name of the second user ? "))

message = ""
user_speaking = User1

while message != "exit":
    message = input(user_speaking + " write your message: ")
    print(user_speaking + ": " + message)

    if user_speaking == User1:
        user_speaking = User2
    else:
        user_speaking = User1
