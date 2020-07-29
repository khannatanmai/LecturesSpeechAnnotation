import sys

fin = open(sys.argv[1],'r').readlines()

for line in fin:
	for i in range(len(line)):

		if(line[i] in ['<', '[', '{']):
			print("\n", end="")
			print(line[i], end="")

		elif(line[i] in ['>', ']', '}']):
			print(line[i], end="")
			print("\n", end="")

		else:
			print(line[i], end="")
