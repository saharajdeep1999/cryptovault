from utils import caesar_encrypt, caesar_decrypt, aes_encrypt, aes_decrypt
import sys

def display_menu():
    print("""
=====================
   🔐 CryptoVault
=====================
1. Caesar Encrypt
2. Caesar Decrypt
3. AES Encrypt
4. AES Decrypt
5. Exit
""")

def get_input(prompt):
    return input(prompt).strip()

if __name__ == "__main__":
    while True:
        display_menu()
        choice = get_input("Enter your choice: ")

        if choice == "1":
            msg = get_input("Message: ")
            shift = int(get_input("Shift: "))
            print("Encrypted:", caesar_encrypt(msg, shift))

        elif choice == "2":
            msg = get_input("Encrypted Message: ")
            shift = int(get_input("Shift: "))
            print("Decrypted:", caesar_decrypt(msg, shift))

        elif choice == "3":
            msg = get_input("Message: ")
            key = get_input("16-byte Key (e.g., 1234567890abcdef): ")
            if len(key) != 16:
                print("Key must be exactly 16 bytes!")
            else:
                print("Encrypted:", aes_encrypt(msg, key))

        elif choice == "4":
            ciphertext = get_input("Encrypted Message: ")
            key = get_input("16-byte Key: ")
            try:
                print("Decrypted:", aes_decrypt(ciphertext, key))
            except Exception as e:
                print("Failed to decrypt:", str(e))

        elif choice == "5":
            print("Exiting. Stay safe!")
            sys.exit()

        else:
            print("Invalid option. Try again.")
