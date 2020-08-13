FROM python:3.8

#COPY requirements.txt /opt/app/requirements.txt
#COPY main_func.py /opt/app/main_func.py

COPY . /opt/app/

RUN pip install --no-cache-dir -r /opt/app/requirements.txt

CMD [ "python3.8", "/opt/app/main_func.py" ]

