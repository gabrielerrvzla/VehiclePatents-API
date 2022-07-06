from utils import Utils
from schemas import PatentSchema


class PatentServices(PatentSchema, Utils):
    def get_id(self):
        return self._convert_patent_to_id()

    def _convert_patent_to_id(self):
        """ 
        Get id from patent code
        """
        cuenta: function = self._generate_secuence()
        result: str = ''
        counter: int = 1

        """ 
        TODO: Better logic to get the id, beacuse the code it's not efficient
        """
        while True:
            result = next(cuenta)
            if self.patent_code == result:
                break
            counter += 1

        return counter
