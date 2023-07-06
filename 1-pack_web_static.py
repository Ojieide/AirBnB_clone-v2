#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ Generates a .tgz archive """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(dt)
        local("tar -cvzf {} ./web_static".format(file_path))
        return file_path
    except Exception:
        return None
