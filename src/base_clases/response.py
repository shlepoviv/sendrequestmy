from src.enums.global_enums import GLOBAL_ERORR_MASSEGE

class Response:
    def __init__(self,response) -> None:
        self.response = response
        self.response_data = response.json()['data']
        self.status_code = response.status_code

    def valisete_status_code(self,status_code):
        if isinstance(status_code,list):
            assert self.status_code in status_code , GLOBAL_ERORR_MASSEGE.WRONG_COdE.value
        else:
            assert self.status_code == status_code

    def validete_data(self,schema):
        if isinstance(self.response_data,list):
            for c in (self.response_data):
                schema.model_validate(c)
        else:
            schema.model_validate(self.response_data)

    
    