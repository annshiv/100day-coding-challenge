number = int(input())
l=len(bin(number)[2:])
for i in range(1,number+1):
    print("{0:d}".format(i).rjust(l),"{0:o}".format(i).rjust(l),"{0:X}".format(i).rjust(l),"{0:b}".format(i).rjust(l))