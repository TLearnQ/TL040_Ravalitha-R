
from asyncio import Handle


endpoint = []

def router(req):
    method,path,data = req.get("method"), req.get("path"), req.get("data",{})
    if method=="GET" and path=="/items":
            return(endpoint)
    if method=="POST" and path=="/items":
        newendpoint={"id":"length"+1,"name":"user"}
        router.append(newendpoint);
        return(newendpoint)
    if method=="GET" and path=="/items":
        
print(Handle({"method":"GET","endpoint":"/users","data":{"id":101}}))


