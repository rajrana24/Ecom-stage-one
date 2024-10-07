from flask import Flask, render_template

app = Flask(__name__)

STARTUPS = [ 
    { 'id': 1 ,
            'name': '1. open ai ',
           'location':'sillicon valley,USA ',
    }, 
    {
        'id': 2 ,
           'name':'2. sapaceX',
           'location':'san francisco,USA ',
    },       
       
    {  
        'id': 3 ,
       'name':'3. genhack ai ',
       'location':'singapore,china',
    },     
            
    {'id': 4 ,
           'name':'4. hugging face',
           'location':'california,USA '
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html' ,   
                           startups =STARTUPS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
