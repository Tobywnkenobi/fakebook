from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return 'Matrix Fakebook'

users = [
    {
    'username':'seanc',
    'email':'seanc@ct.com',
    'posts':[{"body":"Welcome to Flask Week"}]
    },
    {
    'username':'dylans',
    'email':'dylans@ct.com'
    'posts'[{'body':"My favorite Week"}]
    }
]

@app.get('/user')
def get_users():
    return {'users': users}, 200

@app.post('/user')
def create_user():
    user_data = request.get_json()
    user = list(filter(lambda user: user["username"] == user_data['username'],users))[0]
    users['unique identifier'] = user_data
    return user, 200

@app.post('/user/<user_id>')
def update_user():
    user_data = request.get_json()
    try:
        user = users[user_id]
        user['username'] = user_data['username']
        return user, 200
    except KeyError:
        return {'message': 'user not found'}, 400

@app.post('/user')
def delete_user():
    user_data = request.get_json()
    for i, user in enumerate(users):
        if user['username'] == user_data['username']:
            users.pop(i)
            print(users)
        return {'message':f'{user_data}["username"] deleted'}, 202
    
@app.get('/post')
def get_posts():
    return {'posts': posts}
    
    
@app.get('/post/<post_id>')
def edit_posts(post_id):
    post_data = request.get_json()
    if post_id in posts:
        post = posts[post_id]
        post['body'] = post_data['body']
        return post, 200
    return {'message', 'Post not found'}, 400
    
@app.get('/post/<post_id>')
def delete_post(post_id):
    try:
        deleted_post = posts.pop(post_id)
        return {'message':f'{deleted_post["body"]} deleted'}, 202
    except:
        return {'message': 'Post not found'}, 400
    