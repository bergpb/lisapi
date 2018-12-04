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

System requirements: ```python3```, ```pip3```, ```virtualenv```.
1. Clone project,
2. Create a virtualenv: ```python3 -m venv .env```,
3. Activate virtualenv: ```. .env/bin/activate```,
4. Install requirements: ```pip3 install -r requirements.txt```,
4. Run migrations: ```flask db init && flask db migrate && flask db upgrade```,
5. Create a admin user: ```flask seed```,
6. Run project: ```flask run --host=0.0.0.0```.

To do:
- [x] Login.
- [x] Save pins in db.
- [x] Check if pin is disponible.
- [x] Verify if pins exist in Raspberry Pi.
- [ ] Return system status in dashboard.
- [ ] RestFull Api.
