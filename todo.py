from flask import Flask, request, render_template_string

app = Flask(__name__)

# 딕셔너리 기반의 todos 리스트
todos = []

# TODO 리스트 부분만 렌더링하는 함수
def render_todo_list(todos):
    return render_template_string("""
    <div id="todo-list">
      <ul>
        {% for todo in todos %}
          <li>
            {{ todo.text }}
            <button 
              hx-delete="/delete/{{ loop.index0 }}" 
              hx-target="#todo-list"
              hx-swap="outerHTML"
            >❌</button>
          </li>
        {% endfor %}
      </ul>
    </div>
    """, todos=todos)

@app.route("/")
def index():
    return render_template_string("""
    <html>
    <head>
      <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    </head>
    <body>
      <h1>My TODOs</h1>

      <form hx-post="/add" hx-target="#todo-list" hx-swap="outerHTML">
        <input type="text" name="item" placeholder="Enter a todo" required>
        <button type="submit">Add</button>
      </form>

      {{ todo_list|safe }}
    </body>
    </html>
    """, todo_list=render_todo_list(todos))

@app.route("/add", methods=["POST"])
def add():
    item = request.form.get("item")
    if item:
        todos.append({"text": item})
    return render_todo_list(todos)

@app.route("/delete/<int:index>", methods=["DELETE"])
def delete(index):
    print(f"[DELETE] 요청됨 - index: {index}")
    print(f"[BEFORE] todos: {todos}")
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"[AFTER] 삭제된 항목: {removed}")
        print(f"[AFTER] todos: {todos}")
    else:
        print("[WARN] 유효하지 않은 index")
    return render_todo_list(todos)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)