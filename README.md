# Flask Portfolio - Student Teaching Plan
## 6 Lessons × 2 Hours Each

---

# 📋 LESSON 1: Project Setup & Home Page (2 hours)

## 🎯 Learning Objectives
- Understand Flask basics and project structure
- Create a basic Flask application
- Build and style the home page

---

## ⏱️ PART 1: Project Setup (30 mins)

### Step 1: Create Project Folder Structure (10 mins)

**What students do:**
1. Create a new folder called `portfolio`
2. Inside it, create these folders and files:

```
portfolio/
├── app.py
├── templates/
└── static/
    ├── css/
    └── images/
```

**Commands (Terminal/Command Prompt):**
```bash
mkdir portfolio
cd portfolio
mkdir templates
mkdir static
mkdir static/css
mkdir static/images
```

---

### Step 2: Install Flask (10 mins)

**What students do:**
```bash
pip install flask
```

**Check installation:**
```bash
flask --version
```

Should show: `Flask 3.x.x`

---

### Step 3: Create First Flask App (10 mins)

**Create file:** `app.py`

**Students type this code:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**Run it:**
```bash
python app.py
```

**Expected:** Error message (no template yet) - this is GOOD! Explain the error.

---

## ⏱️ PART 2: Create Base Template (40 mins)

### Step 4: Create base.html (20 mins)

**Create file:** `templates/base.html`

**Students type:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Portfolio{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">MyPortfolio</a>
        </div>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**🔍 Explain:**
- `{% block title %}` - Template blocks
- `{{ url_for() }}` - Flask's way to link files
- Bootstrap CDN - CSS framework

**✅ TEST:** Run `python app.py` - still error (no index.html)

---

### Step 5: Create index.html (20 mins)

**Create file:** `templates/index.html`

**Students type:**
```html
{% extends 'base.html' %}

{% block title %}Home - My Portfolio{% endblock %}

{% block content %}
<section class="hero">
    <div class="container">
        <div class="row align-items-center min-vh-100">
            <div class="col-lg-6">
                <h1 class="display-3 fw-bold">Hello, I'm <span class="text-primary">John Doe</span></h1>
                <p class="lead">Full Stack Developer</p>
                <p class="text-muted">I build amazing web applications.</p>
                <div class="mt-4">
                    <a href="#" class="btn btn-primary btn-lg">View My Work</a>
                </div>
            </div>
            <div class="col-lg-6">
                <img src="https://via.placeholder.com/500" alt="Profile" class="img-fluid rounded">
            </div>
        </div>
    </div>
</section>
{% endblock %}
```

**🔍 Explain:**
- `{% extends 'base.html' %}` - Template inheritance
- Bootstrap grid system (`container`, `row`, `col`)

**✅ TEST:** 
```bash
python app.py
```
Open browser: `http://127.0.0.1:5000`

**Expected:** See basic home page (NO STYLING YET)

---

## ⏱️ PART 3: Add CSS Styling (30 mins)

### Step 6: Provide CSS File (10 mins)

**Create file:** `static/css/style.css`

**Teacher provides this CSS (students copy/paste):**

```css
/* General Styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex: 1;
}

/* Navbar */
.navbar-brand {
    font-weight: bold;
    font-size: 1.5rem;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* Cards */
.card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: none;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}
```

**✅ TEST:** Refresh browser - see STYLED home page! 🎨

---

### Step 7: Customize Content (10 mins)

**Students change:**
1. Replace "John Doe" with their name
2. Change "Full Stack Developer" to their own title
3. Update the description text

**✅ TEST:** Refresh and see personalized content

---

### Step 8: Experiment with Styles (10 mins)

**Activity:** Students try changing:
- Background gradient colors in CSS
- Font sizes
- Button colors (change `btn-primary` to `btn-success`, `btn-danger`, etc.)

---

## ⏱️ PART 4: Review & Homework (20 mins)

### What We Built:
✅ Flask application structure  
✅ Base template with Bootstrap  
✅ Home page with hero section  
✅ Custom CSS styling  

### 📝 Homework:
1. Personalize ALL text content
2. Find a profile picture and save it as `static/images/profile.jpg`
3. Change the placeholder image to use your photo

**Hint for homework:**
```html
<img src="{{ url_for('static', filename='images/profile.jpg') }}" alt="Profile">
```

---
---

# 📋 LESSON 2: Navigation & Footer (2 hours)

## 🎯 Learning Objectives
- Create reusable template components
- Understand template includes vs extends
- Build responsive navigation and footer

---

## ⏱️ PART 1: Create Navbar Component (45 mins)

### Step 1: Review Homework (5 mins)
- Check if students personalized their home page
- Verify profile images are added

---

### Step 2: Create navbar.html (25 mins)

**Create file:** `templates/navbar.html`

**Students type:**
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/">MyPortfolio</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/portfolio">Portfolio</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/contact">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

**🔍 Explain:**
- Navbar toggler for mobile
- `ms-auto` - margin start auto (pushes nav to right)
- Bootstrap collapse component

---

### Step 3: Update base.html to Use navbar.html (10 mins)

**Edit file:** `templates/base.html`

**REMOVE these lines:**
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/">MyPortfolio</a>
    </div>
</nav>
```

**REPLACE with:**
```html
{% include 'navbar.html' %}
```

**🔍 Explain:**
- `{% include %}` - Inserts another template
- Difference between `extends` and `include`

**✅ TEST:** Refresh browser - navbar still works!

---

### Step 4: Test Mobile Navigation (5 mins)

**Activity:**
1. Resize browser window to mobile size (narrow)
2. Click the hamburger menu (☰)
3. See navigation menu appear

**✅ Expected:** Menu collapses on mobile, works on desktop

---

## ⏱️ PART 2: Create Footer Component (45 mins)

### Step 5: Create footer.html (30 mins)

**Create file:** `templates/footer.html`

**Students type:**
```html
<footer class="bg-dark text-white py-4 mt-5">
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <h5>About</h5>
                <p>A passionate developer creating amazing web experiences.</p>
            </div>
            <div class="col-md-4">
                <h5>Quick Links</h5>
                <ul class="list-unstyled">
                    <li><a href="/" class="text-white">Home</a></li>
                    <li><a href="/about" class="text-white">About</a></li>
                    <li><a href="/portfolio" class="text-white">Portfolio</a></li>
                    <li><a href="/contact" class="text-white">Contact</a></li>
                </ul>
            </div>
            <div class="col-md-4">
                <h5>Follow Me</h5>
                <div class="social-links">
                    <a href="#" class="text-white me-3">GitHub</a>
                    <a href="#" class="text-white me-3">LinkedIn</a>
                    <a href="#" class="text-white">Twitter</a>
                </div>
            </div>
        </div>
        <hr class="bg-white">
        <div class="text-center">
            <p class="mb-0">&copy; 2024 MyPortfolio. All rights reserved.</p>
        </div>
    </div>
</footer>
```

**🔍 Explain:**
- 3-column footer layout
- `list-unstyled` - removes bullet points
- `text-white` - Bootstrap text color

---

### Step 6: Add Footer to base.html (10 mins)

**Edit file:** `templates/base.html`

**Add BEFORE `</body>`:**
```html
{% include 'footer.html' %}
```

**Your base.html should now look like:**
```html
<body>
    {% include 'navbar.html' %}
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    {% include 'footer.html' %}
    
    <script src="..."></script>
</body>
```

**✅ TEST:** Scroll to bottom - see footer!

---

### Step 7: Fix Footer Position (5 mins)

**Problem:** Footer might be in middle of page on short content

**Solution - Edit:** `templates/base.html`

**Change:**
```html
<main>
```

**To:**
```html
<main style="min-height: 80vh;">
```

**✅ TEST:** Footer now sticks to bottom!

---

## ⏱️ PART 3: Style Navigation & Footer (20 mins)

### Step 8: Add CSS for Nav & Footer (10 mins)

**Edit file:** `static/css/style.css`

**Students add at the end:**
```css
/* Navigation */
.nav-link {
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #0d6efd !important;
}

/* Footer */
footer a {
    text-decoration: none;
    transition: opacity 0.3s ease;
}

footer a:hover {
    opacity: 0.8;
}
```

**🔍 Explain:**
- CSS transitions
- `:hover` pseudo-class
- `!important` (use sparingly)

**✅ TEST:** Hover over nav links - see color change!

---

### Step 9: Customize Footer Content (10 mins)

**Activity:** Students update `footer.html`:
1. Change "About" description to match their profile
2. Update copyright year
3. Add their social media links (or use `#` for now)

**✅ TEST:** Refresh and see personalized footer

---

## ⏱️ PART 4: Review & Homework (10 mins)

### What We Built:
✅ Separate navbar component  
✅ Responsive navigation with mobile menu  
✅ Professional footer with 3 columns  
✅ Hover effects on links  

### 📝 Homework:
1. Find your GitHub, LinkedIn, Twitter URLs
2. Replace `#` in footer social links with real URLs
3. BONUS: Add a 4th navigation item of your choice

---
---

# 📋 LESSON 3: About Page (2 hours)

## 🎯 Learning Objectives
- Create new Flask routes
- Work with Bootstrap grid system
- Add and manage images

---

## ⏱️ PART 1: Create About Route (20 mins)

### Step 1: Add About Route to app.py (10 mins)

**Edit file:** `app.py`

**Add after the index route:**
```python
@app.route('/about')
def about():
    return render_template('about.html')
```

**Full app.py should look like:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**🔍 Explain:**
- Routes are URL paths
- Each route needs a function
- Function returns a template

**✅ TEST:** 
1. Click "About" in navbar
2. Expected: Error (template not found)

---

### Step 2: Create Basic about.html (10 mins)

**Create file:** `templates/about.html`

**Students type:**
```html
{% extends 'base.html' %}

{% block title %}About - My Portfolio{% endblock %}

{% block content %}
<section class="py-5">
    <div class="container">
        <h1 class="display-4 mb-4">About Me</h1>
        <p>This is my about page.</p>
    </div>
</section>
{% endblock %}
```

**✅ TEST:** Click "About" - page loads!

---

## ⏱️ PART 2: Build About Content (60 mins)

### Step 3: Add Image & Bio Section (30 mins)

**Edit file:** `templates/about.html`

**Replace everything inside `{% block content %}` with:**
```html
<section class="py-5">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <h1 class="display-4 mb-4">About Me</h1>
                <img src="https://via.placeholder.com/800x400" alt="About" class="img-fluid rounded mb-4">
                
                <p class="lead">I'm a passionate full-stack developer with a love for creating elegant solutions.</p>
                
                <p>Write your first paragraph here. Talk about how you got into programming, what excites you about technology, and what you're currently learning.</p>
                
                <p>Write your second paragraph here. Discuss your goals, what kind of projects you enjoy, and what makes you unique as a developer.</p>
            </div>
        </div>
    </div>
</section>
```

**🔍 Explain:**
- `col-lg-8 mx-auto` - centered column, 8/12 width
- `img-fluid` - responsive image
- `lead` - larger intro text

**✅ TEST:** See about page with placeholder image

---

### Step 4: Students Write Their Bio (15 mins)

**Activity:** Students replace placeholder text:

**Questions to guide them:**
1. How did you start learning to code?
2. What do you enjoy most about programming?
3. What are your career goals?
4. What technologies are you excited about?

**Example:**
```html
<p class="lead">I'm a high school student passionate about web development and solving real-world problems through code.</p>

<p>My journey into programming started two years ago when I built my first HTML website. Since then, I've been hooked! I love how code can transform an idea into something real that people can use.</p>

<p>Currently, I'm learning Python and Flask to build full-stack web applications. My goal is to become a software engineer and create products that make people's lives easier. In my free time, I enjoy contributing to open-source projects and helping other students learn to code.</p>
```

**✅ TEST:** Read your personalized about section

---

### Step 5: Add Skills Section (15 mins)

**Edit file:** `templates/about.html`

**Add AFTER the bio paragraphs (inside the `<div class="col-lg-8 mx-auto">`)**

```html
                <h2 class="mt-5 mb-4">Skills</h2>
                <div class="row g-3">
                    <div class="col-md-6">
                        <div class="skill-item">
                            <h5>Frontend</h5>
                            <p class="text-muted">HTML, CSS, JavaScript, Bootstrap</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="skill-item">
                            <h5>Backend</h5>
                            <p class="text-muted">Python, Flask</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="skill-item">
                            <h5>Database</h5>
                            <p class="text-muted">MySQL, SQLite</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="skill-item">
                            <h5>Tools</h5>
                            <p class="text-muted">Git, VS Code, GitHub</p>
                        </div>
                    </div>
                </div>
```

**🔍 Explain:**
- 2-column grid for skills
- Each skill category in its own card

**✅ TEST:** See skills in a 2x2 grid

---

## ⏱️ PART 3: Add Real Images (30 mins)

### Step 6: Add Skills Section Styling (10 mins)

**Edit file:** `static/css/style.css`

**Add at the end:**
```css
/* Skills Section */
.skill-item {
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
    transition: background 0.3s ease;
}

.skill-item:hover {
    background: #e9ecef;
}

.skill-item h5 {
    color: #0d6efd;
    margin-bottom: 0.5rem;
}
```

**✅ TEST:** Hover over skills - see background change!

---

### Step 7: Add Your About Image (15 mins)

**Activity:** Students add their about image

**Steps:**
1. Find/create an about image (workplace, coding setup, or professional photo)
2. Save it as `static/images/about.jpg`
3. Update the image in `about.html`:

**Change FROM:**
```html
<img src="https://via.placeholder.com/800x400" alt="About">
```

**Change TO:**
```html
<img src="{{ url_for('static', filename='images/about.jpg') }}" alt="About" class="img-fluid rounded mb-4">
```

**✅ TEST:** Refresh - see your real image!

---

### Step 8: Update Skills List (5 mins)

**Activity:** Students customize their skills

**Examples:**
- Add: React, Node.js, MongoDB, etc.
- Remove skills they don't have
- Add new categories (Design, Languages, etc.)

**✅ TEST:** Skills reflect YOUR actual abilities

---

## ⏱️ PART 4: Review & Homework (10 mins)

### What We Built:
✅ About page with Flask route  
✅ Professional bio section  
✅ Skills grid with hover effects  
✅ Custom about image  

### 📝 Homework:
1. Polish your bio - make it compelling!
2. Find a better about image (professional quality)
3. Add one more skill category (e.g., "Soft Skills")
4. BONUS: Add an education or experience section

---
---

# 📋 LESSON 4: Portfolio Page (2 hours)

## 🎯 Learning Objectives
- Pass data from Flask to templates
- Use Jinja2 for loops
- Create project cards with Bootstrap grid

---

## ⏱️ PART 1: Create Portfolio Route with Data (30 mins)

### Step 1: Add Portfolio Route (20 mins)

**Edit file:** `app.py`

**Add this route AFTER the about route:**
```python
@app.route('/portfolio')
def portfolio():
    projects = [
        {
            'id': 'project-one',
            'title': 'My First Website',
            'description': 'A personal portfolio website built with HTML and CSS',
            'image': 'project1.jpg'
        },
        {
            'id': 'project-two',
            'title': 'Calculator App',
            'description': 'A simple calculator built with Python',
            'image': 'project2.jpg'
        }
    ]
    return render_template('portfolio.html', projects=projects)
```

**🔍 Explain:**
- **Python Dictionary** `{}` - stores key-value pairs
- **Python List** `[]` - stores multiple items
- **Passing data** - `projects=projects` sends data to template
- Each project is a dictionary with: id, title, description, image

**Activity:** Draw on board:
```
projects = [
    {dictionary 1},
    {dictionary 2}
]
```

---

### Step 2: Create Basic portfolio.html (10 mins)

**Create file:** `templates/portfolio.html`

**Students type:**
```html
{% extends 'base.html' %}

{% block title %}Portfolio - My Portfolio{% endblock %}

{% block content %}
<section class="py-5">
    <div class="container">
        <h1 class="display-4 text-center mb-5">My Portfolio</h1>
        <p class="text-center text-muted mb-5">Here are some of my recent projects.</p>
    </div>
</section>
{% endblock %}
```

**✅ TEST:** Click "Portfolio" - see heading only

---

## ⏱️ PART 2: Display Projects with Loop (40 mins)

### Step 3: Add Project Cards (30 mins)

**Edit file:** `templates/portfolio.html`

**Add AFTER the paragraph (inside container):**
```html
        <div class="row g-4">
            {% for project in projects %}
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 project-card">
                    <img src="https://via.placeholder.com/400x300" class="card-img-top" alt="{{ project.title }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ project.title }}</h5>
                        <p class="card-text text-muted">{{ project.description }}</p>
                        <a href="#" class="btn btn-primary">View Project</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
```

**🔍 Explain LINE BY LINE:**

**Line 1:** `<div class="row g-4">` - Bootstrap row with gap
**Line 2:** `{% for project in projects %}` - START of loop
**Line 3:** `<div class="col-md-6 col-lg-4">` - Responsive columns:
  - `col-md-6` = 2 cards per row on tablets
  - `col-lg-4` = 3 cards per row on desktop
**Line 4:** `<div class="card h-100 project-card">` - Bootstrap card, full height
**Line 5:** Image placeholder
**Line 7:** `{{ project.title }}` - Gets title from dictionary
**Line 8:** `{{ project.description }}` - Gets description
**Line 11:** `{% endfor %}` - END of loop

**✅ TEST:** See 2 project cards displayed!

---

### Step 4: Understand the Grid (10 mins)

**Activity:** Resize browser window

**Watch what happens:**
- **Desktop (large):** 3 cards per row
- **Tablet (medium):** 2 cards per row  
- **Mobile (small):** 1 card per row

**🔍 Explain Bootstrap Grid:**
```
col-lg-4  →  12 ÷ 4 = 3 cards per row (large screens)
col-md-6  →  12 ÷ 6 = 2 cards per row (medium screens)
(no col-sm) → 1 card per row (small screens)
```

---

## ⏱️ PART 3: Add More Projects (40 mins)

### Step 5: Students Add Their Projects (25 mins)

**Edit file:** `app.py`

**Activity:** Add 2-4 more projects to the list

**Example - Add this project:**
```python
        {
            'id': 'project-three',
            'title': 'Todo List App',
            'description': 'A task management application with Flask',
            'image': 'project3.jpg'
        },
```

**Students add REAL or PLANNED projects:**
- Web applications they built
- Mobile apps they designed
- Games they created
- Future project ideas

**Your projects list should now have 4-6 projects total**

**✅ TEST:** See all projects displayed!

---

### Step 6: Style Project Cards (15 mins)

**Edit file:** `static/css/style.css`

**Add at the end:**
```css
/* Project Cards */
.project-card img {
    height: 250px;
    object-fit: cover;
}

.project-card {
    transition: transform 0.3s ease;
}

.project-card:hover {
    transform: translateY(-10px);
}
```

**🔍 Explain:**
- `height: 250px` - all images same height
- `object-fit: cover` - image fills space nicely
- `transform: translateY(-10px)` - moves card up on hover

**✅ TEST:** Hover over cards - they lift up!

---

## ⏱️ PART 4: Add Project Images (10 mins)

### Step 7: Add Real Project Images

**Activity:** Students prepare project images

**Steps:**
1. Find/create project screenshots or mockups
2. Save as: `project1.jpg`, `project2.jpg`, `project3.jpg`, etc.
3. Put in `static/images/` folder

**For now, keep placeholder images. We'll update in next lesson!**

---

## ⏱️ Review & Homework (10 mins)

### What We Built:
✅ Portfolio page with Flask route  
✅ Dynamic project data in Python  
✅ For loop to display projects  
✅ Responsive grid layout  
✅ Hover effects on cards  

### 📝 Homework:
1. Add 4-6 projects (real or planned)
2. Write compelling project descriptions
3. Create/find project images (screenshots, mockups, or placeholders)
4. Save all images in `static/images/`

**Next Lesson:** We'll link projects to detail pages!

---
---

# 📋 LESSON 5: Project Detail Pages (2 hours)

## 🎯 Learning Objectives
- Work with URL parameters
- Create detailed project dictionary
- Build single project view page
- Link portfolio cards to detail pages

---

## ⏱️ PART 1: Restructure Project Data (35 mins)

### Step 1: Create PROJECTS Dictionary (25 mins)

**Edit file:** `app.py`

**ADD at the top (AFTER imports, BEFORE routes):**

```python
from flask import Flask, render_template, abort

app = Flask(__name__)

# Project Data
PROJECTS = {
    'project-one': {
        'id': 'project-one',
        'title': 'Personal Portfolio Website',
        'short_description': 'A responsive portfolio built with Flask and Bootstrap',
        'image': 'project1.jpg',
        'technologies': ['Flask', 'Bootstrap', 'Python', 'HTML/CSS'],
        'description': 'This project is a personal portfolio website that showcases my skills and projects. I built it using Flask for the backend and Bootstrap for responsive design. The site features a clean, modern interface with smooth animations and is fully responsive across all devices.',
        'features': [
            'Responsive design that works on all devices',
            'Dynamic project display using Flask templates',
            'Contact form for easy communication',
            'Smooth animations and hover effects',
            'SEO-friendly structure'
        ],
        'challenges': 'The main challenge was learning Flask routing and template inheritance. I solved this by reading the documentation carefully and building one page at a time.',
        'github': 'https://github.com/yourusername/portfolio',
        'live_demo': '#'
    },
    'project-two': {
        'id': 'project-two',
        'title': 'Python Calculator',
        'short_description': 'A command-line calculator with advanced functions',
        'image': 'project2.jpg',
        'technologies': ['Python', 'Math Library'],
        'description': 'A feature-rich calculator application built with Python that handles basic arithmetic operations plus scientific functions like trigonometry and logarithms.',
        'features': [
            'Basic arithmetic operations',
            'Scientific functions (sin, cos, tan, log)',
            'Memory storage for calculations',
            'History of previous calculations',
            'Error handling for invalid inputs'
        ],
        'challenges': 'Implementing error handling for division by zero and invalid mathematical operations was tricky. I used try-except blocks to catch errors and provide helpful messages to users.',
        'github': 'https://github.com/yourusername/calculator',
        'live_demo': '#'
    }
}
```

**🔍 Explain:**
- **Outer dictionary** `PROJECTS = {}` contains all projects
- **Key** is the project ID (like 'project-one')
- **Value** is another dictionary with all project details
- We can access like: `PROJECTS['project-one']` or `PROJECTS.get('project-one')`

**Show example on board:**
```
PROJECTS = {
    'project-one': {
        'title': '...',
        'description': '...'
    },
    'project-two': {
        'title': '...',
        'description': '...'
    }
}
```

---

### Step 2: Update Portfolio Route (10 mins)

**Edit file:** `app.py`

**REPLACE the portfolio route with:**
```python
@app.route('/portfolio')
def portfolio():
    # Create simplified list for portfolio page
    projects = [
        {
            'id': project['id'],
            'title': project['title'],
            'description': project['short_description'],
            'image': project['image']
        }
        for project in PROJECTS.values()
    ]
    return render_template('portfolio.html', projects=projects)
```

**🔍 Explain:**
- `PROJECTS.values()` - gets all project dictionaries
- List comprehension creates simplified versions
- Only sends needed data to portfolio page

**✅ TEST:** Portfolio page still works the same!

---

## ⏱️ PART 2: Create Project Detail Route (25 mins)

### Step 3: Add Project Detail Route (15 mins)

**Edit file:** `app.py`

**ADD this route AFTER the portfolio route:**
```python
@app.route('/project/<project_id>')
def project_detail(project_id):
    project = PROJECTS.get(project_id)
    if project is None:
        abort(404)
    return render_template('project_detail.html', project=project)
```

**🔍 Explain:**
- `<project_id>` - URL parameter (dynamic part)
- Example URLs:
  - `/project/project-one`
  - `/project/project-two`
- `PROJECTS.get(project_id)` - finds project by ID
- `abort(404)` - shows "Page Not Found" if project doesn't exist

**Show example:** Visit `http://127.0.0.1:5000/project/project-one`

**Expected:** Error (no template yet)

---

### Step 4: Test URL Parameters (10 mins)

**Activity:** Test different URLs

**Try these in browser:**
1. `http://127.0.0.1:5000/project/project-one` ← Should show error
2. `http://127.0.0.1:5000/project/project-two` ← Should show error
3. `http://127.0.0.1:5000/project/fake-project` ← Should show 404

**🔍 Explain:** URL parameter captures the ID and looks it up

---

## ⏱️ PART 3: Create Project Detail Template (45 mins)

### Step 5: Create project_detail.html (35 mins)

**Create file:** `templates/project_detail.html`

**Students type:**
```html
{% extends 'base.html' %}

{% block title %}{{ project.title }} - My Portfolio{% endblock %}

{% block content %}
<section class="py-5">
    <div class="container">
        <!-- Back Button -->
        <a href="{{ url_for('portfolio') }}" class="btn btn-outline-secondary mb-4">
            ← Back to Portfolio
        </a>
        
        <!-- Project Header -->
        <h1 class="display-4 mb-3">{{ project.title }}</h1>
        <p class="lead text-muted">{{ project.short_description }}</p>
        
        <!-- Technologies -->
        <div class="mb-4">
            <h5 class="mb-3">Technologies Used:</h5>
            <div class="d-flex flex-wrap gap-2">
                {% for tech in project.technologies %}
                <span class="badge bg-primary">{{ tech }}</span>
                {% endfor %}
            </div>
        </div>
        
        <!-- Project Image -->
        <img src="{{ url_for('static', filename='images/' + project.image) }}" 
             alt="{{ project.title }}" 
             class="img-fluid rounded shadow-lg mb-4">
        
        <!-- Project Description -->
        <h2 class="mb-4">Project Overview</h2>
        <p>{{ project.description }}</p>
        
        <!-- Key Features -->
        <h3 class="mb-3">Key Features</h3>
        <ul class="feature-list">
            {% for feature in project.features %}
            <li class="mb-2">{{ feature }}</li>
            {% endfor %}
        </ul>
        
        <!-- Challenges -->
        <h3 class="mb-3">Challenges & Solutions</h3>
        <p>{{ project.challenges }}</p>
        
        <!-- Project Links -->
        <div class="mt-4">
            <a href="{{ project.github }}" class="btn btn-dark" target="_blank">View on GitHub</a>
            <a href="{{ project.live_demo }}" class="btn btn-success" target="_blank">Live Demo</a>
        </div>
    </div>
</section>
{% endblock %}
```

**🔍 Explain important parts:**
- `{{ url_for('portfolio') }}` - generates /portfolio URL
- Loop through technologies to show badges
- Loop through features to show list
- `target="_blank"` - opens links in new tab

**✅ TEST:** Visit `/project/project-one` - see full project page!

---

### Step 6: Style Feature List (10 mins)

**Edit file:** `static/css/style.css`

**Add at the end:**
```css
/* Project Detail Page */
.feature-list {
    list-style: none;
    padding-left: 0;
}

.feature-list li {
    padding-left: 1.5rem;
    position: relative;
}

.feature-list li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #0d6efd;
    font-weight: bold;
}
```

**✅ TEST:** Refresh - see checkmarks before features!

---

## ⏱️ PART 4: Link Cards to Detail Pages (15 mins)

### Step 7: Update Portfolio Cards (10 mins)

**Edit file:** `templates/portfolio.html`

**FIND this line:**
```html
<a href="#" class="btn btn-primary">View Project</a>
```

**REPLACE with:**
```html
<a href="{{ url_for('project_detail', project_id=project.id) }}" class="btn btn-primary">View Project</a>
```

**🔍 Explain:**
- `url_for('project_detail', ...)` - generates project detail URL
- `project_id=project.id` - passes the project ID as parameter
- Result: `/project/project-one`, `/project/project-two`, etc.

**✅ TEST:** 
1. Go to portfolio page
2. Click "View Project" on any card
3. Should go to detailed project page!

---

### Step 8: Test Full Flow (5 mins)

**Activity:** Navigate the site:
1. Home → Portfolio
2. Click a project card
3. See detail page
4. Click "Back to Portfolio"
5. Click another project

**✅ Expected:** Smooth navigation between pages!

---

## ⏱️ Review & Homework (10 mins)

### What We Built:
✅ PROJECTS dictionary with full project data  
✅ URL parameters for dynamic routing  
✅ Project detail page template  
✅ Links from portfolio to detail pages  
✅ Professional project showcase  

### 📝 Homework:
1. Add at least 3 complete projects to PROJECTS dictionary
2. Write detailed descriptions for each project
3. List actual features you implemented
4. Describe real challenges you faced
5. Add your GitHub links (or use '#' for planned projects)
6. Create/find high-quality project images

**Tip:** For planned projects, write what you WILL build and what features it WILL have!

---
---

# 📋 LESSON 6: Contact Page & Deployment (2 hours)

## 🎯 Learning Objectives
- Create contact page with form
- Prepare project for deployment
- Deploy to Render
- Final testing and polish

---

## ⏱️ PART 1: Create Contact Page (30 mins)

### Step 1: Add Contact Route (5 mins)

**Edit file:** `app.py`

**ADD after project_detail route:**
```python
@app.route('/contact')
def contact():
    return render_template('contact.html')
```

**✅ TEST:** Click "Contact" - should show error (no template)

---

### Step 2: Create contact.html (25 mins)

**Create file:** `templates/contact.html`

**Students type:**
```html
{% extends 'base.html' %}

{% block title %}Contact - My Portfolio{% endblock %}

{% block content %}
<section class="py-5">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <h1 class="display-4 text-center mb-4">Get In Touch</h1>
                <p class="text-center text-muted mb-5">Have a question or want to work together?</p>
                
                <!-- Contact Info -->
                <div class="row mb-5">
                    <div class="col-md-4 text-center mb-4">
                        <h5>Email</h5>
                        <p class="text-muted">your.email@example.com</p>
                    </div>
                    <div class="col-md-4 text-center mb-4">
                        <h5>Phone</h5>
                        <p class="text-muted">+123 456 7890</p>
                    </div>
                    <div class="col-md-4 text-center mb-4">
                        <h5>Location</h5>
                        <p class="text-muted">Your City, Country</p>
                    </div>
                </div>
                
                <!-- Contact Form -->
                <div class="card">
                    <div class="card-body p-4">
                        <h3 class="mb-4">Send Me a Message</h3>
                        <form>
                            <div class="mb-3">
                                <label for="name" class="form-label">Name</label>
                                <input type="text" class="form-control" id="name" required>
                            </div>
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" id="email" required>
                            </div>
                            <div class="mb-3">
                                <label for="subject" class="form-label">Subject</label>
                                <input type="text" class="form-control" id="subject" required>
                            </div>
                            <div class="mb-3">
                                <label for="message" class="form-label">Message</label>
                                <textarea class="form-control" id="message" rows="5" required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary btn-lg w-100">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
```

**Students customize:**
- Replace email with their email
- Replace phone with their phone
- Replace location with their city

**✅ TEST:** Contact page displays with form!

---

## ⏱️ PART 2: Update Project Images (20 mins)

### Step 3: Replace Placeholder Images (15 mins)

**Activity:** Students update all images

**Portfolio Images:**
**Edit file:** `templates/portfolio.html`

**FIND:**
```html
<img src="https://via.placeholder.com/400x300" class="card-img-top">
```

**REPLACE with:**
```html
<img src="{{ url_for('static', filename='images/' + project.image) }}" class="card-img-top" alt="{{ project.title }}">
```

**✅ Checklist for students:**
- [ ] All project images saved in `static/images/`
- [ ] Images named: project1.jpg, project2.jpg, etc.
- [ ] About image is `static/images/about.jpg`
- [ ] Profile image is `static/images/profile.jpg`

---

### Step 4: Final Visual Check (5 mins)

**Activity:** Navigate entire site:
- [ ] Home page - profile image loads
- [ ] About page - about image loads
- [ ] Portfolio page - all project cards show images
- [ ] Project detail pages - project images display
- [ ] Contact page - looks good

---

## ⏱️ PART 3: Prepare for Deployment (40 mins)

### Step 5: Create requirements.txt (10 mins)

**Create file:** `requirements.txt` (in project root)

**Students type:**
```
Flask==3.0.0
gunicorn==21.2.0
```

**🔍 Explain:**
- Lists all Python packages needed
- Render uses this to install dependencies
- Version numbers ensure compatibility

---

### Step 6: Create build.sh (10 mins)

**Create file:** `build.sh` (in project root)

**Students type:**
```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
```

**🔍 Explain:**
- Build script for Render
- Installs Python packages
- Runs before app starts

---

### Step 7: Update app.py for Production (10 mins)

**Edit file:** `app.py`

**FIND the bottom:**
```python
if __name__ == '__main__':
    app.run(debug=True)
```

**REPLACE with:**
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**🔍 Explain:**
- `host='0.0.0.0'` - allows external connections
- Required for deployment platforms like Render

**✅ TEST:** Run locally - should still work!

---

### Step 8: Final Project Structure Check (10 mins)

**Your project should look like:**
```
portfolio/
├── app.py
├── requirements.txt
├── build.sh
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── index.html
│   ├── about.html
│   ├── portfolio.html
│   ├── project_detail.html
│   └── contact.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
        ├── profile.jpg
        ├── about.jpg
        ├── project1.jpg
        ├── project2.jpg
        └── project3.jpg
```

**Checklist:**
- [ ] All template files created
- [ ] CSS file present
- [ ] All images in static/images/
- [ ] requirements.txt exists
- [ ] build.sh exists

---

## ⏱️ PART 4: Deploy to Render (30 mins)

### Step 9: Push to GitHub (15 mins)

**Students follow these commands:**

**Initialize Git:**
```bash
git init
git add .
git commit -m "Initial commit - Flask portfolio"
```

**Create GitHub Repository:**
1. Go to github.com
2. Click "New repository"
3. Name it: `flask-portfolio`
4. Don't add README or .gitignore
5. Click "Create repository"

**Push to GitHub:**
```bash
git remote add origin https://github.com/YOUR-USERNAME/flask-portfolio.git
git branch -M main
git push -u origin main
```

**✅ CHECK:** Repository shows all files on GitHub

---

### Step 10: Deploy on Render (15 mins)

**Steps for students:**

1. **Sign up for Render:**
   - Go to render.com
   - Click "Get Started"
   - Sign up with GitHub

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Click "Connect" next to flask-portfolio

3. **Configure Settings:**
   - **Name:** `my-portfolio` (or your choice)
   - **Region:** Choose closest region
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `chmod +x build.sh && ./build.sh`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 3-5 minutes for deployment

**✅ SUCCESS:** Site is live at `https://your-portfolio.onrender.com`

---

## ⏱️ Review & Final Touches (10 mins)

### What We Accomplished:
✅ Built complete Flask portfolio website  
✅ 6 pages: Home, About, Portfolio, Project Details, Contact  
✅ Responsive design with Bootstrap  
✅ Dynamic content with Flask templates  
✅ Deployed live to the internet!  

### 🎉 Congratulations!

**Students now have:**
- A live portfolio website
- Understanding of Flask web development
- Experience with Bootstrap framework
- Git and deployment skills
- Real project for their resume!

### 📝 Post-Class Tasks:
1. Share your live portfolio URL!
2. Add more projects as you build them
3. Keep your portfolio updated
4. Add your portfolio URL to your resume
5. Share on LinkedIn/social media

---

## 🔧 Troubleshooting Guide

### Common Issues & Solutions:

**Issue: "Template not found"**
- Check file is in `templates/` folder
- Check spelling of template name
- Restart Flask server

**Issue: "Static file not loading"**
- Check file is in `static/` folder
- Check `url_for('static', filename='...')` syntax
- Clear browser cache (Ctrl+F5)

**Issue: "Route not working"**
- Check `@app.route()` decorator syntax
- Make sure route function is defined
- Restart Flask server

**Issue: "Render deployment failed"**
- Check `requirements.txt` exists
- Check `build.sh` has correct syntax
- Check GitHub repository has all files
- Look at build logs in Render dashboard

---

## 📚 Additional Resources

**Flask Documentation:**
- https://flask.palletsprojects.com/

**Bootstrap Documentation:**
- https://getbootstrap.com/docs/

**Jinja2 Templates:**
- https://jinja.palletsprojects.com/

**Render Documentation:**
- https://render.com/docs

---

## ✨ Extension Ideas (For Advanced Students)

1. **Add a blog section**
2. **Implement working contact form** (with Flask-Mail)
3. **Add a database** for projects (with Flask-SQLAlchemy)
4. **Create an admin panel** to manage projects
5. **Add animations** with JavaScript
6. **Implement dark mode** toggle
7. **Add authentication** for admin features
8. **Create an API** for your projects data

---

**End of Teaching Plan**

💡 Remember: Learning to code is a journey. Be patient, practice regularly, and don't be afraid to make mistakes. Every error is a learning opportunity!