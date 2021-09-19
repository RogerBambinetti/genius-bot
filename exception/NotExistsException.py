class NotExistsException(Exception):

    def __init__(self):
        super().__init__("Object Does Not Exists")
