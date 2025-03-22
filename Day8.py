#Caeser Cipher

import string
letters  = list(string.ascii_letters)
#letters.append(" ")
nr_shift = int(input("please enter the shift number?\n"))
msg = input("please enter the message you wish to encrypt:\n")


#creating an encryption function
def encrypt(msg , nr_shift):
    encryptedMsg = []
    msgIndex = []
    spacesIndices = []
    #find the indices of the original msg
    for indexof, letter in enumerate(msg):
        if letter == " ":
            spacesIndices.append(indexof)
        for index, value in enumerate(letters):
            if letter == value:
                msgIndex.append(index)
    
    #encrypt them with the proper shift
    for i in msgIndex:
        encryptedMsg.append(letters[(i + nr_shift) % len(letters)])
    #adding spaces in proper location
    for x in spacesIndices:
        encryptedMsg.insert(x, " ")
    return ''.join(encryptedMsg)

encryptedMsg = encrypt(msg, nr_shift)
print(encryptedMsg)

#creating decrypt msg function
def decrypt(msg, nr_shift):
    decryptedMsg = []
    msgIndex = []
    spacesIndices=[]
    #find the indices of the original msg
    for ind, letter in enumerate(msg):
        if letter == " ":
            spacesIndices.append(ind)
        for index, value in enumerate(letters):
            if letter == value:
                msgIndex.append(index)
    #decrypt them with the proper shift
    for i in msgIndex:
        decryptedMsg.append(letters[(i - nr_shift) % len(letters)])
    #inserting spaces in proper location
    for x in spacesIndices:
        decryptedMsg.insert(x, " ")
    return ''.join(decryptedMsg)

decryptedMsg = decrypt(encryptedMsg, nr_shift)
print(decryptedMsg)



