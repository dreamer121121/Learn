import datetime
from functools import wraps
def http_method_required(method):
    """
    http请求必须是给定的method, 否则返回错误消息
    """

    def _deco(func):
        @wraps(func)
        def __wrapper(*args, **kwargs):

            if args[0].method == method:
                return func(*args, **kwargs)
            else:
                msg = E001.msg % (args[0].method, method)
                logger.error(msg)
                r = error_msg(E001.code, msg)
                return json_response(r)

        return __wrapper

    return _deco


def timecal(func):
    @wraps(func) #消除函数被装饰后名称等属性发生变化的的副作用
    def warpper(*args,**kargs):
        start = datetime.datetime.now()
        f = func(*args,**kargs)
        exe_time = datetime.datetime.now()-start
        print("func name:",func.__name__)
        print("exe_time:",exe_time)
        return f
    return warpper

@timecal
def add(a,b):
    return a+b

@timecal
def sub(a,b):
    return abs(a-b)

@timecal
def loop():
    i = 0
    while i<=10000000:
        i+= 1
print(add.__name__)
# add(1,2)
# sub(1,2)
# loop()
