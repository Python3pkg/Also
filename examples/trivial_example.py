from also import also, AlsoMetaClass

class Foo(metaclass=AlsoMetaClass):
    @also('getThing')
    @also('get_thing')
    def getthing(self):
        return 'go bears'

foo = Foo()
assert (foo.getthing() == foo.get_thing() == 
        foo.getThing() == 'go bears')

