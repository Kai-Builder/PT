import kaibuilder.servermanager


class Stream:
    def __init__(self):
        self.content = []
        self.Json = {
            "pyVENV": "./venv"
        }

    async def addcontent(self, content):
        assert isinstance(content, object)
        self.content.append(content)

