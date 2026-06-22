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


if __name__ == "__main__":
    main()