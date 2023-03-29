from dataclasses import dataclass


@dataclass
class Config:
    token: str = ''
    pay_token: str = ''
    admin: int = None


