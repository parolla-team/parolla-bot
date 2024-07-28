from abc import ABC, abstractmethod
from typing import Any


class BaseChatClient(ABC):
    @abstractmethod
    def get_history(self, channel_id: str) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_last_message(self, channel_id: str) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_last_24h_messages(self, channel_id: str) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_channel_name(self, channel_id: str) -> str:
        pass

    @abstractmethod
    def get_participants(self, channel_id: str) -> list[str]:
        pass

    @abstractmethod
    def send_message(self, channel_id: str, message: str) -> None:
        pass

    @abstractmethod
    def delete_message(self, channel_id: str, message_id: str) -> None:
        pass

    @abstractmethod
    def edit_message(self, channel_id: str, message_id: str, new_message: str) -> None:
        pass

    @abstractmethod
    def get_unread_messages(self, channel_id: str) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def mark_message_as_read(self, channel_id: str, message_id: str) -> None:
        pass
