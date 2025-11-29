from fastapi import *

import key

app = FastAPI()


@app.get("/music/list")
def music_list(api_key: str = Depends(key.API_KEY_HEADER)):
    key.validate(api_key)
    return {"message": "Hello World"}
