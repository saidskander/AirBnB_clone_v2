#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """create a tar.gz tar gzipped archivz for directory web_static"""
    date_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(date_time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose --file={} -z ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
