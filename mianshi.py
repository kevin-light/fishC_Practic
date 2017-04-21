class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kw):
        print('calling normal_method({0},{1}'.format(args,kw))
    @classmethod
    def class_method(*args,**kw):
        print('calling class_method({0},{1})'.format(args,kw))
    @staticmethod
    def static_method(*args,**kw):
        print('calling static method({0},{1})'.format(args,kw))
    @property
    def some_porperty(self,*args,**kw):
        print("calling some_property getter({0},{1},{2})".format(self,args,kw))
        return self._some_property
    @some_porperty.setter
    def some_property(self,*args,**kw):
        print("calling some property setter({0},{1},{2})".format(self,args,kw))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kw):
        print("calling some other porperty get({0},{1},{2})".format(self,args,kw))
        return self._some_other_property

o = MyClass()
print(o.normal_method)
o.normal_method()
o.normal_method(1,2,x=3,y=4)

o.static_method
o.static_method(1,2,x=3,y=4)
o.static_method((1, 2),{'y': 4, 'x': 3})

o.some_property
o.some_property()
