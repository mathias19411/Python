# prime = 17
# gen = 3
# key1 = 5
# key2 = 18

# A = (gen**key1) % prime #5
# print(A)

# B = (gen**key2) % prime #9
# print(B)

# sharedKey1 = (B % prime ** key1) % prime #9
# print(sharedKey1)
# sharedKey2 = (A % prime ** key2) % prime #5
# print(sharedKey2)

def combinedKeyGenerator(prime, gen, key):
    key = int(key)
    prime = int(prime)
    gen = int(gen)
    
    combinedKey = (gen**key) % prime
    strKey = str(combinedKey)
    return strKey

def sharedKeyGenerator1(prime, gen, key1, swapKey1):
    prime = int(prime)
    gen = int(gen)
    key1 = int(key1)
    swapKey1 = int(swapKey1)
    
    aliceSharedKey = (swapKey1 ** key1) % prime
    strSharedKey = aliceSharedKey
    
    return strSharedKey

def sharedKeyGenerator2(prime, gen, key2, swapKey2):
    prime = int(prime)
    gen = int(gen)
    key2 = int(key2)
    swapKey2 = int(swapKey2)
    
    bobSharedKey = (swapKey2 ** key2) % prime
    strSharedKey = bobSharedKey
    
    return strSharedKey

def sharedKeyGenerator3(prime, gen, key1, key2, swapKey1, swapKey2):
    prime = int(prime)
    gen = int(gen)
    key1 = int(key1)
    key2 = int(key2)
    swapKey1 = int(swapKey1)
    swapKey2 = int(swapKey2)
    
    
    aliceSharedKey = (swapKey1 ** key1) % prime
    bobSharedKey = (swapKey2 ** key2) % prime
    strSharedKey = (aliceSharedKey +bobSharedKey) / 2
    
    return strSharedKey

def sharedKeyGenerator4(prime, gen, key1, key2, swapKey1, swapKey2):
    prime = int(prime)
    gen = int(gen)
    key1 = int(key1)
    key2 = int(key2)
    swapKey1 = int(swapKey1)
    swapKey2 = int(swapKey2)
    
    
    aliceSharedKey = (swapKey1 ** key1) % prime
    bobSharedKey = (swapKey2 ** key2) % prime
    strSharedKey = (aliceSharedKey +bobSharedKey) / 2
    
    return strSharedKey

def encrypt(origMessage): #forward
    encryptedMsg = ""
    switches = 7
    for i in range(len(origMessage)):
        indexChar = origMessage[i]
        
        if (indexChar.isalpha() and indexChar.isupper()): #Encryption for uppercase, and chaecking if it belongs to the alphabet
            encryptedMsg += chr((ord(indexChar) + switches-65) % 26 + 65)
        
        elif (indexChar.isalpha() and indexChar.islower()): #Encryption for lowercase, "     "      "  "    "     "   "     "
            encryptedMsg += chr((ord(indexChar) + switches-97) % 26 + 97) 
        
        else: #If non-alphabetical, add it to array
            encryptedMsg += " "
        
    return encryptedMsg  
    
def decrypt(encryptedMessage): #backward
    decryptedMsg = ""
    switches = 7
    for i in range(len(encryptedMessage)):
        indexChar = encryptedMessage[i]
        
        if (indexChar.isupper() and indexChar.isalpha()): #Decryption for uppercase, and chaecking if it belongs to the alphabet
            decryptedMsg += chr((ord(indexChar) - switches-65) % 26 + 65)
            #decryptedMsg += chr((ord(indexChar) + switches-65) % 26 + 62)
        
        elif (indexChar.islower() and indexChar.isalpha()): #Decryption for lowercase, "     "      "  "    "     "   "     "
            decryptedMsg += chr((ord(indexChar) - switches-97) % 26 + 97) 
            #decryptedMsg += chr((ord(indexChar) + switches-97) % 26 + 94) 
            
        else: #If non-alphabetical, add it to array
            decryptedMsg += " "
            
    return decryptedMsg

#Main body

user = input("\nEnter your name: ")
userKey = input("Enter your secret key: ")

choice = input("\n1 - Create combined key\n2 - Send message\n3 - Receive message\n--> ")
print("\n")

f = open("pub.txt") #opens a text file containing the two constant numbers
fileMessage = f.readlines() # e.g. 23 and 9
num1 = fileMessage[0]
num2 = fileMessage[1]
f.close()

if choice == "1":
    userCombinedKey = combinedKeyGenerator(num1, num2, userKey)
    f = open("com.txt", "a")
    f.write(userCombinedKey + "\n")
    f.close()
    
    f1 = open("msg2.txt", "a")
    f1.write(userKey + "\n")
    f1.close()
    
    
elif choice == "2":
    print("\nSend:")
    message = input("\nEnter message: ")
    f = open("ciph.txt", "w")
    f.write(encrypt(message)) 
    f.close()
    
elif choice == "3":
    f = open("com.txt")
    message = f.readlines()
    f1 = open("msg2.txt")
    message1 = f1.readlines()
    
    key1 = message1[0]
    key2 = message1[1]
    key2ToKey1 = message[1]
    key1ToKey2 = message[0]
    
    f.close()
    f1.close()
    sharedKey1 = sharedKeyGenerator1(num1, num2, key1, key2ToKey1)
    sharedKey2 = sharedKeyGenerator2(num1, num2, key2, key1ToKey2)
    sharedKey3 = sharedKeyGenerator3(num1, num2, key1, userKey, key2ToKey1, key1ToKey2)
    sharedKey4 = sharedKeyGenerator4(num1, num2, userKey, key2, key2ToKey1, key1ToKey2)
    
    if sharedKey1 == sharedKey2 and sharedKey1 == sharedKey3 or sharedKey2 == sharedKey4:
        print("\nReceive:")
        with open("ciph.txt", "r") as f2:
            message = f2.read()
        decryptmsg = decrypt(message)
        print("\nDecrypted message: " + decryptmsg + "\n")
        f2.close()
    else:
        print("\nReceive:")
        with open("ciph.txt", "r") as f2:
            message = f2.read()
        print("\nDecrypted message: " + message + "\n")
        f2.close()
else:
    print("\nINVALID INPUT! Please re-run the program!")
    exit()
