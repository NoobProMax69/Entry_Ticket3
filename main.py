import pickle

def display_menu():
    print("---- Menu ----")
    print("1) Add suspect")
    print("2) Add accomplice")
    print("3) Display all suspects")
    print("4) Find potential accomplices")
    print("E) Exit\n")

def display_suspect(suspect, graph):
    print(f"{suspect}:")
    accomplices = graph.get(suspect, set())
    for accomplice in accomplices:
        print(f"    {accomplice}")


def display_all_suspects(graph):
    print("---- All suspects ----")
    for suspect in graph:
        display_suspect(suspect, graph)
    print()


def find_potential_accomplices(suspect, graph):
    potential_accomplices = set()

    for accomplice in graph[suspect]:
        potential_accomplices.update(graph.get(accomplice, set()))

    potential_accomplices.discard(suspect)
    potential_accomplices.difference_update(graph[suspect])

    return {suspect: potential_accomplices}


def display_potential_accomplices(suspect, graph):
    potential_accomplices = find_potential_accomplices(suspect, graph)

    print("---- Potential accomplices ----")
    print("Already known accomplices:")
    display_suspect(suspect, graph)
    print()

    print("Potential new accomplices:")
    display_suspect(suspect, potential_accomplices)


def load_from_file(filename):
    try:
        with open(filename, "rb") as file:
            print("*** Graph loaded from file. ***")
            return pickle.load(file)
    except FileNotFoundError:
        print("*** File not found. Starting with empty graph. ***")
        return {}


def save_to_file(graph, filename):
    with open(filename, "wb") as file:
        pickle.dump(graph, file)
        print("*** Graph saved to file. ***")


def main():
    print()
    filename = input("Enter path to graph file: ")
    print()
    graph = load_from_file(filename)

    while True:
        display_menu()
        choice = input("Your choice: ").strip().upper()

        if choice == "1":
            suspect_name = input("Enter suspect name: ")
            graph[suspect_name] = set()

        elif choice == "2":
            suspect_name = input("Enter suspect name: ")
            accomplice_name = input("Enter accomplice name: ")
            if suspect_name not in graph:
                graph[suspect_name] = set()
            if accomplice_name not in graph:
                graph[accomplice_name] = set()
            graph[suspect_name].add(accomplice_name)
            graph[accomplice_name].add(suspect_name)
            save_to_file(graph, filename)

        elif choice == "3":
            display_all_suspects(graph)

        elif choice == "4":
            suspect_name = input("Enter suspect name: ")
            display_potential_accomplices(suspect_name, graph)

        elif choice == "E":
            break

if __name__ == "__main__":
    main()