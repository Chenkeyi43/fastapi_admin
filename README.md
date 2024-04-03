# 进入后端目录
    cd fastapi_admin

# 安装项目依赖环境
    pip3 install -r requirements.txt

# 配置环境
    在.env.dev文件中配置开发环境的数据库和redis

# 运行sql文件
    1.新建数据库fastapi_admin(默认，可修改)
    2.使用命令或数据库连接工具运行sql文件夹下的fastapi_admin.sql

# 运行后端
    python3 app.py --env=dev


# 默认账号密码
    账号：admin
    密码：admin123

# 浏览器访问
    地址：http://localhost:80


# 发布

    ## 配置环境
    在.env.prod文件中配置生产环境的数据库和redis

    ## 运行后端
    python3 app.py --env=prod
