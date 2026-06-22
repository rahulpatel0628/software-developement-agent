from dotenv import load_dotenv
from graphs.workflow import build_graph
load_dotenv()
def main():
    graph = build_graph()

    requirement = input("\nEnter project requirement:\n> ")

    result = graph.invoke({ "user_requirement": requirement})

    architecture = result.get("architecture",{})
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

    print("\n" + "=" * 60)

    backend_code = result.get("backend_code",{})

    print("\n" + "=" * 60)
    print("BACKEND FILES")
    print("=" * 60)

    for filename, content in backend_code.items():

        print(f"\n\n{filename}")
        print("-" * 60)

        if isinstance(content, str):
            print(content[:1000])
            
    generated_files = result.get("generated_files",[])

    print("\n" + "=" * 60)
    print("GENERATED FILES")
    print("=" * 60)

    for file in generated_files:
        print(file)


if __name__ == "__main__":
    main()