import math

def generateKeypair():
    p = 53
    q = 59
    
    public_part1 = p * q
    public_part2 = 3 # 1 < public_part2 < lambda(public_part1)
    
    private_part1 = (p - 1) * (q - 1)
    k = 2
    private_part2 = ((k * private_part1) + 1) / public_part2
    
    file = open("comRSA.txt", "w")
    file.write(str(public_part1) + "\n")
    file.write(str(public_part2))
    file.close()
    
    # private_part2 = int(private_part2)
    
    return private_part2
    

def encryptMessage(public1, public2, message):

    #data encryption
    list1 = list(message)
    list2 = []
    encryptedList3 = []
    for i in range(len(list1)):
        charOrd = ord(list1[i])
        list2.append(charOrd)
    
    for i in range(len(list2)):
        cipherText = (int(list2[i]) ** int(public2)) % int(public1)
        encryptedList3.append(cipherText)
    
    return encryptedList3   

def decryptMessage(private2, public1, encryptedMessage):
    #data decryption
    encryptedList = list(encryptedMessage)
    encryptedList1 = []
    decryptedList = []
    decryptedData = 0
    myString = ''
    
    for i in range(len(encryptedList)):
        decryptedData = (int(encryptedList[i]) ** int(private2)) % int(public1)
        encryptedList1.append(decryptedData)
        decryptedChar = chr(encryptedList1[i])
        decryptedList.append(decryptedChar)
        str1 = str(decryptedList[i])
        myString += str1
        
    return myString

choice = input("\n1 - Encrypt\n2 - Decrypt\n3 - Exit\n--> ")
print("\n")
privateKey = generateKeypair()
if choice == "1":
    file1 = open("comRSA.txt")
    fileData = file1.readlines()
    publicKey1 = fileData[0]
    publicKey2 = fileData[1]
    file1.close()
    
    messageInput = input("Enter Message: ")
    
    encrypt = (encryptMessage(publicKey1, publicKey2, messageInput))
    
    with open("msg3.txt", "w") as file:
        for item in encrypt:
            file.write("%s\n" % item)
    # file2 = open("msg3.txt", "w")
    # file2.write(str(encryptMessage(publicKey1, publicKey2, messageInput)))
    # file2.close()
    print("\nEncrypted\n")
    
elif choice == "2":
    file1 = open("comRSA.txt")
    fileData = file1.readlines()
    publicKey1 = fileData[0]
    publicKey2 = fileData[1]
    file1.close()
    
    with open("msg3.txt", "r") as file3:
        encryptedMessage = file3.readlines()
    encryptedMessage = [x.strip() for x in encryptedMessage]
    decryptedMessage = decryptMessage(privateKey, publicKey1, encryptedMessage)
    print("Decrypted Message: " + str(decryptedMessage))

else:
    exit()
#encryptMessage(publicKey, message):


#decryptMessage(privateKey, encryptedMessage):

#generating public key
# p = 53
# q = 59

# public_part1 = p * q
# public_part2 = 3 # 1 < public_part2 < lambda(public_part1)
# public key (public_part1, public_part2)

# #generating private key
# private_part1 = (p - 1) * (q - 1)
# k = 2
# private_part2 = ((k * private_part1) + 1) / public_part2
# private_part2 = int(private_part2)

# input = 89

# #data encryption
# cipherText = (input ** public_part2) % public_part1
# print(cipherText)

# #data decryption
# decryptedData = (cipherText ** private_part2) % public_part1
# print(decryptedData)