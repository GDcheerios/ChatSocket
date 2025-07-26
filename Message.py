import json
import datetime as dt


class Message:
    id: int = 0

    def __init__(self, content, author=None, time=None, id=None):
        if id is not None:
            self.id = id
        else:
            Message.id += 1
            self.id = Message.id

        self.content = content
        self.author = str(author) if author is not None else "Anonymous"
        self.time = time if time is not None else str(dt.datetime.now())

    def __str__(self):
        return f"{self.author} | {str(self.time)}\n {self.content}"

    def __repr__(self):
        return f"Message({self.id}, {self.author}, {self.time}, {self.content})"

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Message(data["content"], data["author"], data["time"], data["id"])
