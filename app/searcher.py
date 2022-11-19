from app.models import Human
from app.utils.formats import Fio, Number, Surname
from app.utils.parser import RequestParser

class Searcher:
    @staticmethod
    def execute(session, query: str) -> list:
        # Разбор данных с запроса
        data = RequestParser.execute(query)

        if Fio.check(query):
            print("\n\n\n\nFIO\n\n\n\n")
            humans = session.query(Human).filter(
                Human.surname    == data['surname'] and 
                Human.last_name  == data['last_name'] and
                Human.first_name == data['first_name']
            ).all()

            if humans == None:
                return {}

            result = []
            for human in humans:
                result.append({
                    'surname': human.surname,
                    'first_name': human.first_name,
                    'last_name': human.last_name,
                    'birthdate': str(human.birthdate),
                    'other': human.other
                })
            
            return result

        if Surname.check(query):
            humans = session.query(Human).filter(Human.surname == data['surname']).all()

            if humans == None:
                return {}

            result = []
            for human in humans:
                result.append({
                    'surname': human.surname,
                    'first_name': human.first_name,
                    'last_name': human.last_name,
                    'birthdate': str(human.birthdate),
                    'other': human.other
                })
            
            return result
        
        # if Number.check(query):
            # return session.query(Human).filter(Human.surname == query.)
