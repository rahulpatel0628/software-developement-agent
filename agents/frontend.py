from pydantic import BaseModel
from typing import Dict
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from tools.file_tool import write_file

class FrontendOutput(BaseModel):
    files: Dict[str, str]

PROMPT_PATH = Path("prompts/frontend.txt")


def load_prompt():
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()


def frontend_node(state):

    try:
        architecture = state.get("architecture",{})
        review_report = state.get("review_report",{})
        testing_report = state.get("testing_report",{})

        llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

        prompt = ChatPromptTemplate.from_template(load_prompt())

        chain = (prompt|llm.with_structured_output(FrontendOutput))

        response = chain.invoke({"architecture": architecture,
                                 "review_report":review_report,
                                 "testing_report":testing_report
                                 })

        generated_files = []

        for filename, content in response.files.items():

            file_path = (f"generated/frontend/{filename}")

            write_file(file_path=file_path,content=content)

            generated_files.append(file_path)

        
        return {"frontend_code": response.files,
                "generated_files_frontend":generated_files
                }

    except Exception as e:

        import traceback

        print("\nFULL ERROR:")
        print(traceback.format_exc())

        return {
            "frontend_code": {
                "error": str(e)
            }
        }