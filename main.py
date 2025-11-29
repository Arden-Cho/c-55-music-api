from fastapi import *

import data
import key
from data import Music
from sort_order import SortOrder

app = FastAPI(title="第 55 屆分區技能競賽 - Android 程式設計")


@app.get("/music/list", name="取得音樂列表")
def music_list(sort_order: SortOrder, filter_term: str | None = None,
               api_key: str = Depends(key.API_KEY_HEADER)) -> list[Music]:
    key.validate(api_key)
    return data.MUSIC_LIST
