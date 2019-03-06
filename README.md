### Lisa Pi - Flask Application

Control your Raspberry Pin with Flask application.

Features:
- Login
- Registre pins
- Control state between on/off

Flask modules:
- Flask-Login
- Flask-WTF
- Flask-Migrate
- Flask-SQLAlchemy

System requirements: ```python2.7``` or ```python3```, ```pip``` and ```pipenv```.

1. Clone project,
2. Install dependencies: ```pipenv install```,
3. Activate virtualenv: ```pipenv shell```,
4. Run migrations: ```flask db init && flask db migrate && flask db upgrade```,
5. Create a admin user: ```flask seed```,
7. Export your app to flask env: ```export FLASK_APP=app```
7. Export development in FLASK_ENV: ```export FLASK_ENV=development```
9. Export your api url with: ```export LISA_API=your_url/api/status```
10. Run project: ```flask run --host=0.0.0.0```.

To do:
- [x] User login.
- [x] Save pins in database.
- [x] Check if pin is disponible before register.
- [x] Verify if pins exist in Raspberry Pi GPIO.
- [x] Return system status in dashboard.
- [ ] User permissions.
- [ ] Apply Unit Tests.
- [ ] RestFull Api.
