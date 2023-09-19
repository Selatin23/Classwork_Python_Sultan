class Logger:

    def __new__(cls):
        if not hasattr(cls, isinstance):
            cls.Instance = super(Logger, cls).__new__(cls)
        return cls.Instance

