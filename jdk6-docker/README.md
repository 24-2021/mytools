## 下载JDK6

jdk官方，不再演示

## 配置文件

```bash
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
```
可能会用到的命令
```bash
apt-get install -y vim-gtk 
```
## 根目录下文件
![image.png](https://cdn.nlark.com/yuque/0/2023/png/12847038/1697169172278-688ab2a9-9b50-471e-9461-a1f480b34857.png#averageHue=%2392c6dc&clientId=u6fb7f864-a57f-4&from=paste&height=279&id=u867c882f&originHeight=349&originWidth=810&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=21424&status=done&style=none&taskId=u6fba6ee3-2b56-4722-a027-2154d85ff34&title=&width=648)
## 编译启动
```bash
#编译镜像
docker build -t jdk6 .
#运行镜像
docker run -itd -p 8006:8006 jdk6
#进入终端
docker exec -it [id]  bash
#初始化
. /etc/profile
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/12847038/1697169281690-78d9a1dd-3fef-496d-8147-a8ea097a4a99.png#averageHue=%23080e11&clientId=u6fb7f864-a57f-4&from=paste&height=438&id=uf51e21bf&originHeight=548&originWidth=1466&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=139858&status=done&style=none&taskId=uf856a0f3-53b4-447b-9480-3c2d9d83138&title=&width=1172.8)
以下截图说明部署完成
![image.png](https://cdn.nlark.com/yuque/0/2023/png/12847038/1697169346108-12c2a451-0ebf-4ff5-bb47-8ca0eb1c5256.png#averageHue=%23020203&clientId=u6fb7f864-a57f-4&from=paste&height=590&id=uc5b0116d&originHeight=738&originWidth=1132&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=160992&status=done&style=none&taskId=ue3590a5e-411c-4fda-97aa-5419b0cbbea&title=&width=905.6)
发现启动成功
![image.png](https://cdn.nlark.com/yuque/0/2023/png/12847038/1697169390848-c474c950-bd10-426d-a7fc-e18c6f6949e0.png#averageHue=%23020203&clientId=u6fb7f864-a57f-4&from=paste&height=273&id=u513b73e3&originHeight=341&originWidth=1593&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=83892&status=done&style=none&taskId=u8c736088-8463-4217-9f2a-5ffb0869cc1&title=&width=1274.4)
