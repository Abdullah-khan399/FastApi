
from fastapi import FastAPI
import uvicorn
from MyFastApi.app.api.v1 import api_router



app = FastAPI(title="MyFastApi")
app.include_router(api_router, prefix="/MyFastApi/app/v1")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)