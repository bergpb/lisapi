### Lisa Pi - Flask Application

Control your Raspberry Pi Pins with Flask application.

Features:
- Login,
- Some system info,
- Registre pins,
- Control state between on/off

Flask modules:
- Flask-Login
- Flask-WTF
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Cors

System requirements:```python3```, ```pip``` and ```pipenv```.

Development:
  1. Clone project,
  2. Install dependencies: ```pipenv install```,
  3. Activate virtualenv: ```pipenv shell```,
  4. Run migrations: ```flask db init && flask db migrate && flask db upgrade```,
  5. Create a admin user: ```flask seed```,
  7. Export your app to flask env: ```export FLASK_APP=app```
  8. Export development in FLASK_ENV: ```export FLASK_ENV=development```
  9. Run project: ```flask run --host=0.0.0.0```.

Production (With Docker):
  1. Clone project,
  2. Build a docker container with command: ```docker build -t lisapi lisapi/Dockerfile```
  3. Run a container with command: ```docker run -d -p 80:5000```
  4. Access app in [localhost](localhost) url.


To do:
- [x] User login.
- [x] Save pins in database.
- [x] Check if pin is disponible before register.
- [x] Verify if pins exist in Raspberry Pi GPIO.
- [ ] Return system status in dashboard (Sockets).
- [ ] User permissions.
- [ ] Apply Unit Tests.
- [ ] RestFull Api.
