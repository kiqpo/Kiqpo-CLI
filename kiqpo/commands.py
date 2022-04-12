from kiqpo.section.brain import brain
from . import parsers
from .section import functions
from .error import loadError


class Methods():
    KiqpoParser = parsers.kiqpoParser.parser
    # This is required positional argument
    KiqpoParser.add_argument(
        "commands",
        nargs='*',
        type=str,
        help="kiqpo CLI Commands & Methods",
        default="kiqpo",
    )
    # Initial user entered arguments
    args = KiqpoParser.parse_args()
    method = args.commands[0]
    isValid = False
    runFunction = None
    index = 0

    # Seraching & find wether use give command is right.
    for function in functions.my:
        index += 1
        if(method in function['command']):
            isValid = True
            runFunction = function['command']
            break
        else:
            if(len(function) < index):
                runFunction = None
                print(loadError(code=100))
                break
            else:
                continue

    # Brain the central function of this project
    # Which helps us to run program according to the command give.
    brain(runFunction)
