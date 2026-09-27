class CaseFileError(Exception):
    """Base exception for CASEFILE."""


class CaseNotFoundError(CaseFileError):
    """Raised when a requested case does not exist."""


class InvalidChoiceError(CaseFileError):
    """Raised when the detective enters an invalid menu choice."""