import projector

''' In main projecor path you can add templates for different projects (look examples/templates)'''
PROJECTOR_PATH = projector.__path__[0]
PROJECTOR_TEMPLATES = PROJECTOR_PATH + '/templates/'
SCRIPTS_PATH = PROJECTOR_PATH + '/scripts/'
PROJECTOR_DEFAULT_TEMPLATE = PROJECTOR_TEMPLATES + 'default/'
PROJECTOR_MAIN_LOGS = PROJECTOR_PATH + '/main.log' 

''' MESSAGES'''
TEMPLATE_FILE_EXISTS = 'Template file is exists! Ignored: '
COPY_MESSAGE = 'Making copy from template: '
RUN_MESSAGE = 'Runing command: '
PROJECTFILE_FOUND = "Found PROJECTFILE: "
SCRIPT_BUILD = "Script build: "

'''OS INFORMATION'''
OS = 'ubuntu'
OS_EXECUTOR = 'sh'

''' This files depend on project path '''
PROJECT_PROJECTFILE = 'PROJECTFILE'
PROJECT_PROJECTOR = '.projector/'
PROJECT_LOG = PROJECT_PROJECTOR + 'main.log'
PROJECT_METRICS = PROJECT_PROJECTOR + 'metrics/'

