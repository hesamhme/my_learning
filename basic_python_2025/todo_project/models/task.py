import csv
import os

class Task:
    """
    A class to represent a single task.
    """
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"[{self.priority}] {self.name} - {self.description}"

    def to_dict(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Priority': self.priority
        }

    @staticmethod
    def from_dict(data):
        return Task(data['Name'], data['Description'], data['Priority'])
