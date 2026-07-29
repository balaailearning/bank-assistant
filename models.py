from pydantic import BaseModel,Field
from datetime import date

class Expense(BaseModel):
    category : str = Field(description="catogory of expenses"),
    description : str = Field(description="expense description"),
    amount : float = Field(gt=0 ,description="amount spend"),
    