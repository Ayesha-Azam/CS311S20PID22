def greedy_activity_selector():

    a = []
    k = 0
    file1 = open('txt1.txt', 'r')
    s = file1.readline()

    n = len(s)
    for m in range(0, n):
        if s[m] != '.':
            a.append(s[m])
        else:
            break
        print(a)



print(greedy_activity_selector())