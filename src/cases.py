from src.data_manager import get_cases


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