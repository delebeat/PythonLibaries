__author__='Delebeat'


class post(object):
    def __init__(self,title,content,author,blog_id,id,date):
        # self.title="This is my title"
        # self.content="This is some content"
        self.title=title
        self.content=content
        self.author=author
        self.blog_id=blog_id
        self.id=id
        self.create_date=date

    def save_to_mongo(self):
        pass

    def json(self):
        return{
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'create':self.create_date
        }
