# AWD-PWN出题模板

该仓库是AWD-PWN出题模板

选手账号在`deploy/dockerfile`中配置

`deploy/docker build.sh`用于一键构建容器

`restart.sh`既是启动脚本也是重启脚本

build之前要将`deploy/ctf.xinetd`中的`chal`替换成题目文件的名字

flag如何添加到容器里请自定义，这里没有写

## check

check脚本需自定义，这里提供了模板