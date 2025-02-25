class BadRequestError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.title = 'BadRequest'
        self.status_code = 400