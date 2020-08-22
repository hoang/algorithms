import sys, getopt

def fibonacy(n):
	stack = [0, 1]
	result = 1
	for i in range(n-1):
		last = stack.pop()
		pre_last = stack.pop()
		result = last + pre_last
		stack.append(last)
		stack.append(result)
	return result

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:")
except getopt.GetoptError:
	print("usage: python3 program.py -n <number>")
	sys.exit(2)

n = 1
for opt, arg in opts:
	if opt == '-n':
		n = int(arg)

print("compute fibonacy at " + str(n) + " position:")
result = fibonacy(n)
print(result)
