def sonlar(*sonlar):
    yigindi = 1
    for son in sonlar:
        yigindi *= son
    return yigindi


print(sonlar(1, 2, 3, 4, 54, 5, ))
