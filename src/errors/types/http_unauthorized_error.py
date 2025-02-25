class UnauthorizedError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.title = 'UnauthorizedError'
        self.status_code = 401