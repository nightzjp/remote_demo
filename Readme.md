### active mq 安装

```shell
docker run --name activemq --restart=always -t -d -e ACTIVEMQ_ADMIN_LOGIN=admin -e ACTIVEMQ_ADMIN_PASSWORD=admin  -p 61613:61613 -p 61616:61616 -p 8161:8161 webcenter/activemq:latest
```

### 测试代码启动
```shell
docker-compose up -d
docker-compose ps
```