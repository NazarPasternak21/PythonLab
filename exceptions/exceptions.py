class RedundantChargeException(Exception):

    def __int__(self, message):
        self.message = message

    def __str__(self):
        return "Battery level 100%"
