from src.domain.dtos.update_user_dto import UpdateUserDTO
from typing import Dict
from abc import ABC, abstractmethod

class UpdateUser(ABC):

    @abstractmethod
    def update(self, username:str, update_params:Dict) -> UpdateUserDTO:pass