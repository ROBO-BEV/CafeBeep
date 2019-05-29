# Docker file for a slim Ubuntu-based Python3 image
FROM ubuntu:latest
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY . /CafeBeepKiosk-0.1
WORKDIR /CafeBeepKiosk-0.1
RUN pip install -r requirements.txt
#RUN install node and npm
#RUN npm run install
ENTRYPOINT ["python3"]
CMD ["CafeBeepGUI.py"]
