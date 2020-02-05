Docker容器用来封装应用、框架、及依赖包，Docker容器与虚拟机(VM)最大的区别在于容器不需要将操作系统（OS）封装进去，所有的Docker容器都共享主机(host)上的操作系统(OS)，这样的优势在于能够减少很多CPU, RAM及存储资源。
Docker容器是通过Docker镜像生成的，它是由Docker镜像创造的一个实例（a running instance that encapsulates required software. Containers are always created from images）  
通过```docker run```启动名为ubuntu镜像的docker容器
![image](docker_1.JPG)
docker run首先看主机上是否存在有此镜像（这里的ubuntu），如果没有则从Docker的托管平台下载。其中用到的参数如下：    
-t 在容器内开启一个交互终端  
-i 开启了输入功能  
*-it经常一起使用*  
— rm 当退出容器时容器自动删除  
使用```ctrl+D```退出容器，分别使用```docker ps -a```和```docker images```查看主机的容器和镜像。  
由于容器加了退出自动删除的参数，这里没有正在运行的容器。
![image](docker_2.JPG)  
由于下载了镜像，这里看到存在一个叫ubuntu的镜像。  
![image](docker_3.JPG)

再启动ubuntu镜像，并将她命名为daemon并让它在后台运行。此时通过```docker ps -a```会看到一个名为daemon的容器在运行。
![image](docker_4.JPG)
可以通过```docker stop daemon```、```docker start daemon```和```docker rm daemon```分别停止、开启、删除容器。
![image](docker_5.JPG)

通过以下命令下载nginx并映射端口和挂载存储卷  
```docker run -d --name "test-nginx" -p 8080:80 -v $(pwd):/usr/share/nginx/html:ro nginx:latest```
端口映射和挂载存储卷参数分别为：  
- -p is a ports mapping HOST PORT:CONTAINER PORT.    
- -v is a volume mounting HOST DIRECTORY:CONTAINER DIRECTORY.
![image](docker_6.JPG)
Docker volumes are used to persist data from a certain directory or directories of your Docker containers. So your data is not removed when the container stops or is removed.

## Reference
1. https://hackernoon.com/docker-tutorial-getting-started-with-python-redis-and-nginx-81a9d740d091