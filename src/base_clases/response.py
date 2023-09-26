class Response:
    def __init__(self,response) -> None:
        self.response = response
        self.response_data = response.json()
        self.status_code = response.status_code

    def find_in_respose_data(self,data_path):
        '''
        Returns the find element in response data
        data_path - path list or name element
        if element don't find - return None
        '''
        if isinstance(data_path, list):
            temp = self.response_data
            for i in data_path:
                temp = temp.get(i,None)
                if not temp:
                    return None
            return temp
        else:
            return self.response_data.get(data_path,None)
                    

    def valisete_status_code(self,status_code):
        '''
        Chek status code 
        status_cod int or list(int)
        '''
        if isinstance(status_code,list):
            assert self.status_code in status_code , self
        else:
            assert self.status_code == status_code , self

    def validete_data(self,schema):
        '''
        Validates response data using a schema
        '''
        if isinstance(self.response_data,list):
            for c in (self.response_data):
                schema.model_validate(c)
        else:
            schema.model_validate(self.response_data)
    
    def __str__(self) -> str:
        return f'\n'\
            f'Status code= {self.status_code} \n'\
            f'Response data= {self.response.url} \n'\
            f'Response data= {self.response_data}'
            

    
    