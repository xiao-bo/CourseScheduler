'''
Set system root path, google project ID and all commands will inheritance this
class to set system path
'''

import sys
from pathlib import Path


class BasicCommand(object):

    def __init__(self):

        self.PROJECT_ROOT_PATH = str(Path(__file__).parents[1])

        # Append ROOT_PATH_module to system path
        if self.PROJECT_ROOT_PATH not in sys.path:
            # Avoid to append duplicated path to system path.
            sys.path.append(self.PROJECT_ROOT_PATH)

