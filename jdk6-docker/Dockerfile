# 基础镜像
FROM ubuntu:latest
# 维护者信息
MAINTAINER jdk6 <24@24team.com>

RUN mkdir /usr/java && mkdir /sec

# 将应用程序代码复制到镜像中
COPY ./jdk-6u45-linux-x64.bin /usr/java
COPY ./jre-6u45-linux-x64.bin /usr/java
# 设置工作目录 因为工作目录设置成了/，所以docker容器里面安装的东西则是在根目录
WORKDIR /   

RUN apt-get update && \
    apt-get install -y curl && \
    chmod 755 /usr/java/jdk-6u45-linux-x64.bin && \
    /usr/java/jdk-6u45-linux-x64.bin && \
    chmod a+w /etc/profile && \
  	echo "export JAVA_HOME=/jdk1.6.0_45" >> /etc/profile && \
    echo "export JAVA_BIN=/jdk1.6.0_45/bin" >> /etc/profile && \
    echo "export PATH=\$PATH:\$JAVA_HOME/bin" >> /etc/profile && \
    echo "export CLASSPATH=.:\$JAVA_HOME/lib/dt.jar:\$JAVA_HOME/lib/tools.jar" >> /etc/profile && \
    echo "export JAVA_HOME JAVA_BIN PATH CLASSPATH" >> /etc/profile && \
    chmod a+r /etc/profile
      
# 暴露端口，该端口任意
EXPOSE 8080