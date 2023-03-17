from typing import NamedTuple, List

class ValidLogin(NamedTuple):
  email: str
  password: str


valid_logins: List[ValidLogin] = []