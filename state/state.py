from typing import TypedDict

class SoftwareState(TypedDict):
    user_requirement: str
    architecture: dict
    backend_code: dict
    generated_files: list[str]
    frontend_code: dict
    review_report: dict
    review_iterations: int
    test_cases: str