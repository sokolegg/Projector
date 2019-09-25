'''
projector project - automate your work routine
@author: sokolegg
'''
import os
import shutil
from shutil import copyfile
import logging
import sys
import projector
import subprocess
from yaml import load, dump

''' In main projecor path you can add templates for different projects (look examples/templates)'''
PROJECTOR_PATH = projector.__path__[0]
PROJECTOR_TEMPLATES = PROJECTOR_PATH + '/templates/'
SCRIPTS_PATH = PROJECTOR_PATH + '/scripts/'
PROJECTOR_DEFAULT_TEMPLATE = PROJECTOR_TEMPLATES + 'default/'
PROJECTOR_MAIN_LOGS = PROJECTOR_PATH + '/main.log' 
''' In project/projecor path active file stores'''
PROJECTFILE_NAME = 'PROJECTFILE'
PROJECTOR_INSIDE_PATH = '.projector/'
PROJECTOR_MAKEFILE = PROJECTOR_INSIDE_PATH + 'MAKEFILE'
PROJECTOR_INSIDE_LOG_PATH = PROJECTOR_INSIDE_PATH + 'main.log'
PROJECTOR_INSIDE_METRICS_PATH = PROJECTOR_INSIDE_PATH + 'metrics/'
# Messages
TEMPLATE_FILE_EXISTS = 'Template file is exists! Ignored: '
COPY_MESSAGE = 'Making copy from template: '
RUN_MESSAGE = 'Runing command: '
PROJECTFILE_FOUND = "Found PROJECTFILE: "
# os info
OS = 'ubuntu'

def build(template=None):
	# prepare template
	template_path = PROJECTOR_DEFAULT_TEMPLATE if template is None  \
	else PROJECTOR_TEMPLATES + template + '/'

	# active path
	project_path = os.getcwd()+ '/'
	projector_inside_full = project_path + PROJECTOR_INSIDE_PATH
	os.mkdir(projector_inside_full)

	logging.basicConfig(filename=projector_inside_full + 'main.log', level=logging.INFO)
	# Template files (PROJECTFILE or MAKEFILE or gitignore ...) to current project path
	for template_file in os.listdir(template_path):
		template_orig = template_path + template_file
		template_dst = project_path + template_file
		if os.path.exists(template_dst):
			logging.info(TEMPLATE_FILE_EXISTS + template_dst)
		else:
			logging.info(COPY_MESSAGE + template_dst)
			copyfile(template_orig, template_dst)

def open_folder(path):
	script_path = SCRIPTS_PATH + OS + '/' + 'open_folder'
	subprocess.call([f"sh {script_path} {path}"], shell=True)

def run_process(to_run):
	if to_run == '.':
		open_folder(to_run)

def run():
	# active path
	project_path = os.getcwd()+ '/'
	projector_inside_full = project_path + PROJECTOR_INSIDE_PATH
	logging.basicConfig(filename=projector_inside_full + 'main.log', level=logging.INFO)

	projectfile = project_path + PROJECTFILE_NAME
	file_data = open(projectfile).read()
	logging.info(PROJECTFILE_FOUND + file_data)
	data = load(file_data)
	print(data)
	for to_run in data['run']:
		logging.info(RUN_MESSAGE + to_run)
		run_process(to_run)


def finish():
	pass

def main():
	args = sys.argv[1:]
	if args[0] == 'build':
		t = args[1] if len(args) > 1 else None
		build(t)
	if args[0] == 'run':
		run()

if __name__ == '__main__':
	main()

