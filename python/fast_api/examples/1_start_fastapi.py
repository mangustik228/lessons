import fastapi 
import sys

print('start print param')
for param in sys.argv:
    print(param)
print('finish print param')


api_m = fastapi.FastAPI()

@api_m.get('/hello')
def api_hello():
    return {'hello':'from_api'}