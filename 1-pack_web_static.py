#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Generates a .tgz archive """
    ts = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(ts.year,
                                                         ts.month,
                                                         ts.day,
                                                         ts.hour,
                                                         ts.minute,
                                                         ts.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
