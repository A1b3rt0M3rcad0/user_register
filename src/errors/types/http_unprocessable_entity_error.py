class HttpUnprocessableEntityError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.status_code = 422
        self.title = "UnprocessableEntity"
        self.message = message
