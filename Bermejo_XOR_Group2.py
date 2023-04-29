#Function for encryption and decryption
def encryptDecrypt(string, key):

	# perform XOR operation of key
	for i in range(len(string)):
	
        # encryptedMsg += chr((ord(indexChar) + switches-65) % 26 + 65)
		string = (string[:i] + chr(ord(string[i]) ^ ord(key)) + string[i + 1:]) #Encrypting or decrypting each character of the message given the user-generated key
		print(string[i], end = "") #Printing each encrypted/decrypted character one-by-one into a string
	
	return string

# main body
if __name__ == '__main__':
    
    x = input("Let's Decrypt & Encrypt!\n1 - Encrypt\n2 - Decrypt\n3 - Exit\n--> ")
    
    if x == "1":
    # Encrypt the string
        message = str(input("\nText of your choice: "))
        messageKey = str(input("\nEnter a single character as your key (Pls remember your one-time-key): ")) #Random character as XOR key
        if len(messageKey) > 1:
            print("\nERROR! ONLY ONE CHARACTER for key is allowed, pls try again!\n") #Condition to check if the key contains only one character
            exit()
        f = open("msg1.txt", "w")#create new file
        f.write(encryptDecrypt(message, messageKey))#write data to file
        f.close()
        print("\nSaved to text file.\n")
        
    elif x == "2":
	# Decrypt the string
        messageKey = str(input("\nEnter your personal key: "))
        with open("msg1.txt", "r") as f: #open file and store its contents into a variable
            message = f.read()
        print("\nThe encrypted message is: " + message)
        decryptmsg = encryptDecrypt(message, messageKey)
        print("\nPlaintext: " + decryptmsg + "\n")

    else:
        print("\nThank you for using my program!")
        exit()

