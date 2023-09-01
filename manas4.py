a = int(input("enter your age here"))

re =a>=18
out=('Can vote' * re + 'Cannot vote' * (1-re))

print(out)
