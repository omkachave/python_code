command=""
while command.lower() != "quit":
    command= input(">")
    command= command.lower()
if command=="start":
    print("car started...")
elif command =="stop":
        print("car stop...")
elif command == "help":
    print("""
    start = car starrted 
    stop = car stop 
    quit = to quit
    """)


