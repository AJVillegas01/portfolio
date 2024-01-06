bottle_count_up=99
bottle_count_down=98
again =True
while again:
    print(f"{bottle_count_up} bottles of beer on the wall\n{bottle_count_up} bottles of beer\nTake one down, pass it around\n{bottle_count_down} bottles of beer on the wall\n")
    bottle_count_down=bottle_count_down-1
    bottle_count_up=bottle_count_up-1
    if bottle_count_up == 0:
        again=False
