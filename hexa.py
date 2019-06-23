s=input()
try:
    int(s,16)
    print("yes")
except ValueError:
    print("no")
