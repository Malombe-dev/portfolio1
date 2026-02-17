from flask import *

# create an instance pf the class
app =Flask(__name__)
PROJECTS= {
    'project-one':{
        'id' : 'project-one',
        'title' : 'E-commerce platform',
        'short_description': 'A full-stack e-commerce platform with payment integration',
        'image' : 'p1.jpg',
        'technologies' : ['Flask', 'React', 'PostgreSQL', 'Stripe API'],
        'description' : 'Built a comprehensive e-commerce solution from scratch, handling everything from product management to secure payment processing. The platform features a modern React frontend with a Flask REST API backend.',
        'features' : [
            'User authentication and authorization',
            'Product catalog with search and filtering',
            'Shopping cart and checkout system',
            'Stripe payment integration',
            'Admin dashboard for inventory management',
            'Order tracking and email notifications'
        ],
        'challenges' : 'The main challenge was implementing a secure payment flow while maintaining a smooth user experience. I solved this by integrating Stripe\'s payment intents API and implementing proper error handling.',
        'github' : 'https://github.com/yourusername/ecommerce-platform',
        'live_demo' : 'https://demo-ecommerce.example.com'
    }
}
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
        # pass the simplified project data here 
        {
            'id' : project['id'],
            'title' : project['title'],
            'description' :project['short_description'],
            'image' : project['image']
        }
        for project in PROJECTS.values()
        
    ]

    return render_template('portfolio.html',projects=projects)    
# add a route to acces each project by ID 
@app.route('/project/<project_id>')
def project_details(project_id):
    # get  SPECIFIC PROJECT
    project = PROJECTS.get(project_id)
    if project is None:
        abort(404)
    return render_template('project_detailss.html',project=project)
if __name__ == '__main__':
    app.run(debug=True)