from typing import TypedDict


class SoftwareState(TypedDict):
    user_requirement: str

    architecture: dict

    backend_code: dict

    frontend_code: dict
    
    generated_files_backend: list[str]

    generated_files_frontend: list[str]

    review_report: dict

    review_iterations: int

    testing_report: dict

    test_iterations: int