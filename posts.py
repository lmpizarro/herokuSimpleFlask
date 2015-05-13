class Posts():
    def __init__(self):
        self.posts = [{'title':"Este es un post de prueba", 
                       'subtitle':"El problema con los posts es que tienen vidautil corta",
                       'content':"bmnbmnb bmnbmnb bmnbmnb bmnbmnb bmnbmnb bmnbmnb bmnbmnb bmnbmnb bmnbmnb .........",
                       'date':"July 8, 2013", 'user':"lucho"},

                      {'title':"Man must explore, and this is exploration at its greatest", 
                       'subtitle':"Problems look mighty small from 150 miles up",
                       'content':"xioxioxioxio   xioxioxioxio     xioxioxioxio     xioxioxioxio     xioxioxioxio ",
                       'date':"July 8, 2013", 'user':"silvi"}, 
                      {'title':"I believe every human has a finite number of heartbeats. I don't intend to waste any of mine.", 
                       'subtitle':"", 
                       'content':"ziozioziozio ziozioziozio ziozioziozio ziozioziozio ziozioziozio ziozioziozio ziozioziozio ziozioziozio ",
                       'date':"July 8, 2011", 'user':"nacho"}, 
                      {'title':"Science has not yet mastered prophecy", 
                       'subtitle':"We predict too much for the next year and yet far too little for the next ten.", 
                       'content':"yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio yioyioyio ",
                       'date':"July 8, 2012", 'user':"mati"},
                      {'title':"Failure is not an option", 
                       'subtitle':"Many say exploration is part of our destiny, but it's actually our duty to future generations.",
                       'content':"Xpuiioytogva  Xpuiioytogva  Xpuiioytogva  Xpuiioytogva  Xpuiioytogva  Xpuiioytogva  Xpuiioytogva  ",
                       'date':"July 8, 2014", 'user':"lari"}
                    ]
        pass
    def add_post (self, title, subtitle):
        pass
        date = "2015-05-20"
        self.posts.append({'title':title, 'subtitle':subtitle, 'date':date})

    def get_all (self):
        return self.posts[1:]

    def get_one (self, index):
        return self.posts[index]

def test ():
    posts = Posts()
    posts.add_post("hola mundo", "probando la insercion de posts")
    for post in posts.posts:
        print post['title']
        print post['subtitle']


#test()
