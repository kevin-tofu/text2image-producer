
import os
from fastapi import FastAPI, HTTPException, Depends
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

from src.routes import router
from src.config import config_org as config


app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = ["*"]
# origins = [
#     "http://localhost",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


serverinfo = {
    "version": config.app_version,
    "manager": config.app_manager
}


# https://qiita.com/Seo-4d696b75/items/6fc3792d034c2a01b830

# from fastapi.security import OAuth2PasswordBearer
# from firebase_admin import auth
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         decoded_token = auth.verify_id_token(token)
#         user = await auth.get_user(decoded_token['uid'])
#         return user
#     except:
#         raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# @app.get("/users/me")
# async def read_users_me(current_user: auth.UserRecord = Depends(get_current_user)):
#     return {"user_id": current_user.uid, "email": current_user.email}


@app.get("/")
def root():
    return serverinfo

app.include_router(router)

if __name__ == "__main__":

    
    import uvicorn
    import argparse

    myport = config.app_port
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-P', type=int, default=myport, help='port for http server')
    args = parser.parse_args()

    print("port: ", args.port)
    uvicorn.run('server:app', host="0.0.0.0", port=args.port)
