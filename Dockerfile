FROM ubuntu:20.04

RUN apt-get update 
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
ENV TZ=Asia/Dubai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y python3-tk
RUN apt-get install -y fonts-comic-neue



WORKDIR /app

COPY . .


CMD ["/app/src/main.py"]
ENTRYPOINT ["python3"]
