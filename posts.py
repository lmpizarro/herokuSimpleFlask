class Posts():
    def __init__(self):
        self.posts = [{'title':"Man must explore, and this is exploration at its greatest", 
                       'subtitle':"Problems look mighty small from 150 miles up",
                       'content':"",
                       'date':"July 8, 2013"}, 
                      {'title':"I believe every human has a finite number of heartbeats. I don't intend to waste any of mine.", 
                       'subtitle':"", 
                       'content':"",
                       'date':"July 8, 2011"}, 
                      {'title':"Science has not yet mastered prophecy", 
                       'subtitle':"We predict too much for the next year and yet far too little for the next ten.", 
                       'content':"",
                       'date':"July 8, 2012"},
                      {'title':"Failure is not an option", 
                       'subtitle':"Many say exploration is part of our destiny, but it's actually our duty to future generations.",
                       'content':"",
                       'date':"July 8, 2014"}
                    ]
        pass
    def add_post (self, title, subtitle):
        pass
        date = "2015-05-20"
        self.posts.append({'title':title, 'subtitle':subtitle, 'date':date})


def test ():
    posts = Posts()
    posts.add_post("hola mundo", "probando la insercion de posts")
    for post in posts.posts:
        print post['title']
        print post['subtitle']


#test()
