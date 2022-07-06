from utils import Utils
from schemas import IdSchema


class IdServices(IdSchema, Utils):

    def get_patent_code(self):
        """
        Return Patent code from id to client
        """
        return self._convert_id_to_patent()

    def _convert_id_to_patent(self):
        """
        Get the patent code from id
        """
        cuenta: function = self._generate_secuence()
        result: str = ''

        for _ in range(self.id_code):
            result = next(cuenta)

        return result
