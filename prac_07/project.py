class Project:

    def __init__(self, name, start_date, priority, cost_est, completion_percent):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_est = cost_est
        self.completion_percent = float(completion_percent)

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_est}, competition: {self.completion_percent}%"

    def __gt__(self, other):
        return self.priority > other.priority