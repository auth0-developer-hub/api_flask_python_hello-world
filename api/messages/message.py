class Message:
    def __init__(self, text):
        self.text = text
        self.metadata = vars(Metadata())

class Metadata:
    def __init__(self):
        self.api = "api_flask_python_hello-world"
        self.branch = "basic-role-based-access-control"
