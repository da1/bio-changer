from fabric.api import env, run, cd
"""
    $ fab -u <user> -i ~/.ssh/id_rsa -H <host> --port <port> update
"""

PROJECT_DIR = 'bio-changer'

def update():
    with cd(PROJECT_DIR):
        run('git pull')

def log_tail():
    with cd(PROJECT_DIR):
        run('tail log/update.log')

