#SETUP
#run in terminal '' pip install tqdm '' 

from tqdm import tqdm  
import time
choice = "" 
while choice != "3":
    print("XOR Cipher: Encryption and Decryption.\n\n")
    print("Select the number that corresponds your choice:\n1 --> Encrypt\n2 --> Decrypt\n3 --> Exit\n")
    choice = input("Choice: ")
    if choice == "1": #Encryption.
        # with open ('message.txt', 'r') as f:  UNCOMMENT THIS CODE IF YOU WANT TO READ THE MESSAGE FROM A FILE
        #     message = f.read()
        message = input("Enter Your Message: ")    
            
        print(">>>Encryption<<<")
        shift = input("Encryption Key: ") #input the encryption key
        enc_msg = "" #Default value for enc_msg
        with tqdm(total=len(message), desc="Encrypting") as pbar: #Initialize the progress bar with the length of the message
            for k in range(len(shift)):
                shft = shift[k]
            for i in range(len(message)): #Counting the length of the entered message
                time.sleep(0.01)
                msg_shft = message[i]
                enc_msg += chr(ord(msg_shft) ^ ord(shft)) ##Getting the ASCII value of msg_shft and shft and converting it to a character
                pbar.update(1) #Increment the progress bar
        with open("cipher.txt", "w") as f: #Openning the msg.txt 
            f.write(enc_msg) #Saving the encrypted message into the msg.txt file
        print("Message is saved to msg.txt file...\n")
    
    elif choice == "2": #Decryption
        
        print(">>>Decryption<<<")
        with open("cipher.txt", "r") as f: #Openning the msg2.txt file
            message = f.read() #msg.txt file as a value for variable message
        shift = input("Decryption Key: ") #Input the encryption key
        dec_msg = "" #Default value for dec_msg
        with tqdm(total=len(message), desc="Decrypting") as pbar: #Initialize the progress bar with the length of the message
            for k in range(len(shift)):
                shft = shift[k]
            for i in range(len(message)): #Counting the length of the entered message
                time.sleep(0.01)
                msg_shft = message[i]
                dec_msg += chr(ord(msg_shft) ^ ord(shft))  #Getting the ASCII value of msg_shft and shft and converting it to a character
                pbar.update(1) #Increment the progress bar
                
        print("Decrypted Message is: " + dec_msg ) #Print the decrypted message
