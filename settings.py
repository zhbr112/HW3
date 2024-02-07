

class settings:
    __first_name = ""
    __INN=None
    __BIK=None
    __score=None
    __cor_score=None
    __name=""
    __type_ownership=""

    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()
        
    @property
    def INN(self):
        return self.__INN
    
    @INN.setter
    def INN(self, value: str):

        if not isinstance(value, int) or len(self.INN)!=12:
            raise Exception("Некорректный аргумент!")
        
        self.__INN = value.strip()

    @property
    def BIK(self):
        return self.__BIK
    
    @BIK.setter
    def BIK(self, value: str):

        if not isinstance(value, int) or len(self.BIK)!=9:
            raise Exception("Некорректный аргумент!")
        
        self.__BIK = value.strip()

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value: str):

        if not isinstance(value, int):
            raise Exception("Некорректный аргумент!")
        
        self.__score = value.strip()

    @property
    def cor_score(self):
        return self.__cor_score
    
    @cor_score.setter
    def cor_score(self, value: str):

        if not isinstance(value, int):
            raise Exception("Некорректный аргумент!")
        
        self.__cor_score = value.strip()
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__name = value.strip()

    @property
    def type_ownership(self):
        return self.__type_ownership
    
    @type_ownership.setter
    def type_ownership(self, value: str):

        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__type_ownership = value.strip()