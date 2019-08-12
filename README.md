### Lisa Pi - Flask Application

Control your Raspberry Pi Pins with Flask application.

Features:
- Login
- Some system info,
- Register pins to control,
- Control state of pins between on/off

Flask modules:
- Flask-Login
- Flask-WTF
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Cors
- Flask-SocketIO

System requirements:```python3``` and```pipenv```.

Development:
  1. Clone project,
  1. Enter in project folder,
  1. Install dependencies: ```pipenv install```,
  1. Activate virtualenv: ```pipenv shell```,
  1. Run migrations and create admin user: ```flask db-seed```,
  1. Run project: ```python run.py```.


To do:
- [x] User login.
- [x] Save pins in database.
- [x] Check if pin is disponible before register.
- [x] Verify if pins exist in Raspberry Pi GPIO.
- [x] Return system status in dashboard (Using Sockets).
- [ ] User permissions.
- [ ] Apply Unit Tests.
- [ ] RestFull Api.
