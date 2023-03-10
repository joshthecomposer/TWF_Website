from flask import jsonify, send_from_directory, render_template, json
from flask_app import application as app
from flask_app.models.blog import Blog
import feedparser
import json

EPISODES = feedparser.parse("https://feeds.redcircle.com/7404a6c6-18b8-4f30-a819-468fb013bff2?fbclid=IwAR2jIZ2aJUjpEZL7tOHNtHr8R6OhgfKSQl7Op5OT8MwAuLT2dCxL38y1uqs")

# Path for our main Svelte page
@app.route("/")
@app.route("/blogs")
@app.route("/episodes")
@app.route("/about")
@app.route("/subscribe")
@app.route("/contact")
def base():
    return send_from_directory('./client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def directory(path):
    return send_from_directory('./client/public', path)

@app.route("/api/episodes/latest", methods=["GET"])
def latest():
    e = EPISODES.entries[0]
    return jsonify(e)

@app.route("/api/episodes", methods = ["GET"])
def all_episodes():
    return jsonify(EPISODES.entries)

@app.route("/api/blogs", methods=["GET"])
def api_all_blogs():
    all_blogs = Blog.get_all()
    return jsonify(all_blogs)