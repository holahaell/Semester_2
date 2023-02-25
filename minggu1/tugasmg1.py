nama = input("masukkan nama : ")
result = ""

with open("data.txt","r") as file:
    read = file.readlines()
    modified = []

    def findValue(fullstring):
        fullstring = fullstring.rstrip('\t\t')
        value = fullstring[fullstring.index+1:]
        return value
    
    for line in read:
        modified.append(line.strip())
        if nama.lower() in line.lower():
            result = line
            
print(result)





