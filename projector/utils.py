from projector.cfg import *
import subprocess
from shutil import copyfile
import os
import logging


class Project:

    def __init__(self, path='.'):
        self.name = path
        self.path = path + '/'
        self.projectfile = self.path + PROJECT_PROJECTFILE
        self.projector = self.path + PROJECT_PROJECTOR
        self.log = self.path + PROJECT_LOG
        self.metrics = self.path + PROJECT_METRICS

    def make(self):
        for f in [self.projector, self.metrics]:
            os.mkdir(f)
        for f in [self.projectfile, self.log]:
            open(f, 'x')


class Template:

    def __init__(self, name):
        self.name = 'default' if name is None else name
        self.path = PROJECTOR_TEMPLATES + self.name + '/'

    def insert_in(self, project):
        logging.basicConfig(filename=project.log, level=logging.INFO)
        for template_file in os.listdir(self.path):
            template_orig = self.path + '/' + template_file
            template_dst = project.path + '/' + template_file
            logging.info(COPY_MESSAGE + template_dst)
            copyfile(template_orig, template_dst)


class Script:

    def __init__(self, name):
        self.name = name
        self.path = SCRIPTS_PATH + OS + '/' + name

    def run(self, project, *args):
        logging.basicConfig(filename=project.log, level=logging.INFO)
        script = f"{OS_EXECUTOR} {self.path} {' '.join(args)}"
        logging.info(SCRIPT_BUILD + script)
        return subprocess.call([script], shell=True)
