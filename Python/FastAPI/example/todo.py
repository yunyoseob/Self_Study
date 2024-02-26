from fastapi import APIRouter

todo_router = APIRouter()

todo_list=[]

# http -v GET http://127.0.0.1:8000/todo 
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos":todo_list
    }

# http -v POST http://127.0.0.1:8000/todo name=admin   
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added Successfully"
    }