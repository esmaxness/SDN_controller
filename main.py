from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import *
from rina.coreManager import RinaCoreManager
from rina.manager import RinaManager


app = FastAPI()

maManager = RinaCoreManager()
manager = RinaManager('/var/run/nmconsole.sock', '/tmp/DifTemplates') 
manager.connect()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>SDN Controller</title>
        </head>
        <body>
            <h1>SDN Controller that management RINA nodes by using 
            the RINA SouthBound Driver</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/register_ma")
def post_register_ma(rinaMa: ManagementAgentModel):
    rinaMa_dict = dict(rinaMa)
    print(rinaMa_dict["name"])

    #create a MA object.
    ret = maManager.add_system(rinaMa_dict["url"] , rinaMa_dict["name"], rinaMa_dict["rol"] , str(rinaMa_dict["systemId"]))
    if ret == 0:
        html_content = """
    <html>
        <body>
            <h1>Management agent registered successfully</h1>
        </body>
    </html>
    """
        return HTMLResponse(content=html_content, status_code=201)
    
    return HTMLResponse(status_code=500)

@app.get("/list_ma")
def get_list_ma():
    listNodes = maManager.list_systems()
    return listNodes

@app.get("/list_systems")
def get_list_systems():
    systems = manager.list_systems()
    print(systems)
    print(type(systems))

    return systems # json.dump([system.dict for system in systems])
    
@app.post("/create_dif")
def post_create_dif(requestDif: DifModel):
    requestDif_dict = dict(requestDif)
    manager.create_dif(requestDif_dict["difTemplate"])
    return HTMLResponse(status_code=200)

@app.post("/create_ipcp")
def post_create_dif(requestIpcp: IpcpModel):
    requestIpcp_dict = dict(requestIpcp)
    manager.create_ipcp(str(requestIpcp_dict["systemId"]), requestIpcp_dict["ipcpTemplate"]  )
    return HTMLResponse(status_code=200)

    
@app.put("/destroy_dif")
def put_create_dif():
    return HTMLResponse(status_code=200)

@app.put("/destroy_ipcp")
def put_create_dif():
    return HTMLResponse(status_code=200)

@app.post("/create_l2VPN")
def post_create_l2VPN(requestDif: DifCoreModel):
    requestDif_dict = dict(requestDif)
    maManager.create_dif(str(requestDif_dict["systemId"]), str(requestDif_dict["sliceId"] ) )

    return HTMLResponse(status_code=200)

@app.put("/destroy_l2VPN")
def put_destroy_l2VPN():
    return HTMLResponse(status_code=200)
