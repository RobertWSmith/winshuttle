# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:29:51 2015

@author: A421356
"""

from winshuttle.base import WinshuttleStudio
from winshuttle.studio.token import URLPathTokenValue, LocalPathTokenValue

class Transaction(WinshuttleStudio):
    """\
    Object which aides interaction between python and Winshuttle Transaction.

    Members:
        exe_path string which points to local Winshuttle Studio EXE
        auto_login string which points to local Auto Login File

    Methods:
        subprocess_args returns sequence of arguments suitable for subprocess.Popen
        find_file returns first file path found in sequence
    """

    def __init__(self, auto_login=None):
        paths = (
            "C:/Program Files/Winshuttle/TRANSACTION/TxShuttlecom.exe",
            "C:/Program Files/Winshuttle/Winshuttle Runner/TRANSACTIONRunner/TxRunnercom.exe",
            "C:/Program Files (x86)/Winshuttle/TRANSACTION/TxShuttlecom.exe",
            "C:/Program Files (x86)/Winshuttle/Winshuttle Runner/TRANSACTIONRunner/TxRunnercom.exe"
            )
        super().__init__(exe_path = WinshuttleStudio.find_file(paths), auto_login=LocalPathTokenValue(token='#AL', value=auto_login))

    def subprocess_args(self, run_script, local_file, **kwargs):
        """\
        Generate sequence of arguments for subprocess.Popen to run Winshuttle Query.

        Keyword Arguments:
            run_script required string which points to Winshuttle Central URL for desired script
            local_file required string which indicates desired output file for script
            kwargs optional ignored
        """
        output = super().subprocess_args(URLPathTokenValue('', run_script), LocalPathTokenValue('#F1', local_file))
        output = list([str(output[0]), ','.join([str(v) for v in output[1:]])])
        return output


