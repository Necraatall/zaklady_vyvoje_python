from typing import Dict, Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> Dict[str,str]:
    """_summary_

    Returns:
        Dict[str,str]: vraci hlavni object
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """_summary_

    Args:
        item_id (int): _description_
        q (Optional[str], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {"item_id": item_id, "q": q}