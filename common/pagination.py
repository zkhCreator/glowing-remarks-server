from dataclasses import dataclass
from typing import Generic, List, TypeVar
from sqlalchemy.sql import Select

T = TypeVar('T')

@dataclass
class PaginationModel:
    page_num: int
    page_size: int
    
    def paginate(self, query: Select[T]) -> Select[T]:
        return query.limit(self.page_size).offset(self.page_num * self.page_size)

@dataclass
class PaginationListResponse(Generic[T]):
    total: int
    page_num: int
    page_size: int
    data: List[T]