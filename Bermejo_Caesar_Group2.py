#Functions
def encrypt(origMessage, switches): #forward
    encryptedMsg = ""
    for i in range(len(origMessage)):
        # for i in range(0, b):
        # message.insert(message.pop(0)) #pop() to remove the element and append() to move it to a specific index
        # message[i] = ord(message[i]) - b
        # message[i] = chr(message[i])
        indexChar = origMessage[i]
        
        if (indexChar.isalpha() and indexChar.isupper()): #Encryption for uppercase, and chaecking if it belongs to the alphabet
            encryptedMsg += chr((ord(indexChar) + switches-65) % 26 + 65)
        
        elif (indexChar.isalpha() and indexChar.islower()): #Encryption for lowercase, "     "      "  "    "     "   "     "
            encryptedMsg += chr((ord(indexChar) + switches-97) % 26 + 97) 
        
        else: #If non-alphabetical, add it to array
            encryptedMsg += " "
        
    return encryptedMsg  
    
def decrypt(encryptedMessage, switches): #backward
    decryptedMsg = ""
    for i in range(len(encryptedMessage)):
    # for i in range(0, b):
    #     message.append(message.pop(0)) #pop() to remove the element and append() to move it to a specific index
        # message[i] = ord(message[i]) - b
        # message[i] = chr(message[i])
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
# Main body

x = input("Let's Decrypt & Encrypt!\n1 - Encrypt\n2 - Decrypt\n3 - Exit\n--> ")

if x == "1":
    message = str((input("\nText of your choice: ")))
    messageShift = int((input ("Places to shift: ")))
    f = open("msg.txt", "w")
    f.write(encrypt(message, messageShift))
    f.close()
    print("\nSaved to text file.\n")
    
elif x == "2":
    messageShift = int((input ("\nPlaces to shift: ")))
    with open("msg.txt", "r") as f:
        message = f.read()
    print("\nThe encrypted message is: " + message)
    decryptmsg = decrypt(message, messageShift)
    print("Plaintext: " + decryptmsg + "\n")
    f.close()
else:
    print("\nThank you for using my program!")
    exit()
    
    