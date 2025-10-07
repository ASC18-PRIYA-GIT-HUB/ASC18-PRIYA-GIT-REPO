import sys
print("Script name:", sys.argv[0])
print("Sixth argument:", sys.argv[6])
for arg in sys.argv[1:]:
    print("Argument:", arg)
if len(sys.argv) > 1:
    print("Argument passed:", sys.argv[1:])
else:
    print("No arguments passed")
    