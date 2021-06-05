to_do = input("What's the first thing that comes to mind that needs to get done around here?\n")
how_important = input("How important on a scale of 1-10 is this to do item?\n")
prioritys = []


while to_do.lower() != "q":
	how_important_plus_to_do = str(how_important) + "." + " " + to_do
	prioritys.append(how_important_plus_to_do)
	to_do = input("Anything else that needs to be done? Type Q to quit and be shown your list\n")
	if to_do.lower() == "q":
		break
	else:
		how_important = input("How important on a scale of 1-10 is this to do item?\n")

print("\n")
print("/"*40)	
prioritys.sort()
print("Here is your to-do list, descending from most important to least.\n")
for item in prioritys:
	print(item)