'''
projector project - automate your work routine
@author: sokolegg
'''

import os
import shutil
from shutil import copyfile
import logging

import projector

# MAIN 
''' In main projecor path you can add templates for different projects (look examples/templates)'''
PROJECTOR_PATH = projector.__path__
PROJECTOR_TEMPLATES = PROJECTOR_PATH + '/templates/'
PROJECTOR_DEFAULT_TEMPLATE = PROJECTOR_TEMPLATES + 'default/'
PROJECTOR_MAIN_LOGS = 

# PROJECT
''' In project/projecor path active file stores'''
PROJECTFILE_NAME = 'PROJECTFILE'
PROJECTOR_INSIDE_PATH = '.projector/'
PROJECTOR_MAKEFILE = PROJECTOR_INSIDE_PATH + 'MAKEFILE'
PROJECTOR_INSIDE_LOG_PATH = PROJECTOR_INSIDE_PATH + 'main.log'
PROJECTOR_INSIDE_METRICS_PATH = PROJECTOR_INSIDE_PATH + 'metrics/'

# Messages
TEMPLATE_FILE_EXISTS = 'Template file is exists! Ignored: '

def build(template=None):
	# prepare template
	template_path = PROJECTOR_DEFAULT_TEMPLATE if template is None else PROJECTOR_TEMPLATES + template + '/'

	# active path
	project_path = os.getcwd()
	projector_inside_full = project_dir + '/' + PROJECTOR_INSIDE_PATH
	os.mkdir(projector_inside_full)

	logging.basicConfig(filename="sample.log", level=logging.INFO)
	# Template files (PROJECTFILE or MAKEFILE or gitignore ...) to current project path
	for template_file in template_path:
		template_orig = template_path + template_file
		template_dst = project_path + template_file
		if not os.path.exists(template_dst):
			logging.info(TEMPLATE_FILE_EXISTS + template_dst)
		else:
			copyfile(template_orig, template_dst)


def start():
	pass

def finish():
	pass

