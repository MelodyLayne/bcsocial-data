from flask import Flask
from utilities.users.clout_scoring import user_cat_score, user_vote_score, user_pop_score
from utilities.categories.category_scoring import cat_score
app = Flask(__name__)

@app.route('/')
def index():
    return {
        'user_cat_score': user_cat_score(),
        'user_vote_score': user_vote_score(),
        'user_pop_score': user_pop_score(),
        }, 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
