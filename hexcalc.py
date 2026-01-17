#easy hex conversion

def hex_calculator():
    print("Hex<-> Decimal Calculator")
    print("1. Decimal to Hex")
    print("2. Hex to Decimal")
    
    choice = input("Choose (1 or 2): ").strip()
    
    if choice == "1":
        dec = input("Enter a decimal integer: ").strip()
        try:
            n = int(dec)
            print("Hex:", hex(n))
        except ValueError:
            print("Invalid decimal number.")
            
    elif choice == "2":
        hx = input("Enter a hex value with or witbout 0x").strip()
        try:
            n = int(hx, 16)
            print("Decimal: ", n)
        except ValueError:
                print("Invalid hex value")
                
    else:
        print("Invalid choice")
                
if __name__ == "__main__":
    hex_calculator()
                
