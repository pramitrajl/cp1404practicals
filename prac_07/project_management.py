"""Estimated: 40 mins
Actual : 1 30 mins"""


from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    """ Display menu and perform respective functions """
    print("Welcome to Pythonic Project Management")
    projects = load_project(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_project(filename)
        elif choice == "S":
            filename = input("Enter filename: ")
            save_project(filename, projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            new_project = add_project()
            projects.append(new_project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").upper()
    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save in ["yes", "y"]:
        save_project(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_project(filename):
    """ Load data from filename """
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            if line.strip():
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                    projects.append(project)
    return projects

def save_project(filename, projects):
    """ Save projects into a file """
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_est}\t{project.completion_percent}\n")

def display_project(projects):
    """ Display the projects """
    print("Incomplete projects:")
    incomplete = [p for p in projects if p.completion_percent < 100]
    for project in sorted(incomplete):
        print(project)

    print("Complete projects:")
    complete = [p for p in projects if p.completion_percent == 100]
    for project in sorted(complete):
        print(project)

def filter_project(projects):
    """ Fileter out the project as per input """
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%y").date()
        filtered = sorted([project for project in projects if project.start_date > filter_date], key=lambda project: project.start_date)
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date format. Please enter as dd/mm/yy.")

def add_project():
    """ Add new project """
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    percent_completion = int(input("Percent complete: "))
    return Project(name, date, priority, cost, percent_completion)

def update_project(projects):
    """ Make changes to project """
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_percent = input("New Percentage: ")
        if new_percent:
            project.completion_percent = int(new_percent)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid project choice.")

if __name__ == "__main__":
    main()
