#import Libraries
from pathlib import Path
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from state.state import SoftwareState
from pydantic import BaseModel
from typing import Dict
from tools.file_tool import write_file

#structured output
class BackendOutput(BaseModel):
    files: Dict[str, str]

#load prompt
PROMPT_PATH = Path("prompts/backend.txt")
def load_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()


def backend_node(state: SoftwareState) -> dict:
    try:
        architecture = state.get("architecture", {})
        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        structured_llm = llm.with_structured_output(BackendOutput)

        chain = prompt | structured_llm

        response = chain.invoke({"architecture": architecture})

        generated_files = []

        for filename, content in response.files.items():

            file_path = f"generated/backend/{filename}"

            write_file(file_path=file_path,content=content)
            generated_files.append(file_path )
            
        return {
            "backend_code": response.files,
            "generated_files": generated_files
            }
            

    except Exception as e:
        
        import traceback

        print("\nFULL ERROR:")
        print(traceback.format_exc())

        return {
            "backend_code": {
                "error": str(e)
            }
        }