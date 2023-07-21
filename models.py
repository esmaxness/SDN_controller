from pydantic import BaseModel


class RinaManagerModel(BaseModel):
    name: str
    description: str
    socket_path: str
    templates_path: str


class ManagementAgentModel(BaseModel):
    name: str
    rol: str
    url: str
    systemId: int

class DifCoreModel(BaseModel):
    systemId: int
    sliceId: int

class DifModel(BaseModel):
    difTemplate: str

class IpcpModel(BaseModel):
    systemId: int
    ipcpTemplate: str

class IpcpIdModel(BaseModel):
    systemId: int
    ipcpId: int