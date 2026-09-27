from src.data_manager import get_cases
from src.exceptions import CaseNotFoundError

def view_cases():
    
    cases = get_cases()

    print("\n╔══════════════════════════════════════╗")
    print("║             ACTIVE CASES             ║")
    print("╚══════════════════════════════════════╝")

    if not cases:
        print("\n❌ No cases available.")
        return

    for case in cases:
        print(f"\nCASE #{case['case_id']}")
        print(f"Title: {case['title']}")
        print(f"Location: {case['location']}")
        print(f"Status: {case['status']}")
        print("-" * 38)

def select_case():
    cases = get_cases()

    if not cases:
        raise CaseNotFoundError("No cases are available.")

    choice = input("\nEnter the case number you want to investigate: ")

    try:
        choice = int(choice)
    except ValueError:
        print("\n❌ Please enter a valid case number.")
        return None

    for case in cases:
        if case["case_id"] == choice:
            return case

    raise CaseNotFoundError(f"Case #{choice} was not found.")