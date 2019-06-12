class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
a = A()
print(a.foo)
print(a.class_foo)
print(a.static_foo)
a.foo(1)
A.foo(a,1)
A.class_foo(1)
a.class_foo(1)
a.static_foo(1)
A.static_foo(1)


class A(object):
    def __init__(self, parms):
        self.parms = parms
        self.print_dicts(**parms)
    def print_dicts(self, **parms):
        print(parms['NAME'], parms['AGE']) # 打印配置信息 # 类方法（不需要实例化类就可以被类本身调用）

    @classmethod
    def from_settings(cls, g_dict): # cls : 表示没被实例化的类本身
        return cls(g_dict) # 实例化

# 注册中间件
DICTS = ['test.A']
NAME = 'YangJiHai' # 全局配置变量
AGE = '20' # settings文件与中间件交互的处理，为了简便代码放在这里演示
for test in DICTS:
    m, c = test.rsplit('.', 1) # 反向分割取得类名
    print(m,c)
    m = __import__(m) # 导入模块
    if hasattr(m, c): # 判断模块中是否存在该字符串属性
        target_class = getattr(m, c) # 获取该属性的引用
        print(target_class)
        if hasattr(target_class, 'from_settings'): # 获取inp的引用
            target_func = getattr(target_class, 'from_settings')
            g = globals() # 获取全局变量返回字典类型
            print(g)
            target_func(g) # 执行
