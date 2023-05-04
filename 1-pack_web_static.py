#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tar gzipped archive of the directory web_static."""
    dt = strftime('%Y%m%d%H%M%S') + '.tgz'
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
