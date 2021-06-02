# MySQL 8.0 笔记

## 服务相关

```shell
# 查看 mysql 运行状态
sudo service mysql status
# 启动 mysql
sudo service mysql start
# 停止 mysql
sudo service mysql stop
# 重启 mysql
sudo service mysql restart
```

## MySQL

- 连接 mysql
  
    ```sql
    mysql -u root -p
    ```

- 修改 root 密码

    ```sql
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER; #修改加密规则
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码'; #使用mysql_native_password重新修改密码
    mysql> FLUSH PRIVILEGES;
    ```

- 允许 root 远程访问

    ```sql
    mysql> UPDATE mysql.user SET host = '%' WHERE user = 'root'; #允许远程访问
    mysql> FLUSH PRIVILEGES;
    ```

- 新增用户赋权并设置远程访问

    ```sql
    mysql> CREATE USER 'zhangpeng'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'zhangpeng'@'%' WITH GRANT OPTION;
    mysql> FLUSH PRIVILEGES;
    ```

- 查看所有数据库
  
    ```sql
    mysql> show databases; 
    ```

- 查看所有表
  
    ```sql
    mysql> show tables; 
    ```

- 显示创建 tbl 语句的语句
  
    ```sql
    show create table tbl\G;
    ```

- 显示创建 tbl 语句的语句
  
    ```sql
    show create table tbl\G;
    ```
