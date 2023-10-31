def SPICE_read():
    file1 = open("nmos.sch", "r+")
    lines = file1.readlines()
    for row in lines:
        # check if string present on a current line
        #word1 = 'name'
        word2 = 'L='
        word3 = 'W='

        #print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring

        # if row.find(word1) != -1:
        #     print(row[row.index(word1) + len(word1):])
        #     print('string exists in file')
        #     print('line Number:', lines.index(row)+1)
        if row.find(word2) != -1:
            print(word2 + row[row.index(word2) + len(word2):])
            L = float(row[row.index(word2) + len(word2):])
            # print('string exists in file')
            # print('line Number:', lines.index(row)+1)
        if row.find(word3) != -1:
            print(word3 + row[row.index(word3) + len(word3):])
            W = int(row[row.index(word3) + len(word3):])
            # print('string exists in file')
            # print('line Number:', lines.index(row)+1)
        file1.close() 

    return(L,W)


