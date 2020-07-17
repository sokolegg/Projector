"""
projector project - automate your work routine
@author: sokolegg
"""
import os
import logging
import sys
import projector
from yaml import load, dump
from projector import cfg
from projector.utils import Project, Template, Script

project = Project(os.getcwd())


def build(template_name):
    project.make()
    template = Template(template_name)
    template.insert_in(project)
    logging.basicConfig(filename=project.log, level=logging.INFO)


def run():
    logging.basicConfig(filename=project.log, level=logging.INFO)
    file_data = open(project.projectfile).read()
    logging.info(cfg.PROJECTFILE_FOUND + file_data)
    data = load(file_data)
    for to_run in data['run']:
        logging.info(cfg.RUN_MESSAGE + to_run)
        run_process(to_run)


def run_process(to_run):
    if to_run == '.':
        path = project.path
        Script('open_folder').run(project, path)


def stop():
    pass


def main():
    project = Project(os.getcwd())
    args = sys.argv[1:]
    if args[0] == 'build':
        t = args[1] if len(args) > 1 else None
        build(t)
    if args[0] == 'run':
        run()


if __name__ == '__main__':
    main()
