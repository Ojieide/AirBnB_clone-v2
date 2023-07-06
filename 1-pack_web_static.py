#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """ Generates a .tgz archive """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    ts = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        ts.year,
        ts.month,
        ts.day,
        ts.hour,
        ts.minute,
        ts.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
