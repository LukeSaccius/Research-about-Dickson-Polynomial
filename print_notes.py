
def print_research_notes():
    """
    Reads and prints the content of the research_notes.md file.
    """
    try:
        with open("research_notes.md", "r") as f:
            notes = f.read()
            print(notes)
    except FileNotFoundError:
        print("Error: research_notes.md not found.")

if __name__ == "__main__":
    print_research_notes()
