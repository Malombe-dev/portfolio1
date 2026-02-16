from flask import Flask,render_template

# create an instance pf the class
app =Flask(__name__)

# routes/
@app.route('/')
def index():
    return render_template('index.html')
# other routes 

# about route 
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    # portfolio details 
    projects = [
        {
            'id' : 'project-one',
            'title' : 'My first website',
            'description' : 'A personal portfolio website biult wit css and html',
            'image' : 'p1.jpg'
        }
        
    ]

    return render_template('portfolio.html',projects=projects)    


if __name__ == '__main__':
    app.run(debug=True)