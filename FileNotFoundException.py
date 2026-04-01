class FileNotFoundException(Exception):
    _message: str = ""

    def __init__(self, message: str | None) -> None:
        if message is None:
            self._message = "File not found Exception"
        else:
            self._message = message
        super().__init__(self._message)

    def show_error(self) -> str:
        return self._message
