
player_A = input("Masukan pilihan dari pemain satu (kertas/gunting/batu) : ")
player_B= input("Masukan pilihan dari pemain dua (kertas/gunting/batu) : ")

if player_A == "kertas":
    if player_B == "batu":
        print("pemain A menang dan pemain B kalah, kertas mengalahkan batu")
    else:
        print("pemain A kalah dan pemain B menang, gunting mengalahkan kertas")
elif player_A == "gunting":
    if player_B == "kertas":
        print("pemain A menang dan pemain B kalah, gunting mengalahkan kertas")
    else:
        print("pemain A kalah dan pemain B menang, batu mengalahkan gunting")
else:
    if player_B == "gunting":
        print("pemain A menang dan pemain B kalah, batu mengalahkan gunting")
    else:
        print("pemain A kalah dan pemain B menang, kertas mengalahkan batu")
        
