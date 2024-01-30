# text = 'mrttaqrhknsw ih puggrur'
# custom_key = 'python'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# print(f'\nEncrypted text: {text}')
# print(f'Key: {custom_key}')
# decryption = decrypt(text, custom_key)
# print(f'\nDecrypted text: {decryption}\n')
def main():
    print("For encryption press 'enc'\nfor decrypt press 'dec'")
    todo = input("= ")
    if todo == "enc":
        msg = input("Enter your message : ")
        key = input("Enter your key: ")
        encrpted_text = encrypt(msg,key)
        print(encrpted_text)
    elif todo == "dec":
        msg = input("Enter your message : ")
        key = input("Enter your key: ")
        decrypted_text = decrypt(msg,key)
        print(decrypted_text)
    else:
        print("Please check your inputs")
if __name__ == "__main__":
    main()