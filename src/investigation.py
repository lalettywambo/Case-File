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
            print("\n Returning...")
            break

        else:
            print("\n❌ Invalid choice.")


def view_suspects(case):
    print("\n SUSPECTS")
    print("=" * 40)

    for suspect in case["suspects"]:
        print(f"\nName: {suspect['name']}")
        print(f"Role: {suspect['role']}")
        print(f"Statement: {suspect['statement']}")

    input("\nPress Enter to return to the investigation menu...")


def view_evidence(case):
    print("\n EVIDENCE")
    print("=" * 40)

    for evidence in case["evidence"]:
        print(f"\nEvidence #{evidence['id']}")
        print(f"Description: {evidence['description']}")
        print(f"Found at: {evidence['location']}")

    input("\nPress Enter to return to the investigation menu...")


def interview_witnesses(case):
    print("\n WITNESSES")
    print("=" * 40)

    for witness in case["witnesses"]:
        print(f"\nWitness: {witness['name']}")
        print(f"Statement: {witness['statement']}")

    input("\nPress Enter to return to the investigation menu...")


def submit_theory(case):
    print("\n SUBMIT YOUR THEORY")
    print("=" * 40)

    print("\nWho do you believe is responsible?")

    for index, suspect in enumerate(case["suspects"], start=1):
        print(f"{index}. {suspect['name']}")

    choice = input("\nEnter suspect number: ")

    try:
        choice = int(choice)

        if choice < 1 or choice > len(case["suspects"]):
            print("\n❌ Invalid suspect number.")
            return

        selected_suspect = case["suspects"][choice - 1]

        print(f"\nYour theory: {selected_suspect['name']}")

        print("\n Theory submitted for review.")

    except ValueError:
        print("\n❌ Please enter a number.")