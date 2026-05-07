# hellnced program hello.py - A program to greet multiple users

def get_names():
    """Get multiple names from the user"""
    names = []
    print("Enter names one by one (press Enter without typing a name to finish):")
    
    while True:
        name = input("Enter a name: ").strip()
        if name:  # If name is not empty
            names.append(name)
        else:  # Empty input means we're done
            break
    
    return names

def greet_names(names):
    """Greet each name in the list"""
    print("\n" + "="*30)
    print("GREETINGS:")
    print("="*30)
    for name in names:
        print(f"hello {name.title()}!")
    print("="*30)

def main():
    """Main program flow"""
    print("Welcome to the Multi-Person Greeting Program!")
    print("-" * 40)
    
    # Get multiple names
    names_list = get_names()
    
    # Check if any names were entered
    if names_list:
        print(f"\nYou entered {len(names_list)} name(s): {', '.join(names_list)}")
        greet_names(names_list)
    else:
        print("\nNo names were entered. Goodbye!")

if __name__ == "__main__":
    main()
