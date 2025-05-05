# htmlxpoc



# 1. 개요

HTMLX(또는 [htmx](https://htmx.org/))는 HTML 속성만으로 서버와의 상호작용(AJAX, WebSocket, SSE 등)을 쉽게 구현할 수 있게 해주는 JavaScript 라이브러리이다. 클라이언트 측 JavaScript 없이도 동적인 웹 페이지를 만들 수 있다는 점에서 매우 직관적이다.



# 2. Hello World

간단한 “Hello World” 버튼 → 서버에서 텍스트 가져오기



## 1) 서버 (Python Flask 예시)



```
# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head>
        <script src="https://unpkg.com/htmx.org@1.9.10"></script>
      </head>
      <body>
        <button hx-get="/hello" hx-target="#result">Say Hello</button>
        <div id="result"></div>
      </body>
    </html>
    """

@app.route("/hello")
def hello():
    return "Hello, HTMX!"

if __name__ == "__main__":
    app.run(debug=True)
```

* hx-get="/hello": 버튼 클릭 시 /hello 엔드포인트로 GET 요청 보냄.
* hx-target="#result": 응답 받은 내용을 <div id="result">에 삽입함.



## 2) 실행 방법

```
pip install flask
python hello.py
```

웹 브라우저에서 http://localhost:5000 접속.









# 3. TODO list 예제

**폼 제출**, **리스트 렌더링**, **동적 갱신** 같이 실전에서 많이 사용하는 간단한 TODO 리스트를 살펴보자.



**기능 설명**

* 입력 폼으로 TODO 추가
* 서버 응답으로 리스트 갱신



## 1) Flask 서버 코드 (app.py)



```sh

$ cd ~/song/htmx

$ cat > app.py

```



```python
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
    app.run(debug=True, host="0.0.0.0", port=5000)
```



HTMLX 핵심 포인트

| **속성**  | **의미**                                      |
| --------- | --------------------------------------------- |
| hx-post   | 서버로 POST 요청 보냄                         |
| hx-target | 응답을 삽입할 대상 요소 선택자                |
| hx-swap   | 응답을 삽입할 방식 (outerHTML, innerHTML, 등) |



#### 임시코드

```html



    <div id="todo-list">
      <ul>
        {% for todo in todos %}
          <li>{{ todo }}</li>
        {% endfor %}
      </ul>
    </div>




    <div id="todo-list">
      <ul>
        {% for todo in todos %}
          <li>
            {{ todo.text }}
            <button hx-delete="/delete/{{ loop.index0 }}" hx-target="closest li" hx-swap="outerHTML">❌</button>
          </li>
        {% endfor %}
      </ul>
    </div>



```











## 2) 설치 및 실행

```
pip install flask
python app.py
```

브라우저에서 http://localhost:5000 접속





**📘 확장 아이디어**

​	•	버튼으로 TODO 삭제 (hx-delete)

​	•	완료 상태 토글 (hx-patch)

​	•	무한스크롤 (hx-trigger="revealed")





# 11. python 실행 환경



## 1) python pod 실행

```sh

$ kubectl -n temp create deploy python --image=python -- sleep 365d

$ kubectl -n temp exec -it deploy/python -- bash

```



## 2) port-forward

```sh

$ kubectl port-forward pod/flask-htmx-5cbb8f5d6d-xxxx 5000:5000

```

