import json
import os

def loadError(code):
    """
    ### Return error message
    ##### Return an error message from error.json file.
    @code: The error code number.
    pass an argument `error code` number as in `errors.json` file to return\n
    >>> strting from 100
    ----
    """
    with open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'kiqpo','errors.json'))) as errList:
        errorsList = json.loads(errList.read())
        result = [error for error in errorsList if error["code"]==code]
        return result[0]['error']