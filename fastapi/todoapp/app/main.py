from fastapi import FastAPI, HTTPException
from app.models import Todo

app = FastAPI()

todo_list = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI To-Do App"}

@app.post("/todos/")
def create_todo(todo: Todo):
    # Check if todo with same ID already exists
    for item in todo_list:
        if item.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todo_list.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

@app.get("/todos/")
def get_all_todos():
    return todo_list

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for item in todo_list:
        if item.id == todo_id:
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            todo_list[index] = updated_todo
            return {"message": "Todo updated successfully", "todo": updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            del todo_list[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
