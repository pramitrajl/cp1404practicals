from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():

    print("Welcome to Pythonic Project Management")
    #loading message
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        """if choice == "L":
            load_project() """
        """elif choice == "S":
            save_project()"""
        """elif choice == "D":
            display_project()"""
        """ elif choice == "F":
            filter_project()"""
        """elif choice== "A":
            add_project()"""
        """elif choice == "U":
            update_project()"""
        """else:
            print("Invalid")
            choice = input(">>>").upper()"""

def load_project():
    projects = []
    with open ("projects.txt", 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0],parts[1],parts[2],parts[3],parts[4])
            projects.append(project)
        projects.sort()
        for project in projects:
            print(project)

load_project()
