import random
from datetime import datetime
f = open("wwb.log.txt", "w")
f.write("")
f = open("wwb.log.txt", "a")
space = 1
turn = 0
maxspace = 0
while space < 101 :
	turn += 1
	now = datetime.now()
	if random.randint(1,6) == 5 :
		if random.randint(1,6) == 5 :
			space += 1
			if space > maxspace :
				print ("Player reached space " + str(space) + " in turn " + str(turn) + " at " + str(now))
				maxspace = space
		else :
			space = 1
			f = open("wwb.log.txt", "w")
			f.write("")
			f = open("wwb.log.txt", "a")
	f.write("Time: " + str(now) + " ")	
	f.write("Turn: " + str(turn) + " ")
	f.write("Space: " + str(space) + " ")
	f.write("Record: " + str(maxspace) + " ")
	f.write("\n")
print("YOU'RE WINNER!")