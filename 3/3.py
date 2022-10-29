from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def hello():
    return "hello world"

@app.get("/html")
async def html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SA practical</title>
</head>
<body>
    this is a sa practical Exam. this is a web service and you can read this and give me marks please. 
    end this suffuring and let me goooooooo.......  
</body>
</html>"""
    return HTMLResponse(html)

######################################
#   How to run
#   install fastAPI and uvidorn 
#   pip install fastapi 
#   pip install uvicorn
#   
#   make sure name of file is server.py
#   uvicorn server:app --reload
#
