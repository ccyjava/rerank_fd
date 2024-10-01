from flask import Flask, render_template, request, redirect, url_for, jsonify
import random

app = Flask(__name__)

# Simulated image database with sample images
IMAGES = [
    {'id': 1, 'url': 'https://via.placeholder.com/150?text=Image+1', 'likes': 0, 'dislikes': 0, 'comments': []},
    {'id': 2, 'url': 'https://via.placeholder.com/150?text=Image+2', 'likes': 0, 'dislikes': 0, 'comments': []},
    {'id': 3, 'url': 'https://via.placeholder.com/150?text=Image+3', 'likes': 0, 'dislikes': 0, 'comments': []},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    # Simulate image search by shuffling the sample images
    results = random.sample(IMAGES, len(IMAGES))
    return render_template('search_results.html', query=query, results=results)

@app.route('/like', methods=['POST'])
def like_image():
    image_id = int(request.form['image_id'])
    action = request.form['action']
    
    for img in IMAGES:
        if img['id'] == image_id:
            if action == 'like':
                img['likes'] += 1
            elif action == 'dislike':
                img['dislikes'] += 1
            break
    return jsonify(success=True)

@app.route('/comment', methods=['POST'])
def comment_image():
    image_id = int(request.form['image_id'])
    comment = request.form['comment']
    
    for img in IMAGES:
        if img['id'] == image_id:
            img['comments'].append(comment)
            break
    return jsonify(success=True)

@app.route('/refine', methods=['POST'])
def refine():
    # Simulate reranking based on likes and dislikes
    refined_results = sorted(IMAGES, key=lambda x: x['likes'] - x['dislikes'], reverse=True)
    return render_template('search_results.html', query='Refined results', results=refined_results)

if __name__ == '__main__':
    app.run(debug=True)
