class Singleton:
    instance=None


    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super(Singleton,cls).__new__(cls)

        return cls.instance



a= Singleton()
b= Singleton()

