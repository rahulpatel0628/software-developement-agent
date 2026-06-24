from pydantic import BaseModel
from typing import List
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state.state import SoftwareState

class TestingOutput(BaseModel):
    backend_score: int
    frontend_score: int

    backend_issues: List[str]
    frontend_issues: List[str]

PROMPT_PATH = Path("prompts/tester.txt")
def load_prompt():
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()


def tester_node(state: SoftwareState):

    try:

        architecture = state.get("architecture", {})
        review_report = state.get("review_report",{})
        backend_code  = state.get("backend_code",{})
        frontend_code  = state.get("frontend_code",{})

        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        chain = (prompt|llm.with_structured_output(TestingOutput))

        response = chain.invoke(
                        {
                            "architecture": architecture,
                            "backend_code": backend_code,
                            "frontend_code": frontend_code,
                            "review_report": review_report
                        }
                    )
        return {"testing_report":response.model_dump(),
                "test_iterations":state.get("test_iterations",0) + 1
                }

    except Exception as e:

        import traceback

        print(traceback.format_exc())

        return {
            "testing_report": {
                "error": str(e)
            }
        }