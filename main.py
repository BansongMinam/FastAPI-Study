#조건1. GET /orders/{order_id} 경로를 정의해라
#조건2. 경로변수  order_id(정수형)을 매개변수로 받아라
#조건3. 선택적 쿼리 파라미터 pickup(논리형)을 받아라. 이 값이 전달되지 않을 시 None이 되도록 설정
#조건4. order_id와 pickup을 포함하는 응답모델을 BaseModel로 정의해라
#조건5. response_model 옵션을 사용해 해당 응답 모델을 반환하도록 설정해라
#완성된 API의 동작 예시 -요청 GET /orders/5?pickup=true, -응답 {"order_id":5,"pickup":ture}


from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class dmdekqahepf(BaseModel):
    order_id:int
    pickup:bool | None= None
@app.get('/orders/{order_id}', response_model = dmdekqahepf)
def dkssudgktpdy(order_id:int, pickup:bool | None=None):
    return {"order_id": order_id, "pickup":pickup}





