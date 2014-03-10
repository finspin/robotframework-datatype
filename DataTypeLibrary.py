from robot.api import logger


class DataTypeLibrary(object):

    def should_be_integer(self, obj):
        if not isinstance(obj, int):
            message = "%s his is not integer" % obj
            raise AssertionError(message)

    def should_be_string(self, obj):
        if not isinstance(obj, basestring):
            message = "%s his is not string" % obj
            raise AssertionError(message)
     
    def should_be_digit(self, obj):
        if not obj.isdigit():
            message = "%s his is not digit" % obj
            raise AssertionError(message)
            
    def should_be_alphanumeric(self, obj):
        if not obj.isalnum():
            message = "%s his is not alphanumeric" % obj
            raise AssertionError(message)

    def should_be_alphabetic(self, obj):
        if not obj.isalpha():
            message = "%s is not alphabetic" % obj
            raise AssertionError(message)
            
    def should_be_numeric(self, obj):
        if not obj.isnumeric():
            message = "%s is not numeric" % obj
            raise AssertionError(message)

    def convert_to_lowercase(self, string):
        lowstr = string.lower()
        logger.info("%s has been converted to %s" % (string, lowstr))
        return lowstr 
            
    def convert_to_uppercase(self, string):
        upstr = string.upper()
        logger.info("%s has been converted to %s" % (string, upstr))
        return upstr 
