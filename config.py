import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY='Welch want to go chengdu'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX='[Welch]'
	FLASKY_MAIL_SENDER='Admin Welch <18383078106@163.com>'
	FLASK_ADMIN='450406504@qq.com'
	FLASKY_POSTS_PER_PAGE = 20

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER='smtp.163.com'
	MAIL_PORT=25
	MAIL_USE_TLS = True
	MAIL_USERNAME = '18383078106@163.com'
	MAIL_PASSWORD = '*l'
	SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or\
				'sqlite:///'+os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or\
				'sqlite:///'+os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or\
				'sqlite:///'+os.path.join(basedir, 'data.sqlite')

config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,

	'default':DevelopmentConfig
}
