from flask import render_template

class Post:
    def __init__(self, data, num):
        self.data = data
        self.num = num
    
    def desiredPost(self):
        for post in self.data:
            if post["id"] == int(self.num):  
                return post
        return None

    def getPost(self):
        desiredData = self.desiredPost()
        subtitle = desiredData['subtitle']
        body = desiredData['body']
        return render_template("post.html", subtitle=subtitle, body=body)
    