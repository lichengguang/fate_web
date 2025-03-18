#!/bin/bash
# 后台启动Flask服务并指定监听地址
nohup flask run --host=0.0.0.0 --port=5000 > server.log 2>&1 &

# 显示启动状态
echo "服务已后台启动，PID: $!"
echo "访问地址: http://0.0.0.0:5000"
echo "查看日志: tail -f server.log"
