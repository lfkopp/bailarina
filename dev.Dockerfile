# USING PYTHON 3.11.8
FROM python:3.11.8-slim-bullseye

# SET PYTHONUNBUFFERED TO FIX LOGGING
ENV PYTHONUNBUFFERED=1

# SET PYTHONPATH TO ALLOW LOCATING SRC MODULE
ENV PYTHONPATH=/srv/app

# SET WORKDIR
WORKDIR /srv/app

# COPY REQUIREMENTS.TXT
COPY requirements.txt .

# INSTALL DEPENDENCIES
RUN pip install -r requirements.txt

# COPY SOURCE FILES
COPY . .

# RUN COMMAND
CMD [ "python3", "-u", "app.py" ]
