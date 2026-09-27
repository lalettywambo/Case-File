from src.authentication import register_detective, login_detective
from src.cases import view_cases, select_case
from src.investigation import investigate_case


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

selected_case = select_case()

if selected_case:
    print("\n CASE SELECTED")
    print("--------------------")
    print(f"Case #{selected_case['case_id']}")
    print(f"Title: {selected_case['title']}")
    print(f"Location: {selected_case['location']}")
    print(f"Status: {selected_case['status']}")

    investigate_case(selected_case)

else:
     print("\n❌ Invalid choice.")