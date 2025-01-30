from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/callback")
async def callback(request: Request):
    # Retrieve the authorization code
    auth_code = request.query_params.get('code')
    if auth_code:
        return JSONResponse(content={"Authorization Code": auth_code}, status_code=200)
    else:
        return JSONResponse(content={"detail": "No authorization code found."}, status_code=400)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)