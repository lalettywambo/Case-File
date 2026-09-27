from src.data_manager import save_record
from src.models import EvidenceItem, WitnessItem


def investigate_case(case):
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║          INVESTIGATION MENU          ║")
        print("╚══════════════════════════════════════╝")

        print(f"\nCASE #{case['case_id']}: {case['title']}")
        print("\n1.  View Suspects")
        print("2.  Examine Evidence")
        print("3.  Interview Witnesses")
        print("4.  Submit Theory")
        print("5.  Leave Investigation")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_suspects(case)

        elif choice == "2":
            view_evidence(case)

        elif choice == "3":
            interview_witnesses(case)

        elif choice == "4":
            submit_theory(case)

        elif choice == "5":
            print("\nReturning...")
            break

        else:
            print("\nInvalid choice.")


def view_suspects(case):
    print("\nSUSPECTS")
    print("=" * 40)

    for suspect in case["suspects"]:
        print(f"\nName: {suspect['name']}")
        print(f"Role: {suspect['role']}")
        print(f"Statement: {suspect['statement']}")

    input("\nPress Enter to return to the investigation menu...")


def view_evidence(case):
    print("\nEVIDENCE")
    print("=" * 40)

    for evidence in case["evidence"]:
        item = EvidenceItem(
            evidence["description"],
            evidence["location"]
        )

        item.display()

    input("\nPress Enter to return to the investigation menu...")


def interview_witnesses(case):
    print("\nWITNESSES")
    print("=" * 40)

    for witness in case["witnesses"]:
        item = WitnessItem(
            witness["name"],
            witness["statement"]
        )

        item.display()

    input("\nPress Enter to return to the investigation menu...")

def submit_theory(case):
    print("\nSUBMIT YOUR THEORY")
    print("=" * 40)

    print("\nWho do you believe is responsible?")

    for index, suspect in enumerate(case["suspects"], start=1):
        print(f"{index}. {suspect['name']}")

    choice = input("\nEnter suspect number: ")

    try:
        choice = int(choice)

        if choice < 1 or choice > len(case["suspects"]):
            print("\nInvalid suspect number.")
            return

        # The menu is numbered from 1, so shift back to a list index.
        selected_suspect = case["suspects"][choice - 1]

        print(f"\nYour theory: {selected_suspect['name']}")

        if selected_suspect["name"] == case["correct_suspect"]:
            print("\nTHEORY CORRECT!")
            print("Excellent detective work.")

            save_record(
                case,
                selected_suspect["name"],
                "Correct"
            )

        else:
            print("\nTHEORY INCORRECT.")
            print(f"The actual suspect was: {case['correct_suspect']}")

            save_record(
                case,
                selected_suspect["name"],
                "Incorrect"
            )

    except ValueError:
        print("\nPlease enter a number.")