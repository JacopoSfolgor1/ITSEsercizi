n_players = int(input("Please state how many players: "))

for n in range(1, n_players +1):
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n== 3:
        print(f"{n}rd")
    else: 
        print(f"{n}th")
    n_players -= 1


