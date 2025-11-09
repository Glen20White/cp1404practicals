from project import Project
from datetime import datetime
import csv

FILENAME = "projects.txt"

MENU = """(L) Load projects
(S) Save projects
(D) Display projects
(F) Filter projects by date
(A) Add new project
(U) Update project
(Q) Quit
"""


def main():
    print("Welcome to Pythonic Project Manager")
    projects = load_projects(FILENAME)
    print(f"{len(projects)} projects loaded from {FILENAME}")
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects.")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid selection.")
        choice = input(MENU + ">>> ").strip().upper()

    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a tab-separated file and return a list."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header line
        for line in in_file:
            clean_line = line.strip().split("\t")
            name, start_date, priority, cost_estimate, completion_percentage = clean_line
            project = Project(
                name,
                start_date,
                int(priority),
                float(cost_estimate),
                int(completion_percentage)
            )
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save all projects back to the given file."""
    is_save_projects = input("Would you like to save to project.txt (y/n)")
    if is_save_projects == "y":
        with open(filename, "w", newline='') as out_file:
            writer = csv.writer(out_file)
            for project in projects:
                writer.writerow([project.name, project.start_date, project.priority, project.cost_estimate,
                                 project.completion_percentage])
    else:
        print("Thank you for using custom-built project management software.")


def display_projects(projects):
    """Show incomplete and completed projects separately."""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100:
            print(f"  {project}")

    print("Completed projects:")
    for project in projects:
        if project.completion_percentage >= 100:
            print(f"  {project}")


def filter_by_date(projects):
    """Display projects starting on or after a given date."""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        compare_date = datetime.strptime(date_input, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [project for project in projects if datetime.strptime(project.start_date, "%d/%m/%Y") >= compare_date]
    filtered.sort(key=lambda project: datetime.strptime(project.start_date, "%d/%m/%Y"))

    for project in filtered:
        print(project)


def add_project(projects):
    """Prompt the user and create a new project."""
    print("Add a new project:")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Choose a project and change completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


main()
