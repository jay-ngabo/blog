from app import create_app,db
from app.models import User
from  flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('production')
# app = create_app('test')
app.config.update(dict(
    SECRET_KEY="biivannce",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True


migrate = Migrate(app,db)


# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User =User)


if __name__ == '__main__':
    app.run()