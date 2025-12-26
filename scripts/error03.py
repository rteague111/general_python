import logging

#setup logging (errors will be saved to errors1.log)
logging.basicConfig(
    filename="errors1.log",
    level=logging.ERROR,
    format="%(acstime)s - %(levelname)s - %(message)s"
)

#defining class for the choice menu; the numbers represent user choice

def error_playground():
    while True:
        print("\nChoose an action: ")
        print("1. Divide numbers")
        print("2. Open a File")
        print("3. Look up a Dictionary Key")
        print("4. Enter your age")
        print("5. Quit")

        choice = input("Enter your Choice:") #user input here
#try logic for the choice tree and yes its nested
        try:
            if choice == "1":
                a = int(input("Enter a numerator: "))
                b = int(input("Enter a denominator: "))
                result = a/b
                print(f"Result: {result}")

            elif choice == "2":
                filename = input("Enter a filename: ")
                with open(filename, "r") as f:
                    print(f.read())

            elif choice == "3":
                d = {"name": "Fred", "language": "Python"}
                key = input("Enter the key to look up: ")
                print(f"Value {f[key]}")

            elif choice == "4":
                while True:
                    try:
                        age = int(input("Enter your age: "))
                        print(f"You are {age} years old.")
                        break
                    except ValueError:
                        print("Oops! That wasn't a number! Try again!") # here is the first of the error handling

            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice!") # more error handling, if nothing else or any other value than 1-5 this prints
        
        # Further exception handling and their error logs printed in log file
        except ValueError:
            print("That wasn't a valid number.")
            logging.error("ValueError: Invalid number entered. ")
        except ZeroDivisionError:
            print("You can't divide by zero!")
            logging.error("ZeroDivisonError: Tried dividing by zero.")
        except FileNotFoundError as e:
            print("That file doesn't exist.")
            logging.error(f"FileNotFoundError: {e}")
        except KeyError as e:
            print(f"KeyError! The dictionary has no key: {e}")
            logging.error(f"KeyError: Missing key {e}")

#run the playground
if __name__ == "__main__":
    error_playground()