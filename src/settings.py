

class Settings:
    __first_name = ""
    __second_name = ""
    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()
        
    @property
    def second_name(self):
        return self.__second_name
    
    @first_name.setter
    def second_name(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__second_name = value.strip()
        
        