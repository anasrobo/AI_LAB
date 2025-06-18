win_positions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
    ]
def game(player):
    print("\n", "|".join(mesh[:3]))
    print("----+----+----")
    print("\n", "|".join(mesh[3:6]))
    print("----+----+----")
    print("\n", "|".join(mesh[6:]))
    while True:
        try:
            ch = int(input(f"Enter Player Choice:"))
            if str(ch) not in mesh:
                raise ValueError
            mesh[ch-1] = player
            break
        except ValueError:
            print("Invalid")
    for wp in win_positions:
        if all(mesh[pos] == player for pos in wp):
            return wp
    return None
player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")
for i in range (9):
    won = game(player)
    if won:
        print("\n", "|".join(mesh[:3]))
        print("----+----+----")
        print("\n", "|".join(mesh[3:6]))
        print("----+----+----")
        print("\n", "|".join(mesh[6:]))
        print(f"**** Player {player} won! ***")
        break
    player = player1 if player == player2 else player2
else:
        print ("Game Ends In a Draw LOL") 
        
