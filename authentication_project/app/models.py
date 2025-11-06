from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int]=None
    description:Optional[str]=None