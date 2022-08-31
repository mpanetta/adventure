from datetime import datetime

class _Logger(object):
    DEBUG = "debug"

    _instance = None

    def __new__(klass):
        if(klass._instance == None):
            klass._instance = super(_Logger, klass).__new__(klass)
            klass._instance._set_log()

        return klass._instance

    # public methods

    def log(self, msg, channel = DEBUG):
        path = f"./log/{channel}_log.txt"
        with open(path, "a+") as f:
            f.write(f"\n{msg}")

    # private methods

    def _set_log(self, channel = DEBUG):
        self.log(f"\n\n\n\n{datetime.now()}")
Logger = _Logger()
