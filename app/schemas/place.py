from typing import Optional
 
from pydantic import BaseModel, AnyHttpUrl
 
# Shared properties
class PlaceBase(BaseModel):
   nombre: str
   precio: Optional[int] = 0
   imagen: Optional[AnyHttpUrl]
 
# Properties to receive on place creation
class PlaceCreate(PlaceBase):
   pass
 
# Properties to receive on place update
class PlaceUpdate(PlaceBase):
   pass
 
# Properties shared by models stored in DB
class PlaceInDBBase(PlaceBase):
   id: int
   #owner_id: int
 
   class Config:
       orm_mode = True
 
# Properties to return to client
class Place(PlaceInDBBase):
   pass
 
# Properties properties stored in DB
class PlaceInDB(PlaceInDBBase):
   pass
