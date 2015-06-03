# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:29:44 2015

@author: A421356
"""

from winshuttle.base import WinshuttleStudio
from winshuttle.studio.token import URLPathTokenValue, LocalPathTokenValue, StringTokenValue, RuntimeTokenValue




class Query(WinshuttleStudio):
    """\
    Object which aides interaction between python and Winshuttle Query.

    Members:
        exe_path string which points to local Winshuttle Studio EXE
        auto_login string which points to local Auto Login File

    Methods:
        subprocess_args returns sequence of arguments suitable for subprocess.Popen
        find_file returns first file path found in sequence
    """

    def __init__(self, auto_login):
        paths = (
            "C:/Program Files/Winshuttle/QUERY/querySHUTTLEcom.exe",
            "C:/Program Files/Winshuttle/Winshuttle Runner/QUERYRunner/xSHUTTLEcom.exe",
            "C:/Program Files (x86)/Winshuttle/QUERY/querySHUTTLEcom.exe",
            "C:/Program Files (x86)/Winshuttle/Winshuttle Runner/QUERYRunner/xSHUTTLEcom.exe"
            )
        super().__init__(exe_path = WinshuttleStudio.find_file(paths), auto_login = LocalPathTokenValue(token='-alf', value=auto_login))

    def subprocess_args(self, run_script, local_file, **kwargs):
        """\
        Generate sequence of arguments for subprocess.Popen to run Winshuttle Query.

        Keyword Arguments:
            run_script required string which points to Winshuttle Central URL for desired script
            local_file required string which indicates desired output file for script
            local_table optional string which indicates the table name in the output file
            log_column optional string which indicates the name of the log column in the output file
            runtime_values optional sequence of dictionaries with fields `table`, `field` and `value`
        """
        lt = kwargs.get('local_table')
        lf = kwargs.get('log_column')
        rtv = kwargs.get('runtime_values')
        output = super().subprocess_args(URLPathTokenValue('-run', run_script), LocalPathTokenValue('-rfn', local_file))
        output = list([str(v) for v in output])
        if lf is not None:
            output.append(str(StringTokenValue(token='-log', value=lf)))
        if lt is not None:
            output.append(str(StringTokenValue(token='-rdt', value=lt)))
        if rtv is not None:
            output.append(str(RuntimeTokenValue(rtv)))
        output.append('-spw')
        return output

