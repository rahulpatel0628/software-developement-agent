from pydantic import BaseModel
from typing import List,Dict
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state.state import SoftwareState

class BackendPlan(BaseModel):
    framework: str
    required_files: List[str]

PROMPT_PATH = Path("prompts/backend_planner.txt")


def load_prompt() -> str:
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()


def backend_planner_node(state: SoftwareState) -> dict:

    try:

        architecture = state.get("architecture",{})

        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        structured_llm = llm.with_structured_output(BackendPlan)

        chain = prompt | structured_llm

        response = chain.invoke({"architecture": architecture})

        return {"backend_plan": response.model_dump()}

    except Exception as e:

        import traceback

        print(traceback.format_exc())

        return {
            "backend_plan": {
                "error": str(e)
            }
        }