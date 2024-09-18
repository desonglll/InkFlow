class Result:
    """
    Represents the result of an operation.

    Attributes:
        status (int): The status of the result.
        message (str): The message associated with the result.
        data (Any, optional): Additional data related to the result. Defaults to None.
    """

    def __init__(self, status: int, message: str, data=None):
        """
        Initializes a new Result instance.

        Args:
            status (int): The status of the result.
            message (str): The message associated with the result.
            data (Any, optional): Additional data related to the result. Defaults to None.
        """
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        """
        Converts the Result instance to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representation of the Result.
        """
        return {
            'status': self.status,
            'message': self.message,
            'data': self.data,
        }
