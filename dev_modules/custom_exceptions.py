class CustomError(Exception):
    """Exception raised for custom error in the application."""
    # ATT this function doesn't accept printf for the message arg; a printf string needs to be assigned to a var
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
