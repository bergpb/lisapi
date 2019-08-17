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
- Flask-SocketIO

System requirements:
```sudo apt install build-essential libssl-dev libffi-dev python3-dev```


Development:
  1. Clone project,
  2. Enter in project folder,
  3. Install dependencies: ```pipenv install```,
  4. Activate virtualenv: ```pipenv shell```,
  5. Run migrations and create admin user: ```flask db-seed```,
  6. Run project: ```python run.py```.


Production:
  1. [Deploy with supervisor](https://github.com/bergpb/lisapi/wiki/Deploy-with-Supervisor)
  2. [Deploy with nginx](https://github.com/bergpb/lisapi/wiki/Deploy-with-Nginx)

To do:
- [x] User login.
- [x] Save pins in database.
- [x] Check if pin is disponible before register.
- [x] Verify if pins exist in Raspberry Pi GPIO.
- [x] Return system status in dashboard (Using Sockets).
- [ ] User permissions.
- [ ] Apply Unit Tests.
- [ ] RestFull Api.
