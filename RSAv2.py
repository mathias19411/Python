import math

def generateKeypair():
    p = 53
    q = 59
    
    public_part1 = p * q
    public_part2 = 7 # 1 < public_part2 < lambda(public_part1)
    
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
    myString = ''
    for i in range(len(list1)):
        charOrd = ord(list1[i])
        list2.append(charOrd)

    for i in range(len(list2)):
        str1 = str(list2[i])
        myString += str1
    print(myString)
    cipherText = (int(myString) ** int(public2)) % int(public1)
    
    return cipherText

def decryptMessage(private2, public1, encryptedMessage):
    #data decryption
    decryptedData = (int(encryptedMessage) ** int(private2)) % int(public1)

    return decryptedData

choice = input("\n1 - Encrypt\n2 - Decrypt\n--> ")
print("\n")
privateKey = generateKeypair()
if choice == "1":
    file1 = open("comRSA.txt")
    fileData = file1.readlines()
    publicKey1 = fileData[0]
    publicKey2 = fileData[1]
    file1.close()
    
    messageInput = input("Enter Message: ")
    file2 = open("msg3.txt", "w")
    file2.write(str(encryptMessage(publicKey1, publicKey2, messageInput)))
    file2.close()
    print("\nEncrypted\n")
    
elif choice == "2":
    file1 = open("comRSA.txt")
    fileData = file1.readlines()
    publicKey1 = fileData[0]
    publicKey2 = fileData[1]
    file1.close()
    
    with open("msg3.txt", "r") as file3:
        encryptedMessage = file3.read()
        
    decryptedMessage = decryptMessage(privateKey, publicKey1, encryptedMessage)
    print("Decrypted Message: " + str(decryptedMessage))

# string = "Hello"
# list1 = list(string)
# list2 = []
# myString = ' '
# for i in range(len(list1)):
#     charOrd = ord(list1[i])
#     list2.append(charOrd)
# print(list2)

# for i in range(len(list2)):
#     str1 = str(list2[i])
#     myString += str1
# print(myString)