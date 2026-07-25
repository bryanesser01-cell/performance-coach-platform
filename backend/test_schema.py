import datetime as dt

from pydantic import BaseModel


class Test(BaseModel):
    date: dt.date | None = None


print(Test.model_json_schema())
