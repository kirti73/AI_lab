# Vacuum Cleaner Agent

# -1 = Move Left
#  0 = Clean
# +1 = Move Right
print("State : 1 = Dirty, 0 = Clean")
count=0
room = [1, 1]       # 1 = Dirty, 0 = Clean
room[0]=int(input("Enter state of left room:"))
room[1]=int(input("Enter state of right room:"))
pos = int(input("Enter position (0 = Left, 1 = Right): "))
while room[0] != 0 or room[1] != 0:

    if room[pos] == 1:
        action = 0
        room[pos] = 0
        count+=1
        print("Position:", pos, " Action:", action, "(Clean)")

    elif pos == 0:
        action = 1
        pos += action
        count+=1
        print("Position:", pos, " Action:", action, "(Move Right)")

    else:
        action = -1
        pos += action
        count+=1
        print("Position:", pos, " Action:", action, "(Move Left)")

print("Both rooms are clean.")
print("Cost=",count)
