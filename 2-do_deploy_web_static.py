#!/usr/bin/python3
# Fabric script that generates a
# .tgz archive from the contents of the web_static
import os
import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import *
from fabric.operations import run
from fabric.operations import put
""" def do_pack """

env.hosts = ['35.237.87.143', '34.75.67.199']


def do_deploy(archive_path):
    """ using fabric to create and distribute an archive """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except:
        return False
