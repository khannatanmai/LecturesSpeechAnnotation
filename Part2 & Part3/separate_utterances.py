import sys

fin = open(sys.argv[1],'r').readlines()
dont_separate = False

for line in fin:
	for i in range(len(line)):

		if(line[i] in ['<', '[', '{']):
			if(line[i+1:i+3] == "ft" or line[i+1:i+3] == "rt" or line[i+1:i+4] == "emp"):
				dont_separate = True
				print(line[i], end="")
				continue

			print("\n", end="")
			print(line[i], end="")

		elif(line[i] in ['>', ']', '}']):
			if(dont_separate):
				print(line[i], end="")
				dont_separate = False
				continue

			print(line[i], end="")
			print("\n", end="")

		else:
			print(line[i], end="")
