# Imports
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.console import Console
from time import sleep
import os
import platform
import sys

# Console Def:
cons = Console()

# Title Def:
Title=Text(justify="center")
Title.append("Encrypt" , style="bold underline cyan1")
Title.append(" and " , style="italic dark_orange3")
Title.append("Decrypt" , style="bold underline green3")
Title.append(":" , style="bold bright_white")

# Menu Def:
menu = Text(justify="center")
menu.append("\n>> Encrypt                                       :e" , style="bold cyan1")
menu.append("\n>> Decrpyt                                       :d" , style="bold green3")
menu.append("\n>> Refresh Screen                                :r" , style="bold dark_orange3")
menu.append("\n>> Exit                                          :x" , style="bold magenta3")

# Crypt Def:
C_def= [("a","l") , ("b","U") , ("c","L") , ("d","c") , ("e","O") , ("f","C") , ("g","T") , ("h","u") , ("i","t") , ("j","l.") , ("k","U.") , ("l","L.") , ("m","c.") , ("n","O.") , ("o","C.") , ("p","T.") , ("q","u.") , ("r","t.") , ("s","V") , ("t",">") , ("u","v") , ("v","<") , ("w","V.") , ("x",">.") , ("y","v.") , ("z","<.") , (" ","Z") , (".","X") , (">","rt") , ("<","ef")]

#def cls(): # Use this block to Refresh Screen if the other bolck doesn't work
#    sys.stdout.wirte('\330[2J\330[H')
#    sys.stdout.flush()

def cls(): # Refresh Screen Block
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    elif os_name == "Linux" or os_name == "Darwin":
        os.system('clear')
    else:
        print("[bold bright_red]Clear Screen Function is not Supported for ur OS[/bold bright_red]")

def ptl(): # Print Title Block
    print(Panel(Title,box=box.ASCII))

def rst(): # Restart Program Block
    with cons.status("[italic dark_orange3]Restarting Program...[/italic dark_orange3]" , spinner = "line" , spinner_style="gold3") as status:
        sleep(3)

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
    if len(text) <= 100:
        slt=len(text)/10
    else:
        slt=10+len(text)/10
    with cons.status("[italic cyan1]Encrypting...[/italic cyan1]" , spinner = "point" , spinner_style="gold3") as status:
        sleep(slt)
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
    if len(text) <= 100:
        slt=len(text)/10
    else:
        slt=10+len(text)/10
    with cons.status("[italic green3]Decrypting...[/italic green3]" , spinner = "point" , spinner_style="gold3") as status:
        sleep(slt)
    return decrypted_text



if __name__== "__main__": # Main Block (Get User Inputs)
    choice=""
    cls()
    ptl()
    while choice != "x":
        if choice == "":
            print("\n")
            print(Panel(menu, title="Menu:", box=box.DOUBLE))  
            choice= (Prompt.ask("\n[italic]Choice?[/italic]")).lower()
        elif choice == "e":
            text = input("\nEnter text to encrypt: ")
            encrypted_text = encrypt(C_def, text.lower())
            print("\n")
            print(Panel.fit(f"Encrypted text: {encrypted_text}"))
            choice=""
        elif choice == "d":
            text = input("\nEnter text to decrypt: ")
            decrypted_text = decrypt(C_def, text)
            print("\n")
            print(Panel.fit(f"Decrypted text: {decrypted_text}"))
            choice=""
        elif choice == "r":
            rst()
            cls()
            ptl()
            choice=""
        else:
            print("[bold bright_red]Invalid choice! Please try again.[/bold bright_red]")
            rst()
            cls()
            ptl()
            choice=""
    else:
        cls()
        with cons.status("[italic magenta3]Exiting...[/italic magenta3]" , spinner = "line"  , spinner_style="gold3") as status:
            sleep(2)
            sys.exit()
