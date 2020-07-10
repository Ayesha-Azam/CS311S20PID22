from itertools import dropwhile, islice
str1 = []
str2 = []
file1 = open("txt1.txt", "r")
print(file1.readlines()[1])
for fnam in file1:
    with open(fnam) in file1:
        start_at = dropwhile(lambda L: '.' not in L.splite(), file1)
        for line in islice(start_at, 1, None):
           print(line)
