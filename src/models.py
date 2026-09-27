class Detective:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_profile(self):
        print(f"Detective: {self.name}")
        print(f"Email: {self.email}")


class Suspect:
    def __init__(self, name, role, statement):
        self.name = name
        self.role = role
        self.statement = statement

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Statement: {self.statement}")


class Evidence:
    def __init__(self, evidence_id, description, location):
        self.evidence_id = evidence_id
        self.description = description
        self.location = location

    def display(self):
        print(f"Evidence #{self.evidence_id}")
        print(f"Description: {self.description}")
        print(f"Found at: {self.location}")


class Witness:
    def __init__(self, name, statement):
        self.name = name
        self.statement = statement

    def give_statement(self):
        print(f"Witness: {self.name}")
        print(f"Statement: {self.statement}")


class Case:
    def __init__(self, case_id, title, location, status):
        self.case_id = case_id
        self.title = title
        self.location = location
        self.status = status

    def display_case(self):
        print(f"Case #{self.case_id}: {self.title}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")

class InvestigationItem:
    def display(self):
        raise NotImplementedError("This method must be implemented.")


class EvidenceItem(InvestigationItem):
    def __init__(self, description, location):
        self.description = description
        self.location = location

    def display(self):
        print(f"\n Evidence: {self.description}")
        print(f"Found at: {self.location}")


class WitnessItem(InvestigationItem):
    def __init__(self, name, statement):
        self.name = name
        self.statement = statement

    def display(self):
        print(f"\n Witness: {self.name}")
        print(f"Statement: {self.statement}")