

from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel

from dataclasses import dataclass
from typing import Generic, List, TypeVar

T = TypeVar('T')

@dataclass
class PaginationModel:
    page_num: int
    page_size: int

@dataclass
class PaginationListResponse(Generic[T]):
    total: int
    page_num: int
    page_size: int
    data: List[T]