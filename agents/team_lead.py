#Import Library
from pathlib import Path
from langchain_groq import ChatGroq
from state.state import SoftwareState
from pydantic import BaseModel
from typing import List,Dict

#Define Schemas for structured output
class ArchitecturePlan(BaseModel):
    project_name: str
    description: str
    tech_stack: List[str]
    frontend_tasks: List[str]
    backend_tasks: List[str]
    database_entities: List[str]
    api_endpoints: List[str]
    folder_structure: List[str]
    authentication_strategy: str
    database_design: Dict[str, List[str]]
    deployment_strategy: str

#load prompt
PROMPT_PATH = Path("prompts/team_lead.txt")
def load_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()

#build team-lead node
def team_lead_node(state: SoftwareState) -> dict:

    try:
        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt_template = load_prompt()

        prompt = prompt_template.format(requirement=state["user_requirement"])

        structured_llm = llm.with_structured_output(ArchitecturePlan)

        architecture = structured_llm.invoke(prompt)

        return {"architecture": architecture.model_dump()}

    except Exception as e:
        return {
            "architecture": {
                "error": str(e)
            }
        }