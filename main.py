from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

app = FastAPI() # создаем экземпляр приложения через конструктор

# функция-обработчик корневого GET-запроса вместе с методом-декоратором app.get

@app.get("/")
async def get_root():
    page = "<h1>Hello World!</h1>" # текст ответа сервера
    return HTMLResponse(content=page)

# функция-обработчик импровизированного GET-запроса страницы вместе с методом-декоратором app.get

@app.get("/pages/{page_number}")
async def get_page(page_number):
    return JSONResponse({"page_number": page_number})

# функция-обработчик импровизированного GET-запроса пользователя вместе с методом-декоратором app.get

@app.get("/members/{member_number}")
async def get_page(member_number):
    return JSONResponse({"member_number": member_number})

# функция-обработчик импровизированного POST-запроса пользователя вместе с методом-декоратором app.post

@app.post("/logout/")
async def post_logout(member_number):
    return JSONResponse({"member_number": member_number, "status": "OK"})