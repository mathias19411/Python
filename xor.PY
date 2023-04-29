#Function for encryption and decryption
def encryptDecrypt(string, key):

	# perform XOR operation of key
	for i in range(len(string)):
	
		string = (string[:i] + chr(ord(string[i]) ^ ord(key)) + string[i + 1:])
		print(string[i], end = "")
	
	return string

# main body
if __name__ == '__main__':
    
    x = input("Let's Decrypt & Encrypt!\n1 - Encrypt\n2 - Decrypt\n3 - Exit\n--> ")
    
    if x == "1":
    # Encrypt the string
        message = str(input("\nText of your choice: "))
        messageKey = str(input("\nEnter a single character as your key (Pls remember your one-time-key): ")) #Random character as XOR key
        if len(messageKey) > 1:
            print("Error! only one character for key is allowed, pls try again!")
            exit()
        f = open("msg1.txt", "w")
        f.write(encryptDecrypt(message, messageKey))
        f.close()
        print("\nSaved to text file.\n")
        
    elif x == "2":
	# Decrypt the string
        messageKey = str(input("\nEnter your personal key: "))
        with open("msg1.txt", "r") as f:
            message = f.read()
        print("\nThe encrypted message is: " + message)
        decryptmsg = encryptDecrypt(message, messageKey)
        print("\nPlaintext: " + decryptmsg + "\n")

    else:
        print("\nThank you for using my program!")
        exit()

