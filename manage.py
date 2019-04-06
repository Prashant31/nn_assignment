#! /usr/bin/env python

import os

from flask_script import Manager
from GunicornServer import GunicornServer

from app import create_app, db


app = create_app(os.getenv('APP_CONFIG', 'default'))
manager = Manager(app)
manager.add_command("gunicorn", GunicornServer())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
