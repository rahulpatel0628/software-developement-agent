from pydantic import BaseModel
from typing import List
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state.state import SoftwareState
from tools.file_tool import read_directory

class TestingOutput(BaseModel):
    passed: bool
    score: int
    issues: List[str]
    test_files: List[str]

PROMPT_PATH = Path("prompts/tester.txt")
def load_prompt():
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()


def tester_node(state: SoftwareState):

    try:

        files = read_directory("generated/backend")

        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        chain = (prompt|llm.with_structured_output(TestingOutput))

        response = chain.invoke({"files": files})

        return {"testing_report":response.model_dump()}

    except Exception as e:

        import traceback

        print(traceback.format_exc())

        return {
            "testing_report": {
                "error": str(e)
            }
        }