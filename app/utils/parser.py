from app.utils.formats import Fio, Number, Surname, Organization

import re

class RequestParser:
    @staticmethod
    def execute(query: str) -> dict:
        if Fio.check(query):
            result = re.match('([а-яА-Я]+)\s+([а-яА-Я]+)\s+([а-яА-Я]+)$', query)
            return {
                'surname': result[1],
                'first_name': result[2],
                'last_name': result[3]
            }
        if Surname.check(query):
            return {
                'surname': re.match('[а-яА-Я]+', query)[0]
            }
        if Number.check(query):
            return {
                'number': re.match('\d', query)[0]
            }
        
        return {}