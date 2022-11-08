FROM ubuntu:22.10

RUN apt-get update
RUN apt-get install -y build-essential

# This will install Python, pip, pip3, and pip3.6.

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip 

WORKDIR /api

COPY requirements.txt /api/

RUN pip3 --no-cache-dir install -r requirements.txt 

COPY . /api/

EXPOSE 5000

CMD ["python3", "app.py"]
