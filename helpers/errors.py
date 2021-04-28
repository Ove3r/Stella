class Error(Exception):
    pass

class PlayerNotFound(Error):
    pass

class ItemNotFound(Error):
    pass

class ProfileNotFound(Error):
    pass

class DisabledAPI(Error):
    pass

class GuildNotFound(Error):
    pass

class LocationError(Error):
    pass

class APIResponseError(Error):
    def __init__(self, code=0):
        super().__init__()
        self.code = code

class NoProfileError(Error):
    def __init__(self, name):
        super().__init__()
        self.name = name
    