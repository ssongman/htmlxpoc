
posts = []
counter = 1

def get_all_posts():
    return posts

def get_post(post_id):
    return next((p for p in posts if p["id"] == post_id), None)

def create_post(title, content):
    global counter
    post = {"id": counter, "title": title, "content": content}
    posts.append(post)
    counter += 1
    return post

def update_post(post_id, title, content):
    post = get_post(post_id)
    if post:
        post["title"] = title
        post["content"] = content
    return post

def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
