FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    snmp \
    gcc

RUN pip install snmpsim

RUN adduser snmpsim

ADD data /usr/local/snmpsim/data

# Use a nicer Linux shell
COPY bashrc /root/.bashrc
ENTRYPOINT [ "/bin/bash" ]

#CMD snmpsimd.py --data-dir=data --agent-udpv4-endpoint=127.0.0.1:1161 --process-user=root --process-group=root

