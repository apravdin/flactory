import os
import shutil
from shlex import split
from subprocess import call

DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE = '{}/{}'.format(DIR, 'app_template')

APP_NAME_PLACEHOLDER = 'myapp'

FILES = ['README.md', 'config.py']


def update_file(file_path, pattern, replace):
    cmd = "sed -i '' s/{}/{}/g {}".format(pattern, replace, file_path)
    print cmd
    call(split(cmd))


def create_project(project_name):
    project_path = os.path.join(DIR, project_name)

    print 'Creating project in: {}'.format(project_path)

    try:
        shutil.copytree(TEMPLATE, project_path)
    except OSError:
        print 'Directory already exists. Exiting creation.'

    for filename in FILES:
        path = os.path.join(project_path, filename)
        update_file(path, APP_NAME_PLACEHOLDER, project_name)

if __name__ == '__main__':
    project_name = raw_input('Project name: ')

    create_project(project_name)
