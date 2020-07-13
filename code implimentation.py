"""def dataReadingAndLCS(file1, file2):
    global resultArray
    global f1, f2
    global res
    i=0
    j=0
    char_arr1 = []
    char_arr2 = []
    string1 = []
    string2 = []
    #f1 = file1.read()
    #f2 = file2.read()
    l1 = len(f1)
    l2 = len(f2)
    f=0
    file1Lines=0
    file2Lines=0
    for q in range(0,l1):
        while f1[f] != ';':
            char_arr1.append(f1[f])
            f = f + 1
        file1Lines=file1Lines+1
    h=0
    for q in range(0,l2):
        while f2[h] != ';':
            char_arr2.append(f2[h])
            h = h + 1
        file1Lines=file1Lines+1
    print(file2Lines)
    if(l1>=l2):
        for g in range(0,l1):
            while f1[i]!=';':
                char_arr1.append(f1[i])
                i=i+1
            while f2[j]!=';':
                char_arr2.append(f2[j])
                j=j+1
                        # temp = 0
            s = LongestommonSubstring(char_arr2, char_arr2, len(char_arr1), len(char_arr2))
            char_arr2 = []
            char_arr1 = []
            #resultArray = string2
            res = res + s
    else:
        while f1[i] != ';':
            char_arr1.append(f1[i])
            i = i + 1
        while f2[j] != ';':
            char_arr2.append(f2[j])
            j = j + 1
            # temp = 0
        s = LongestommonSubstring(char_arr2, char_arr2, len(char_arr1), len(char_arr2))
        char_arr2 = []
        char_arr1 = []
        resultArray = string2
        res = res + s"""
MAX_SIZE = 10000
resultArray=[''for i in range(MAX_SIZE)]
def LongestommonSubstring(str1,str2, n1, n2):            #it is a function  that return the number of matched characters
    global memoizedArray
    global resultArray
    global k
    if (n1 == 0 or n2 == 0):
        return 0
    if (memoizedArray[n1 - 1][n2 - 1] != -1):       #if computed already then simply return that computed value
        return memoizedArray[n1 - 1][n2 - 1]
    if (str1[n1 - 1] == str2[n2 - 1]):   #case1: if matches then add 1 and call it self with length - 1
        #resultArray[k]=str1[n1-1]
        #k=k+1
        memoizedArray[n1 - 1][n2 - 1] = 1 + LongestommonSubstring(str1, str2, n1 - 1, n2 - 1)
        return memoizedArray[n1 - 1][n2 - 1]
    else:                                           #case2: if dunno match
        memoizedArray[n1 - 1][n2 - 1] = max(LongestommonSubstring(str1, str2, n1, n2 - 1),
                               LongestommonSubstring(str1, str2, n1 - 1, n2))

        return memoizedArray[n1 - 1][n2 - 1]
def CPPdataReadingAndLCS(file1, file2):
    global resultArray
    global f1, f2
    global res
    char_arr1 = []
    char_arr2 = []
    string1 = []
    string2 = []
    f1 = file1.read()
    f2 = file2.read()
    l1 = len(f1)
    l2 = len(f2)
    for i in range(0, l1):
        temp=0
        if f1[i] != ';':
            char_arr1.append(f1[i])
        else:
            string1 = ""
            for x in char_arr1:
                string1 += x
            for f in range(0, len(char_arr1)):
               if (char_arr1[f] == ' '):
                  char_arr1[f] = '\0'
            for j in range(0, l2):

                if f2[j] != ';':
                    char_arr2.append(f2[j])
                else:
                    string2 = ""
                    for y in char_arr2:
                        string2 += y
                    #temp = 0
                    #for f in range(0, len(char_arr1)):
                     #   if (char_arr1[f] == ' '):
                      #      char_arr1[f] = '\0'

                    for f in range(0, len(char_arr2)):
                        if (char_arr2[f] == ' '):
                            char_arr2[f] = '\0'
                    s=LongestommonSubstring(char_arr1,char_arr2,len(char_arr1),len(char_arr2))
                    if(s>temp):
                        temp =s
                        char_arr2 = []
                        char_arr1 = []
            resultArray = string2
            #print(string2, end=" ")
            res += temp
res = 0
k=0
doc1 = open('txt3.cpp', 'r')
textt1 = doc1.read()
p1=textt1
doc1.close()
resultArray = [" "for i in range(MAX_SIZE)]
doc2 = open('txt4.cpp', 'r')
p2=doc2.read()
p1=len(p1)
p2=len(p2)
doc2.close()
memoizedArray = [[-1 for i in range(MAX_SIZE)]
      for i in range(len(textt1))]
doc1=open('txt3.cpp','r')
doc2=open('txt4.cpp','r')
CPPdataReadingAndLCS(doc1, doc2)
print("matched words are: ")
print(resultArray)
#for i in range(len(resultArray)):
 #   if(resultArray[i]!=' '):
  #      print(resultArray[i], end=" ")
print(" ")
doc1.close()
doc2.close()
numerator=0
if(p1<p2):
    numerator=p1
elif(p1==p2):
    numerator=p1
else:
    numerator=p2
print(res)
percent=(res/numerator)*100
if(percent>70):
    print("these are plagiarised files")
else:
    print("this is not plagiarised text")

print("number of matched characters:",end="")
print(" ")
print(percent)