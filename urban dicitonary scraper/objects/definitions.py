class Definition:
    """
    class representing a single definition and it's properties
    """

    def __init__(self, name, meaning, example, likes, dislikes):
        self.name = name
        self.meaning = meaning
        self.example = example
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self):
        return f'Name:{self.name}\nmeaning:{self.meaning}.\nexample:{self.example}.\nlikes/dislikes:{self.likes}||{self.dislikes}\n\n'

