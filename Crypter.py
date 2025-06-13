# Imports
#import rich
#import time

# Crypt Def:
C_def= [("a","l") , ("b","U") , ("c","L") , ("d","c") , ("e","O") , ("f","C") , ("g","T") , ("h","u") , ("i","t") , ("j","l.") , ("k","U.") , ("l","L.") , ("m","c.") , ("n","O.") , ("o","C.") , ("p","T.") , ("q","u.") , ("r","t.") , ("s","V") , ("t",">") , ("u","v") , ("v","<") , ("w","V.") , ("x",">.") , ("y","v.") , ("z","<.") , (" ","Z") , (".","X") , (">","rt") , ("<","lt")]

def encrypt(C_def, text): # Encrypting Block
    encrypted_text = ""
    for char in text:
        flag=False
        for tup in C_def:
            while tup[0]==char: # Character in C_def
                encrypted_text+=tup[1]
                flag=True
                break
        if not flag:
            encrypted_text+=char # Character not in C_def
    return encrypted_text

def decrypt(C_def, text):  # Decrypt Block
    decrypted_text = ""
    i = 0
    while i < len(text):
        matched = False
        # Try to match substrings of varying lengths (longest first)
        for length in range(2, 0, -1):  # Check for 2-char, then 1-char matches
            if i + length <= len(text):
                substring = text[i:i + length]
                for tup in C_def:
                    if tup[1] == substring:  # Match found in C_def for encrypted value
                        decrypted_text += tup[0]
                        i += length
                        matched = True
                        break
            if matched:
                break
        if not matched:  # If no match is found, keep the character as is
            decrypted_text += text[i]
            i += 1
    return decrypted_text



if __name__== "__main__": # Main Block (Get User Inputs)
    choice=""
    while choice != "x":
        if choice == "":
            choice= input("\n__*Menu:*__\n\'e\' - Encrypt \n\'d\' - Decrypt \n\'x\' - Exit Loop \nChoice?: ").lower()
        elif choice == "e":
            text = input("Enter text to encrypt: ")
            encrypted_text = encrypt(C_def, text.lower())
            print(f"Encrypted text: {encrypted_text}")
            choice=""
        elif choice == "d":
            text = input("Enter text to decrypt: ")
            decrypted_text = decrypt(C_def, text)
            print(f"Decrypted text: {decrypted_text}")
            choice=""
        else:
            print("Invalid choice. Please try again.")
            choice=""
