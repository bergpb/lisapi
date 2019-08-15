# Deploy with Supervisor and Nginx

## Install OS dependencies

```sudo apt install python-pip python-virtualenv supervisor nginx```

---

### Creating virtualenv and running project

1. Clone project,
2. Enter in project folder,
3. Create a virtualenv: ```python -m venv .venv```,
4. Install python dependencies: ```pip install -r requirements.txt```,
5. Activate virtualenv: ```source .venv/bin/activate```,
6. Run ```flask db-init``` to run migrations and create admin user,
7. Create a .env file in root of project and add FLASK_ENV and SECRET_KEY variables with your values.
   1. FLASK_ENV - Flask environment, development or production. Ex: FLASK_ENV=development
   2. SECRET_KEY - Your secret key into app. Ex: SECRET_KEY=your_secret_key
8. Run server: ```gunicorn app:app --worker-class eventlet -w 2 -b 0.0.0.0:8000```,
9. Access [http://localhost:8000](http://localhost:8000),
10. Application is up.

### Creating a supervisor configuration

1. Running with supervisor you have many options to control application execution.
This configuration starts application with O.S. start, and restarts automatically if something going wrong.
Change pi with your system user.

```sudo nano /etc/supervisor/conf.d/lisapi.conf```

```bash
[program:lisapi]
command = /home/raspb/lisapi/.venv/bin/gunicorn app:app --worker-class eventlet -w 4 -b :5000 --reload
directory = /home/raspb/lisapi
user = raspb   
autostart = true
stderr_logfile = /var/log/supervisor/lisapi-stderr.log
stdout_logfile = /var/log/supervisor/lisapi-stdout.log
```

2. Save file.

3. Restart ```supervisor``` configurations:

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart lisapi
```

---

### Creating a nginx configuration

1. Removing default and creating new configuration file:
```bash
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/lisapi
sudo ln -s /etc/nginx/sites-available/lisapi /etc/nginx/sites-enabled/lisapi
sudo nano /etc/nginx/sites-available/lisapi
```
Insert this content:
```bash
server {
    server_name _;
    location /static {
    alias /home/raspb/lisapi/app/static;
        autoindex on;
        expires max;
    }
    location / {
        include proxy_params;
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://localhost:8000/socket.io;
    }
        error_log /var/log/nginx/lisapi_error.log;
        access_log /var/log/nginx/lisapi_access.log;
}
```
2. Save file.
3. Check config and restart ```nginx``` service:
```bash
sudo nginx -t
sudo service nginx restart
```
4. Access your remote url.
