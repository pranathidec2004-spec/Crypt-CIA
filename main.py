import hashlib

def caesar_cipher(text, shift, mode='e'):
    result = ""
    if mode == 'd':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

def get_sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    print("Caesar Cipher")
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter shift key (integer): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    encrypted = caesar_cipher(message, shift, mode='e')
    decrypted = caesar_cipher(encrypted, shift, mode='d')
    message_hash = get_sha256_hash(message)

    print("\n--- Results ---")
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"SHA-256 Hash: {message_hash}")

if __name__ == "__main__":
    main()