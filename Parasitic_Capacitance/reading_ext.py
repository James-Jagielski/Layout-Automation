parasitic_nets = dict()
file1 = open("inverter.ext", "r+")
lines = file1.readlines()


def SPICE_read():
    file1 = open("nmos.sch", "r+")
    lines = file1.readlines()
    for row in lines:
        # check if string present on a current line
        #word1 = 'name'
        word = "cap"

        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring

        # if row.find(word1) != -1:
        #     print(row[row.index(word1) + len(word1):])
        if row.find("cap") != -1:
            key = row[row.index(word)+ len(word):len(row)-8:]
            cap = row[len(row)-8:]
            addnet(key,cap)
        file1.close()
    return(parasitic_nets)

def addnet(name, number):
    for i in parasitic_nets:
        if i == name:
            print('error')
            return
    parasitic_nets[name] = number




#parasitic_nets = dict()
#file1 = open("inverter.ext", "r+")
'''lines = file1.readlines()
for row in lines:
    # check if string present on a current line
    #word1 = 'name'
    word = "cap"
    word2 = "6"

    # find() method returns -1 if the value is not found,
    # if found it returns index of the first occurrence of the substring

    if row.find(word) != -1:
        print(row[row.index(word) + len(word):])
        print(row[row.index(word)+ len(word):len(row)-8:])
    #    if row.find("cap") != -1:
    #        print(word + row[row.index(word) + len(word):])
        key = row[row.index(word)+ len(word):len(row)-8:]
        cap = row[len(row)-8:]
    file1.close()
'''


