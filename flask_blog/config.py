class config:
	SECRET_KEY='a272dbc8c1517d505213a0c4c8781e04'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('site.db')
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	MAIL_SERVER='smtp.googlemail.com'
	MAIL_PORT=465
	MAIL_USE_SSL=True
	MAIL_USERNAME='aditya126461@gmail.com'
	MAIL_PASSWORD='R@U+H@N12'
