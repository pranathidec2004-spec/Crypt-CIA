from main import caesar_cipher, get_sha256_hash

def run_round_trip_test():
    test_message = "SecureData2026"
    shift_key = 8
    print(f"--- Starting Round-Trip Test ---")
    print(f"Input Message: {test_message}")
    encrypted = caesar_cipher(test_message, shift_key, mode='e')
    print(f"1. Encrypted:   {encrypted}")
    cipher_hash = get_sha256_hash(encrypted)
    print(f"2. Cipher Hash: {cipher_hash}")
    decrypted = caesar_cipher(encrypted, shift_key, mode='d')
    print(f"3. Decrypted:   {decrypted}")
    if test_message == decrypted:
        print("\nSUCCESS: Round-trip complete. Original message recovered.")
    else:
        print("\nFAILURE: Decrypted message does not match original.")

if __name__ == "__main__":
    run_round_trip_test()