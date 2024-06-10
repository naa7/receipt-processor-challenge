class AppState:
    """
    Singleton class that stores the state of the application.
    """

    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
            self._instance.receipts = {}
        return self._instance
