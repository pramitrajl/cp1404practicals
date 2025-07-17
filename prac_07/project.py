class Project:

    def __init__(self, name, start_date, priority, cost_est, competition_percent):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_est = cost_est
        self.competition_percent = competition_percent

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_est}, competition: {self.competition_percent}"

    def __gt__(self, other):
        return self.priority > other.priority