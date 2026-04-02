# Crypt-CIA
CAESAR CIPHER:

It is a monoalphabetic cipher than works by shifting the letters present in the plain text by the given key to produce cypher text. Decryption works the same way but it shifts the letters in the cypher text in the opposite direction of that of the encryption.

For example: Plain text -> A (0)
Key -> 3 (0+3=3)
Cypher text -> D (3)
Decryption:
Cypher text -> D (3)
Key -> 3 ( 3-3 = 0)
Plain text -> A (0)
So we can derive the encryption and decryption formula from this
E (n) = ( P + K) mod 26
D (n) = (C - K ) mod 26

POLYNOMIAL ROLLING HASH:

I chose the Polynomial Rolling Hash because it is a robust, linear-time algorithm that can be implemented entirely from scratch using only basic arithmetic operators. It satisfies the requirement of avoiding built-in cryptography libraries while providing a high degree of uniqueness for string inputs.
It works by not just simply having the sum of the letters but multiplying each letter by its respective weight. If we just take the sum then it will give us the same sum for words like 'ACT' and 'CAT'.

The formula is -> H = ( s[0] . P^0 + S[1] . P^1...)

INSTRUCTIONS:
Here are the instructions on how to run the files.
1. Create the main.py file.
2. Create the test_script.py file by importing caeser and hash from the main file.
3. Run both the files on command prompt and check for the output.
4. To run the command we use is : python main.py
   python test_script.py

OUTPUTS:
<img width="804" height="440" alt="image" src="https://github.com/user-attachments/assets/1f5ac53a-0832-46af-ba2b-83e4fad0fc65" />
<img width="823" height="129" alt="image" src="https://github.com/user-attachments/assets/f482d743-7931-4d05-a7c9-be421a5dca7b" />


