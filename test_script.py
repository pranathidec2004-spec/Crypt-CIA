from main import cipher, hasher

def run_test():
    msg = "Test2026"
    k = 8
    
    enc = cipher(msg, k, 'e')
    hsh = hasher(enc)
    dec = cipher(enc, k, 'd')
    
    print(f"Input: {msg}")
    print(f"1. Encrypt: {enc}")
    print(f"2. Hash: {hsh}")
    print(f"3. Decrypt: {dec}")
    
    if msg == dec:
        print("Result: Success")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    run_test()