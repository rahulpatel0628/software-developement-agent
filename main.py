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
    

def print_generated_files(generated_files: list):


    print("\n" + "=" * 60)
    print("GENERATED FILES")
    print("=" * 60)

    for file in generated_files:
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


def main():
    requirement = input("Enter project requirement:\n> ")
    graph = build_graph()

    result = graph.invoke({"user_requirement": requirement,"review_iterations": 0})

    architecture = result.get("architecture",{})

    backend_code = result.get("backend_code",{})

    generated_files = result.get("generated_files",[])

    review_report = result.get("review_report",{})

    print_architecture(architecture)

    print_backend_files(backend_code)

    print_generated_files(generated_files)

    print_review(review_report)

    print("\nReview Iterations:",result.get("review_iterations",0))

if __name__ == "__main__":
    main()