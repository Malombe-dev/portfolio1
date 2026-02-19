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
        },
        'project-two': {
            'id': 'project-two',
            'title': 'Task Management System',
            'short_description': 'A collaborative task management tool for teams',
            'image': 'p2.jpg',
            'technologies': ['Python', 'Django', 'Vue.js', 'Redis'],
            'description': 'Developed a robust task management system that allows teams to collaborate efficiently. Features real-time updates, drag-and-drop interfaces, and comprehensive reporting tools.',
            'features': [
                'Real-time collaboration with WebSockets',
                'Kanban board with drag-and-drop',
                'Team management and permissions',
                'File attachments and comments',
                'Advanced filtering and search',
                'Analytics dashboard with charts'
            ],
            'challenges': 'Implementing real-time updates across multiple users was complex. I used WebSockets with Redis pub/sub to ensure all team members saw updates instantly without performance degradation.',
            'github': 'https://github.com/yourusername/task-manager',
            'live_demo': 'https://demo-tasks.example.com'
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
    return render_template('project_details.html',project=project)

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True,port='5001')