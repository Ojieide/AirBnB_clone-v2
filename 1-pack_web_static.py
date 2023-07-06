#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Returns the archive path if the archive has been correctly
    generated Otherwise, None
    """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} ./web_static".format(file_name))
        return file_name
    except Exception:
        return None
