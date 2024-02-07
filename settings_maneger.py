import os
import json
import uuid
from settings import settings


class settings_maneger(object):
    __file_name="settings.json"
    __unique_number=None
    __data={}
    __settings=settings()

    def __new__(cls):
        if not hasattr(cls,"instance"):
            cls.instance = super(settings_maneger,cls).__new__(cls)
        return cls.instance
    
    def convert(self):
        if len(self.data)==0:
            raise Exception()
        fields=dir(self.__settings.__class__)
        print([i for i in fields if i[0:1]!='_'])
        
        

    def __init__(self):
        self.__unique_number=uuid.uuid4()

    @property
    def unique_number(self):
        return str(self.__unique_number.hex)
    
    @property
    def file_name(self):
        return self.__file_name
    
    @property
    def data(self):
        return self.__data

    def open(self,file_name:str):
        if not isinstance(file_name,str):
            raise Exception()
        
        if file_name=="":
            raise Exception()
        
        self.__file_name=file_name.strip()

        try:
            self.__open()
        except:
            raise Exception()
        
        return True

    def __open(self):
        file_path=os.path.split(__file__)
        settings_file="%s/%s"%(file_path[0],self.__file_name)

        if not os.path.exists(settings_file):
            raise Exception()
        with open(settings_file,"r") as read_file:
            self.__data=json.load(read_file)
            