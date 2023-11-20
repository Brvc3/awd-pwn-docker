FROM ubuntu:18.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd ssh

RUN useradd -m ctf
RUN useradd -u 544 -g ctf -s /bin/bash -m ctfix
RUN echo ctfix:0123@ctfix | chpasswd

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf
RUN cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev
RUN mknod /home/ctf/dev/null c 1 3
RUN mknod /home/ctf/dev/zero c 1 5
RUN mknod /home/ctf/dev/random c 1 8
RUN mknod /home/ctf/dev/urandom c 1 9
RUN chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin
RUN cp /bin/sh /home/ctf/bin
RUN cp /bin/ls /home/ctf/bin
RUN cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./restart.sh /restart.sh
RUN chown ctfix:ctf /restart.sh
RUN chmod -R 750 /restart.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail


COPY ./bin/ /home/ctf/
RUN chown -R root:ctf /home/ctf
RUN chmod -R 750 /home/ctf
RUN chmod -R 770 /home/ctf/chal
#RUN chmod 744 /home/ctf/flag

CMD ["/restart.sh"]

EXPOSE 9999
