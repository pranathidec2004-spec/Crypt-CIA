def cipher(txt, s, m):
    res = ""
    if m == 'd':
        s = -s
    for c in txt:
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - start + s) % 26 + start)
        else:
            res += c
    return res

def hasher(txt):
    p, m, h, pw = 31, 10**9 + 9, 0, 1
    for c in txt:
        h = (h + ord(c) * pw) % m
        pw = (pw * p) % m
    return h

def main():
    msg = input("Message: ")
    k = int(input("Shift: "))

    enc = cipher(msg, k, 'e')
    dec = cipher(enc, k, 'd')
    hsh = hasher(msg)

    print(f"Original: {msg}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
    print(f"Hash: {hsh}")

if __name__ == "__main__":
    main()