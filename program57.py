""" Acessing all accessspecifers"""
class Base:
    publicdata = "PublicData"
    _protecteddata = "Preotecteddata"
    __Privatedata = "privatedata"

    def private(self):
        print(f"Private data of Base Class : {self.__Privatedata}")

    
class Derived(Base):
    def AccesProtectedData(self):
        print(f"Accessing Protested data from Base Class {self._protecteddata}")

dobj = Derived()
print(dobj.publicdata)
dobj.private()
dobj.AccesProtectedData()