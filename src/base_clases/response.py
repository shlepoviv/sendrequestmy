class Response:
    def __init__(self,response) -> None:
        self.response = response
        self.response_data = response.json()['data']
        self.status_code = response.status_code

    def valisete_status_code(self,status_code):
        if isinstance(status_code,list):
            assert self.status_code in status_code , self
        else:
            assert self.status_code == status_code , self

    def validete_data(self,schema):
        if isinstance(self.response_data,list):
            for c in (self.response_data):
                schema.model_validate(c)
        else:
            schema.model_validate(self.response_data)
    
    def __str__(self) -> str:
        return f'\n'\
            f'Status code= {self.status_code} \n'\
            f'Response data= {self.response_data}'

    
    