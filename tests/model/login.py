class Login:

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return "%s:%s" % (self.name, self.password)
