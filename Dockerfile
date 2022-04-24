#FROM python:3.7-slim
FROM python:3.9-slim-bullseye

# Install SNMP server 
RUN apt-get update && apt-get install -y \
    snmp \
    gcc

RUN pip install snmpsim

RUN adduser snmpsim

ADD data /usr/local/snmpsim/data

# Example to start with the SNMP server
#CMD snmpsimd.py --data-dir=data --agent-udpv4-endpoint=127.0.0.1:1161 --process-user=root --process-group=root

# Install pynacl
RUN apt-get update && apt-get install -yf python3-dev build-essential python3 python3-venv curl git tcpdump wget 
RUN python3 -m venv venv
RUN venv/bin/pip install pynacl

# Install graphviz for plantuml
RUN apt-get install -y graphviz

# Install Java
RUN apt-get install -y openjdk-11-jre

# Install Pyangbind
RUN git clone https://github.com/robshakir/pyangbind.git && cd pyangbind && python3 setup.py install

# Install go
RUN apt-get install -y golang-go
RUN apt-get install -y nano
RUN mkdir /usr/share/gocode/
RUN mkdir /usr/share/gocode/src/
RUN export GOPATH=/usr/share/gocode/
RUN go get github.com/google/gnxi
RUN go get github.com/openconfig/ygot/generator

# Use a nicer Linux shell
COPY bashrc /root/.bashrc
ENTRYPOINT [ "/bin/bash" ]

# Create folder for sharing
RUN mkdir /root/lab

# Add files into the container
ADD OFC_SC472 /root/OFC_SC472

COPY lab_requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Set working directory
WORKDIR /root
