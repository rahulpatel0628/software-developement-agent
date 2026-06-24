from graphs.workflow import build_graph
from dotenv import load_dotenv
load_dotenv()

def print_architecture(architecture: dict):
    print("\n" + "=" * 60)
    print("ARCHITECTURE PLAN")
    print("=" * 60)

    for key, value in architecture.items():

        print(f"\n{key.upper()}")

        if isinstance(value, list):

            for item in value:
                print(f"  • {item}")

        else:
            print(value)

def print_backend_files(backend_code: dict):

    print("\n" + "=" * 60)
    print("BACKEND FILES")
    print("=" * 60)

    if "error" in backend_code:

        print("\nerror")
        print("-" * 60)
        print(backend_code["error"])

        return

    for filename, content in backend_code.items():

        print(f"\n{filename}")
        print("-" * 60)

        print(content[:1000])

        if len(content) > 1000:
            print("\n...truncated...")

def print_frontend_files(frontend_code: dict):

    print("\n" + "=" * 60)
    print("FRONTEND FILES")
    print("=" * 60)

    if "error" in frontend_code:

        print("\nerror")
        print("-" * 60)
        print(frontend_code["error"])

        return

    for filename, content in frontend_code.items():

        print(f"\n{filename}")
        print("-" * 60)

        print(content[:1000])

        if len(content) > 1000:
            print("\n...truncated...")
    

def print_generated_files_backend(generated_files_backend: list):


    print("\n" + "=" * 60)
    print("GENERATED FILES")
    print("=" * 60)

    for file in generated_files_backend:
        print(file)

def print_generated_files_frontend(generated_files_frontend: list):


    print("\n" + "=" * 60)
    print("GENERATED FILES")
    print("=" * 60)

    for file in generated_files_frontend:
        print(file)

def print_review(review_report: dict):
    print("\n" + "=" * 60)
    print("CODE REVIEW")
    print("=" * 60)

    if not review_report:
        print("No review report available.")
        return

    print(f"\nScore: {review_report.get('score', 'N/A')}/10")

    print("\nIssues:")

    for issue in review_report.get("issues",[]):
        print(f"  • {issue}")

    print("\nSuggestions:")

    for suggestion in review_report.get("suggestions",[]):
        print(f"  • {suggestion}")

def print_testing(testing_report: dict):
    print("\n" + "=" * 60)
    print("TEST REPORT")
    print("=" * 60)

    print("Frontend Score:",testing_report.get("frontend_score",0))

    print("\nFrontend Issues:")

    for issue in testing_report.get("frontend_issues",[]):
        print(f"  • {issue}")
        
    print("Backend Score:",testing_report.get("backend_score",0))

    print("\nBackend Issues:")

    for issue in testing_report.get("backend_issues",[]):
        print(f"  • {issue}")

def main():
    requirement = input("Enter project requirement:\n> ")
    graph = build_graph()

    result = graph.invoke({"user_requirement": requirement,"review_iterations": 0})

    architecture = result.get("architecture",{})

    backend_code = result.get("backend_code",{})

    frontend_code = result.get("frontend_code",{})

    generated_files_backend = result.get("generated_files_backend",[])
    
    generated_files_frontend = result.get("generated_files_frontend",[])

    review_report = result.get("review_report",{})

    testing_report = result.get("testing_report",{})

    print_architecture(architecture)

    print_backend_files(backend_code)

    print_generated_files_backend(generated_files_backend)

    print_frontend_files(frontend_code)

    print_generated_files_frontend(generated_files_frontend)

    print_review(review_report)

    print("\nReview Iterations:",result.get("review_iterations",0))

    print_testing(testing_report)
    
if __name__ == "__main__":
    main()