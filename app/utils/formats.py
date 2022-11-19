import re

class Number:
    @staticmethod
    def check(content: str) -> bool:
        # Одни цифры 79******
        if re.match(r'79\d+$', content) != None:
            return True
        
        return False

class Fio:
    @staticmethod
    def check(content: str) -> bool:
        # Фамилия Имя Отчество
        if re.match(r'[а-яА-Я]+\s+[а-яА-Я]+\s+[а-яА-Я]+$', content) != None:
            return True

        return False

class Surname:
    @staticmethod
    def check(content: str) -> bool:
        # Фамилия И.О.
        if re.match(r'[а-яА-Я]+\s+[а-яА-Я]\.\s*[а-яА-Я]\.$', content) != None:
            return True
        
        return False

class Organization:
    @staticmethod
    def check(content: str) -> bool:
        # Тип компании ООО, ОАО, ЗАО, АО, ПАО, ФГУП
        if re.match(r'(ООО|ОАО|ЗАО|ПАО|АО|ФГУП', content) != None:
            return True

        return False