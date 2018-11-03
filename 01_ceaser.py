
decrypted = b"abcdefghijklmnopqrstuvwxyz"
encrypted = b"ithadbeenaterriblehorrible"

encrypt_table=bytes.maketrans(decrypted,encrypted)
decrypt_table=bytes.maketrans(encrypted,decrypted)

result=''
message=''
choice=''

while choice !='0':

              choice=input("\n Do you want to encrypt or decrypt your message? \n 1 to encrypt 2 to decrypt 0 to exit")

                  if choice == '1':
       		    message = input('\n Enter message for encryption: ')
       		    result = message.translate(encrypt_table)
       		    print(result + '\n\n')

                  elif choice == '2':
	            message=input('\n Enter message to decryption:')
	            result=message.translate(decrypt_table)
	            print(result + '\n\n')

                  elif choice !== '0':
	            print('you have entered an invalid input.\n\n')
