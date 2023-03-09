from flask_app.config.mysqlconnection import connectToMySQL

DB = "twfdb"

class Blog:
    def __init__(self, data):
        self.id = data["id"]
        self.admin_id = data["admin_id"]
        self.title = data["title"]
        self.author = data["author"]
        self.content = data["content"]
        self.created_at  = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO blogs (admin_id, title, author, content) VALUES (%(admin_id)s,%(title)s,%(author)s,%(content)s,)"
        return connectToMySQL(DB).query_db(query, data)