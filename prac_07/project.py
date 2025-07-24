"""Estimated: 10 mins
Actual: 19 mins """
import datetime

class Project:
    """Represent Project objects """
    def __init__(self, name, start_date, priority, cost_est, completion_percent):
        """ Initialize instances  """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date() if isinstance(start_date,str) else start_date
        self.priority = int(priority)
        self.cost_est = float(cost_est)
        self.completion_percent = float(completion_percent)

    def __str__(self):
        """ Return string representation """
        return f"\t{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_est}, completion: {self.completion_percent}%"

    def __gt__(self, other):
        """ Return true if self priority is greater than other priority """
        return self.priority >  other.priority