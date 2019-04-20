### Lisa Pi - Flask Application

Control your Raspberry Pi Pins with Flask application.

Features:
- Login
- Some system info,
- Register pins,
- Control state between on/off

Flask modules:
- Flask-Login
- Flask-WTF
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Cors
- Flask-SocketIO

System requirements:```python3```, ```pip``` and ```pipenv```.

Development:
  1. Clone project,
  2. Enter in project folder,
  3. Install dependencies: ```pipenv install```,
  4. Activate virtualenv: ```pipenv shell```,
  5. Run migrations: ```flask db init && flask db migrate && flask db upgrade```,
  6. Create a admin user: ```flask seed```,
  7. Export your app to flask env: ```export FLASK_APP=app```
  8. Export development in FLASK_ENV: ```export FLASK_ENV=development```
  9. Run project: ```python run.py```.

Production (With Docker):
  1. Clone project,
  2. Enter in project folder,
  3. Build a docker container with command: ```docker build -t lisapi .```
  4. Run a container with command: ```docker run -d -p 5000:5000```
  5. Access app in [localhost:5000](localhost:5000).


To do:
- [x] User login.
- [x] Save pins in database.
- [x] Check if pin is disponible before register.
- [x] Verify if pins exist in Raspberry Pi GPIO.
- [x] Return system status in dashboard (Sockets).
- [ ] User permissions.
- [ ] Apply Unit Tests.
- [ ] RestFull Api.
