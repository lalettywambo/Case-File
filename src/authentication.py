from src.models import Detective
from src.data_manager import save_detective, get_detectives


def register_detective():
    print("\nCREATE DETECTIVE ACCOUNT")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")

    detective = Detective(name, email, password)

    save_detective(detective)

    print("\nDetective account created successfully!")

    return detective


def login_detective():
    print("\nDETECTIVE LOGIN")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    detectives = get_detectives()

    for detective in detectives:
        if detective["email"] == email and detective["password"] == password:
            print(f"\nWelcome back, Detective {detective['name']}!")
            return Detective(
                detective["name"],
                detective["email"],
                detective["password"]
            )

    print("\nIncorrect email or password.")
    return None