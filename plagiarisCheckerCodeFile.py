#2018-cs-131
#this is the memoized recursive code in python for finding the longest common strings or substring from the given list
MAX_SIZE = 100000
resultArray=[" "for i in range(0,10)]
def LongestommonSubstring(str1,str2, n1, n2):            #it is a function  that return the number of matched characters
    global memoizedArray
    global resultArray
    i=0
    if (n1 == 0 or n2 == 0):
        return 0
    if (memoizedArray[n1 - 1][n2 - 1] != -1):       #if computed already then simply return that computed value
        return memoizedArray[n1 - 1][n2 - 1]
    if (str1[n1 - 1] == str2[n2 - 1]):        #case1: if matches then add 1 and call it self with length - 1
        resultArray[i] = str1[n1 - 1]
        i = i + 1
        memoizedArray[n1 - 1][n2 - 1] = 1 + LongestommonSubstring(str1, str2, n1 - 1, n2 - 1)
        return memoizedArray[n1 - 1][n2 - 1]
    else:                                           #case2: if dunno match
        memoizedArray[n1 - 1][n2 - 1] = max(LongestommonSubstring(str1, str2, n1, n2 - 1),
                               LongestommonSubstring(str1, str2, n1 - 1, n2))

        return memoizedArray[n1 - 1][n2 - 1]
str1=["ayesha", "is","also","a","girl","sky","is","blue","i","know","you","actually","i","know","him"]
str2=["iram"",is","also","a","girl","nobody","know","me","his"]
n1 = len(str1)
n2 = len(str2)

memoizedArray = [[-1 for i in range(MAX_SIZE)]
      for i in range(n1)]
print(resultArray)
print("Length of LCS:", LongestommonSubstring(str1, str2, n1, n2))
