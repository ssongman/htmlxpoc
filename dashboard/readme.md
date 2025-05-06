

# 1. 개요



**HTMX + Flask 기반의 CRUD 게시판 (Dashboard)**  프로젝트 

hx-get, hx-post, hx-target, hx-swap 등을 활용하여 **페이지 전체 새로고침 없이**, HTML fragment만 교체하는 구조 이다.





## **📁 프로젝트 구조**

```

htmx_dashboard/
├── app.py
├── models.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── post_form_create.html     # 글쓰기용 폼
│   ├── post_form_edit.html       # 글쓰기용 폼
│   └── post_list_wrapper         # 목록 wrapper
│   └── post_list_fragment.html   # 목록 페이지


```

* HTML은 분리된 템플릿 구조로 유지

* 첫 화면에 게시글 목록이 나타남
* 글쓰기 버튼 클릭 시 form 표시
* 글 작성 후 → 목록 자동 갱신
* 각 글에 ✏️ 수정 / ❌ 삭제 버튼 포함
* 수정 후에도 목록으로 돌아감 (페이지 새로고침 없음)





## 실행



```sh

$ python app.py

```



