from src.models import Detective
from src.data_manager import save_detective, get_detectives


def register_detective():
    print("\n CREATE DETECTIVE ACCOUNT")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")

    detective = Detective(name, email, password)

    save_detective(detective)

    print("\n Detective account created successfully!")

    return detective


def login_detective():
    print("\n DETECTIVE LOGIN")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    detectives = get_detectives()

    for detective in detectives:
        if detective["email"] == email and detective["password"] == password:
            print(f"\n Welcome back, Detective {detective['name']}!")
            return Detective(
                detective["name"],
                detective["email"],
                detective["password"]
            )

    print("\n❌ Incorrect email or password.")
    return None