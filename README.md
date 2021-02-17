# 概述

通过控制台登录go.ruc认证连接外网。

假期在家通过vpn连接实验室的电脑（Linux），虽然可以连接上，但是由于时间原因，go.ruc自动下线，导致电脑无法连接外网。而go.ruc目前只能通过浏览器认证登录，因此萌发了通过terminal登录go.ruc的想法，这也是编写这个脚本的目的。

# 环境准备


## 浏览器

确保你的电脑已经安装firefox或者chrome，如果没有请先安装二者其一，这里仅介绍如何安装firefox：

- Centos:

```
sudo yum install -y firefox
```

- Ubuntu:

```
sudo apt install firefox
```

**注**：这里推荐使用firefox，主要因为firefox安装更加方便。

由于本脚本为python脚本，因此需要确保你的电脑已有python环境，关于python环境的安装这里不做赘述。


另外，如果你没有安装chrome或者firefox，也不打算安装，可以有另外一个选择：使用无头浏览器PhantomJS，具体安装教程可以参考[这里](https://www.vultr.com/docs/how-to-install-phantomjs-on-ubuntu-16-04)。

## 浏览器驱动

如果使用firefox浏览器和chrome浏览器, 还需要安装驱动。对于firefox，从[这里](https://github.com/mozilla/geckodriver/releases/)可以下载驱动(geckodriver)：

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
```

对于chrome，就稍微有点麻烦，安装的驱动必须和你的浏览器版本对应，[这里](https://sites.google.com/a/chromium.org/chromedriver/downloads/version-selection)阐述了如何下载正确的驱动，当然我这里提供了脚本可以帮助你下载正确的驱动：

```
sh get_chrome_drive.sh # must install curl or wget before 
```

**注**：如果下载失败，很可能是因为官方修改了驱动的路径，请自行阅读文档并下载。

下载完成之后，务必解压到当前路径。

## python依赖

当运行环境准备好后，运行下面的命令安装必要的依赖：

```
pip install selenium
```

上述命令需要联网才能执行，如果你当前无法连接到外网，那么可以通过源码安装，可以在[此处](https://pypi.python.org/pypi/selenium)下载源码，解压之后进入源码目录运行下面的命令：

```
python setup.py install
```

# 使用方法

运行login_goruc.py，输入用户名、密码即可认证通过，从而连接外网：

```
python login_goruc.py
```

