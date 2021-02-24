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
