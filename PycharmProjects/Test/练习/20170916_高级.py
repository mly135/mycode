#coding=utf-8


####self 代表类的实例
class Person:
    name = "";
    age = 0;
    __private_sex = 2;
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aaa(self):
        print "aaa"



per = Person("李四", 15)

print per.__dict__

print per.__doc__

per.__init__("张三", 12)

print per.__dict__

print per.__module__



##### 对象回收机制
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1
del pt2
del pt3



#####类的继承，可以支持多继承

class Chinese(Person):

    __private_children = 1;

    def aaa(self):
        Person.aaa(self)

    def __init__(self, __init__, name, age):
        __init__.name = name
        __init__.age = age
    def __str__(self):
        print "重写str方法"



person = Person("张三",12);

print person.name,person.age

children = Chinese(person, "李四", 13);

print person.name,person.age


# 判断是否是父类
print issubclass(Chinese,Person)
# 判断是否是实例
print isinstance(children, Chinese)

# __foo__ 特殊方法
#
# __foo  私有变量
#
# _foo protected 变量
#




