from typing import TypedDict


class SoftwareState(TypedDict):
    user_requirement: str

    architecture: dict

    backend_plan: dict

    backend_code: dict

    generated_files: list[str]

    review_report: dict

    review_iterations: int

    testing_report: dict

    test_iterations: int