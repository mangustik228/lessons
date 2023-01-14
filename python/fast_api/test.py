from pydantic import BaseModel

class Test(BaseModel):
    id:int 
    name:str 
    sex:str 

test = {'id': 25, 'name':'Vasiliy', 'sex':'m'}

a = Test(**test)
print(type(a))
print(a)
print(a['id'])