class StoryException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Story with name {self.name} already exists."