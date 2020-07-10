def greedy_activity_selector(file1, file2):

    char_arr1 = []
    char_arr2 = []

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
                    string2 = ""
                    for y in char_arr2:
                        string2 += y
                    #lcs(string1, string2)
                    #length_of_lcs(strin1, string2)
                    print("this is 2nd file"+ string2)
                    char_arr2 = []
            print("this is 1st file"+string1)
            char_arr1 = []





doc1 = open('txt1.txt', 'r')
doc2 = open('txt2.txt', 'r')
greedy_activity_selector(doc1, doc2)