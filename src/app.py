from src.authentication import register_detective, login_detective
from src.cases import view_cases


def start_casefile():
    print("\n╔══════════════════════════════════════╗")
    print("║              CASEFILE              ║")
    print("║       Investigation Console         ║")
    print("╚══════════════════════════════════════╝")

    print("\n1. Create Detective Account")
    print("2. Login")

    choice = input("\nChoose an option: ")

    if choice == "1":
        detective = register_detective()

        print("\n DETECTIVE PROFILE")
        print("--------------------")
        detective.display_profile()

    elif choice == "2":
        detective = login_detective()

        if detective:
            print("\n Login successful.")
            print(f"Welcome, Detective {detective.name}!")
            view_cases()

    else:
        print("\n❌ Invalid choice.")