MAX_SIZE=10000
def LongestommonSubstring(str1,str2, n1, n2):            #it is a function  that return the number of matched characters
    global memoizedArray
    global resultArray
    i=0
    global k
    if (n1 == 0 or n2 == 0):
        return 0
    if (memoizedArray[n1 - 1][n2 - 1] != -1):       #if computed already then simply return that computed value
        return memoizedArray[n1 - 1][n2 - 1]
    if (str1[n1 - 1] == str2[n2 - 1]):   #case1: if matches then add 1 and call it self with length - 1
        resultArray[k]=str1[n1-1]
        k=k+1
        memoizedArray[n1 - 1][n2 - 1] = 1 + LongestommonSubstring(str1, str2, n1 - 1, n2 - 1)
        return memoizedArray[n1 - 1][n2 - 1]
    else:                                           #case2: if dunno match
        memoizedArray[n1 - 1][n2 - 1] = max(LongestommonSubstring(str1, str2, n1, n2 - 1),
                               LongestommonSubstring(str1, str2, n1 - 1, n2))

        return memoizedArray[n1 - 1][n2 - 1]
def dataReadingAndLCS(file1, file2):
    global resultArray
    global res
    temp=0
    char_arr1 = []
    char_arr2 = []
    string1=[]
    string2=[]
    file1 = open('text1.txt', 'r')
    f1 = file1.read()
    f2 = file2.read()
    l1 = len(f1)
    l2 = len(f2)
    for i in range(0, l1):

        if f1[i] != '.':
            char_arr1.append(f1[i])
        else:
            string1 = ""
            for x in char_arr1:
                string1 += x
            for j in range(0, l2):

                if f2[j] != '.':
                    char_arr2.append(f2[j])
                else:
                    string2 = " "
                    for y in char_arr2:
                        string2 += y
                        char_arr2=[]
                temp=0
               # print("length is ",LongestommonSubstring(string1,string2,len(string1),len(string2)))
                if(LongestommonSubstring(string1,string2,len(string1),len(string2))>temp):
                    temp=LongestommonSubstring(string1,string2,len(string1),len(string2))
                #length_of_lcs(strin1, string2)
                    #char_arr2 = []
            res += temp
            char_arr1 = []

k=0
doc1 = open('text1.txt', 'r')
textt1=doc1.read()
doc1.close()
resultArray=[" "for i in range(MAX_SIZE)]
res=0
doc2 = open('text2.txt', 'r')
memoizedArray = [[-1 for i in range(MAX_SIZE)]
      for i in range(len(textt1))]
dataReadingAndLCS(doc1, doc2)
print("matched words are: ")
for i in range(MAX_SIZE):
    if(resultArray[i]!=" "):
        print(resultArray[i],end="")

print(" ")
print(res)MAX_SIZE=10000
def LongestommonSubstring(str1,str2, n1, n2):            #it is a function  that return the number of matched characters
    global memoizedArray
    global resultArray
    i=0
    global k
    if (n1 == 0 or n2 == 0):
        return 0
    if (memoizedArray[n1 - 1][n2 - 1] != -1):       #if computed already then simply return that computed value
        return memoizedArray[n1 - 1][n2 - 1]
    if (str1[n1 - 1] == str2[n2 - 1]):   #case1: if matches then add 1 and call it self with length - 1
        resultArray[k]=str1[n1-1]
        k=k+1
        memoizedArray[n1 - 1][n2 - 1] = 1 + LongestommonSubstring(str1, str2, n1 - 1, n2 - 1)
        return memoizedArray[n1 - 1][n2 - 1]
    else:                                           #case2: if dunno match
        memoizedArray[n1 - 1][n2 - 1] = max(LongestommonSubstring(str1, str2, n1, n2 - 1),
                               LongestommonSubstring(str1, str2, n1 - 1, n2))

        return memoizedArray[n1 - 1][n2 - 1]
def dataReadingAndLCS(file1, file2):
    global resultArray
    global res
    temp=0
    char_arr1 = []
    char_arr2 = []
    string1=[]
    string2=[]
    file1 = open('text1.txt', 'r')
    f1 = file1.read()
    f2 = file2.read()
    l1 = len(f1)
    l2 = len(f2)
    for i in range(0, l1):

        if f1[i] != '.':
            char_arr1.append(f1[i])
        else:
            string1 = ""
            for x in char_arr1:
                string1 += x
            for j in range(0, l2):

                if f2[j] != '.':
                    char_arr2.append(f2[j])
                else:
                    string2 = " "
                    for y in char_arr2:
                        string2 += y
                        char_arr2=[]
                temp=0
               # print("length is ",LongestommonSubstring(string1,string2,len(string1),len(string2)))
                if(LongestommonSubstring(string1,string2,len(string1),len(string2))>temp):
                    temp=LongestommonSubstring(string1,string2,len(string1),len(string2))
                #length_of_lcs(strin1, string2)
                    #char_arr2 = []
            res += temp
            char_arr1 = []

k=0
doc1 = open('text1.txt', 'r')
textt1=doc1.read()
doc1.close()
resultArray=[" "for i in range(MAX_SIZE)]
res=0
doc2 = open('text2.txt', 'r')
memoizedArray = [[-1 for i in range(MAX_SIZE)]
      for i in range(len(textt1))]
dataReadingAndLCS(doc1, doc2)
print("matched words are: ")
for i in range(MAX_SIZE):
    if(resultArray[i]!=" "):
        print(resultArray[i],end="")

print(" ")
print(res)