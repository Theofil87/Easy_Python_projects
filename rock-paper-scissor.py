import random

# List of game options
options = ["kő", "papír", "olló"]

# Function to get computer's choice
def computer_choice():
    return random.choice(options)

# Function to get winner
def get_winner(user, computer):
    if user == computer:
        return "Döntetlen"
    elif user == "kő" and computer == "papír":
        return "Számítógép nyert"
    elif user == "papír" and computer == "olló":
        return "Számítógép nyert"
    elif user == "olló" and computer == "kő":
        return "Számítógép nyert"
    else:
        return "Te nyertél"

# Game loop
while True:
    print("Válassz a következő lehetőségek közül: kő, papír, olló")
    user_choice = input().lower()
    if user_choice not in options:
        print("Érvénytelen bevitel. Próbálkozz újra.")
    else:
        computer = computer_choice()
        winner = get_winner(user_choice, computer)
        print(f"Te: {user_choice}, Számítógép: {computer}")
        print(f"A nyertes: {winner}")
        play_again = input("Szeretnél újra játszani? (Igen/Nem)").lower()
        if play_again != "igen":
            break
