import random

# Computer randomly chooses -1 (Rock), 0 (Paper), or 1 (Scissors)
computer = random.choice([-1, 0, 1])

# User inputs choice as "r" for Rock, "p" for Paper, "s" for Scissors
youstr = input("Enter Your Choice (r for Rock, p for Paper, s for Scissors): ").lower()
youdict = {"r": -1, "p": 0, "s": 1}  # Maps choices to values
reversedict = {-1: "Rock", 0: "Paper", 1: "Scissors"}  # Maps values to choices

# Check if the input is valid
if youstr not in youdict:
    print("Invalid input! Please choose 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
else:
    you = youdict[youstr]
    
    print(f"You Choose {reversedict[you]}\nComputer Choose {reversedict[computer]}")

    # Determine the result
    if computer == you:
        print("It's a Draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("Computer Wins!")
    else:
        print("You Win!")
