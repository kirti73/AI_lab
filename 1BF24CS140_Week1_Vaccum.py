# Vacuum Cleaner Agent

# -1 = Move Left
#  0 = Clean
# +1 = Move Right

room = [1, 1]       # 1 = Dirty, 0 = Clean
pos = int(input("Enter position (0 = Left, 1 = Right): "))

while room[0] != 0 or room[1] != 0:

    if room[pos] == 1:
        action = 0
        room[pos] = 0
        print("Position:", pos, " Action:", action, "(Clean)")

    elif pos == 0:
        action = 1
        pos += action
        print("Position:", pos, " Action:", action, "(Move Right)")

    else:
        action = -1
        pos += action
        print("Position:", pos, " Action:", action, "(Move Left)")

print("Both rooms are clean.")
