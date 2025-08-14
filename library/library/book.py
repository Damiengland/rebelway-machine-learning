from dataclasses import dataclass, field
from typing import Optional
from library.rand_num_utils import RandomUtils

@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    summary: Optional[str] = field(default="")
    id: str = field(default_factory=RandomUtils.generate_random_id)

    @property
    def get_summary(self) -> str:
        """
        Returns the summary of the book. 
        """
        return self.summary if self.summary else "No summary available."
    
    @property
    def search_string(self) -> str:
        """
        Returns a string that can be used for searching the book.
        """
        return f"{self.title} {self.author} {self.genre}"

