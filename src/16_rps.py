import random
# Create a rock paper scissors game in python

# Player should be ables to type r,p, or s 

# Computer will pick r, p, or set

# Game will print out the results and keep track of wins, losses ans ties

# Type q to quit

# Build a REPL
choices = ["r", "p", "s"]
wins = 0
losses = 0
ties = 0

# LOOP
while True:
    print("Possible moves: 'Rock: r ', 'Paper: p ', 'Scissors: s ' ... type 'q' to Quit!!   ")
    print(f"\nWins: {wins}, Losses: {losses}, Ties: {ties}")
    # READ
    cmd= input("~~> ")
    # EVAL
    # Computer picks r/p/s
    cpu_move = random.choice(choices)
    if cmd == "r":
        if cpu_move == "r":
          print("It's a tie!")
          ties += 1
        elif cpu_move == "p":
          print("You just lost that round!")
          losses += 1
        elif cpu_move == "s":
          print('Well done, round won!!')
          wins += 1
    elif cmd == "p":
        if cpu_move == "p":
          print("It's a tie!")
          ties += 1
        if cpu_move == "r":
          print("You just lost that round!")
          wins += 1
        if cpu_move == "s":
          print("You just lost that round!")
          losses += 1
    elif cmd == "s":
        if cpu_move == "s":
          print("It's a tie!")
          ties += 1
        if cpu_move == "r":
          print("You just lost that round!")
          losses += 1
        if cpu_move == "p":
          print('Well done, round won!!')
          wins += 1           


    # Compare player command to cpu command
    if cmd == "q":
      print("GoodBye!!!")
      break
    # PRINT
    if cmd == "r":
      print(f"You chose: {cmd}ock!")
    elif cmd == "p":
      print(f"You chose: {cmd}aper!")  
    elif cmd == "s":
      print(f"You chose: {cmd}cissors!")
    elif cmd is not "r" or "p" or "s" or "q":
      print("Invalid input! try using 'r' , 'p' , or 's' .... press 'q' to quit! ")  
    
