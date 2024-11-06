from pydantic import BaseModel, constr

class UserModel(BaseModel):
    id: int
    name: constr(min_length=1) # type: ignore
    email: constr(min_length=1) # type: ignore

    # Usando configuração para permitir a conversão ORM diretamente
    class Config:
        from_attributes = True  # Pydantic agora entende instâncias ORM como UserTable
