from pydantic import Field
from swarmauri.standard.messages.base.MessageBase import MessageBase

class HumanMessage(MessageBase):
    content: str
    role: str = Field(default='user')