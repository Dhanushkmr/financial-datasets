from typing import Optional

from pydantic import BaseModel


class DatasetItem(BaseModel):
    question: str
    answer: str
    context: str
    chunks: Optional[str] = None


class Dataset(BaseModel):
    items: list[DatasetItem]
