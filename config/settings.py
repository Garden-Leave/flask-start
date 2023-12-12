

HOST = '192.168.0.11'


# 用下面的代码区分prod和local配置，生产环境的配置放在local_settings.py,如果有生产配置就导入，没有就什么也不做，代表测试环境
try:
    from local_settings import *
except ImportError as e:
    print('import error %s' % e)
