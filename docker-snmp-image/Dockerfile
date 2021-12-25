FROM python:3.7-slim

RUN pip install snmpsim

RUN adduser --system snmpsim

ADD data /usr/local/snmpsim/data

EXPOSE 161/udp

CMD snmpsimd.py --data-dir=data --agent-udpv4-endpoint=127.0.0.1:1161 --process-user=snmpsim --process-group=nogroup