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
from fabric.operations import sudo
""" def do_pack """

env.hosts = ['35.196.178.240', '34.74.85.130']
path_to_deploy = None


def do_pack():
    """create a tar.gz tar gzipped archivz for directory web_static"""
    date_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(date_time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose --file={} -z ./web_static"
              .format(file))
        return file
    except:
        return None


def do_deploy(archive_path):
    """ using fabric to distribute archive """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        directory = archive.split(".")
        run("mkdir -p {}/{}/".format(path, directory[0]))
        new_archive = '.'.join(directory)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, directory[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, directory[0], path, directory[0]))
        run("rm -rf {}/{}/web_static".format(path, directory[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, directory[0]))
        return True
    except:
        return False


def create_distribute_deploy():
    """ deploy function creates and distribute an archive """
    global path_to_deploy
    if path_to_deploy is None:
        path_to_deploy = do_pack()
    if path_to_deploy is None:
        return False
    return do_deploy(path_to_deploy)
