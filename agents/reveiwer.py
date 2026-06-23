from pydantic import BaseModel
from typing import List
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state.state import SoftwareState
from tools.file_tool import read_directory

class ReviewOutput(BaseModel):
    issues: List[str]
    suggestions: List[str]
    score: int

PROMPT_PATH = Path("prompts/reviewer.txt")
def load_prompt() -> str:
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()


def reviewer_node(state: SoftwareState) -> dict:

    try:

        files = read_directory("generated/backend")
        #print(files)
        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        structured_llm = llm.with_structured_output(ReviewOutput)

        chain = prompt | structured_llm

        review = chain.invoke({"files": files})
        
        return {"review_report": review.model_dump(),
                "review_iterations":state.get("review_iterations",0) + 1
                }

    except Exception as e:

        import traceback
        print(traceback.format_exc())
        return {"review_report": {"error": str(e)}}