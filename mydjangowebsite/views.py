from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

# Portfolio page view
def portfolio_view(request):
    print("Portfolio function is called from view")
    
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Engr. Muhammad Abul Hassan</title>
    <!-- Include CSS and Google Fonts -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="container">
            <a href="#" class="navbar-brand">Engr. Abul Hassan</a>
            <ul class="nav-links">
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero-section">
        <div class="container">
            <h1>Hi, I'm Muhammad Abul Hassan</h1>
            <p>A Computer Engineer specializing in AI, Machine Learning, and Web Development.</p>
            <a href="https://github.com/M-Abul-Hassan" class="btn btn-primary">View My Work</a>
            <a href="Muhammad_Abul_Hassan_CV.pdf" class="btn btn-light" download>Download CV</a>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="about-section">
        <div class="container">
            <h2>About Me</h2>
            <p>I'm a passionate computer engineer with experience in AI, ML, and web development. I aim to solve real-world problems using cutting-edge technology.</p>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills-section">
        <div class="container">
            <h2>My Skills</h2>
            <div class="skills-list">
                <div class="skill">
                    <i class="fas fa-laptop-code"></i>
                    <h4>Web Development</h4>
                </div>
                <div class="skill">
                    <i class="fas fa-robot"></i>
                    <h4>Artificial Intelligence</h4>
                </div>
                <div class="skill">
                    <i class="fas fa-brain"></i>
                    <h4>Machine Learning</h4>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects-section">
        <div class="container">
            <h2>My Projects</h2>
            <div class="project-grid">
                <div class="project-card">
                    <h3>AI-Based Fire Detection System</h3>
                    <p>This project monitors CCTV cameras to detect fire incidents in real time.</p>
                </div>
                <div class="project-card">
                    <h3>E-Commerce Website</h3>
                    <p>An e-commerce platform for selling AI-based products and services.</p>
                </div>
                <div class="project-card">
                    <h3>Portfolio Website</h3>
                    <p>A responsive and visually appealing website to showcase my skills and projects.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="container">
            <h2>Contact Me</h2>
            <p>Email: muhammadabulhassan70@gmail.com</p>
            <form class="contact-form">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <textarea placeholder="Your Message" required></textarea>
                <button type="submit" class="btn btn-primary">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Engr. Muhammad Abul Hassan | All Rights Reserved</p>
        </div>
    </footer>

    <!-- Link to external JS file -->
    <script src="script.js"></script>
</body>
</html>

    """
    
    return HttpResponse(html_content)

def home(request):
    print("Portfolio function is called from view")
    #return HttpResponse("My name is Muhammad Abul Hassan")
    return render(request,"profile.html",{})

def name(request):
    print("Portfolio function is called from view")
    return HttpResponse("My name is Muhammad Abul Hassan")

def project(request):
    print("Portfolio function is called from view")
    return HttpResponse("Ai Based fire detection system")

# URL patterns
urlpatterns = [
    path('', portfolio_view, name='portfolio'),
]
