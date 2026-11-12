import string

def caesar_cipher(message, shift, mode):
    letters = string.ascii_lowercase
    result_message = ""

    for letter in message:
        if letter.lower() in letters:
            original_position = letters.index(letter.lower())
            
            if mode == "encrypt":
                new_position = (original_position + shift) % 26
            else:
                new_position = (original_position - shift) % 26
                
            new_letter = letters[new_position]
            
            if letter.isupper():
                new_letter = new_letter.upper()
                
            result_message += new_letter
        else:
            result_message += letter
            
    return result_message

print("=== Caesar Cipher Tool ===")

while True:
    print("\n----------------------------------------")
    choice = input("Do you want to (encrypt), (decrypt), or type (exit, q) to quit? ").strip().lower()

    if choice == "exit" or choice == "q":
        print("Goodbye! Keep coding! 🚀")
        break

    if choice == "encrypt" or choice == "1":
        user_message = input("Enter the message to encrypt: ")
        user_shift = int(input("Enter the shift number: "))
        result = caesar_cipher(user_message, user_shift, mode="encrypt")
        print(f"\nEncrypted Message:\n*\n{result}\n*")
        break
    elif choice == "decrypt" or choice == "2":
        user_message = input("Enter the message to decrypt: ")
        user_shift = int(input("Enter the shift number: "))
        result = caesar_cipher(user_message, user_shift, mode="decrypt")
        print(f"\nDecrypted Message:\n*\n{result}\n*")
        break
    else:
        print("❌ Invalid choice! Please type 'encrypt', 'decrypt', or 'exit'.")
        continue  