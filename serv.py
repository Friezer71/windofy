import os
import subprocess

# Create directories
os.makedirs('static', exist_ok=True)
os.makedirs('templates', exist_ok=True)

# Create index.html in the templates directory
with open('templates/index.html', 'w') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Windofy</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1 id="title">Windofy</h1>
        <p id="description">Bienvenue sur le site de Windofy. Découvrez nos fonctionnalités incroyables.</p>
    </div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
''')

# Create style.css in the static directory
with open('static/style.css', 'w') as f:
    f.write('''body {
    background-color: #262626;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

h1 {
    font-size: 3em;
    opacity: 0;
    animation: fadeIn 2s forwards, moveUp 2s 2s forwards, borderAnimation 2s 4s forwards;
}

p {
    font-size: 1.5em;
    opacity: 0;
    animation: fadeIn 2s 6s forwards;
}

@keyframes fadeIn {
    to {
        opacity: 1;
    }
}

@keyframes moveUp {
    to {
        transform: translate(-50%, -100%);
    }
}

@keyframes borderAnimation {
    from {
        border: none;
    }
    to {
        border: 2px solid;
        border-image: linear-gradient(45deg, red, yellow, green, cyan, blue, magenta, red) 1;
    }
}
''')

# Create script.js in the static directory
with open('static/script.js', 'w') as f:
    f.write('''document.addEventListener("DOMContentLoaded", function() {
    const title = document.getElementById("title");
    const description = document.getElementById("description");

    // Trigger the animations
    title.style.animationPlayState = 'running';
    description.style.animationPlayState = 'running';
});
''')

# Create app.py
with open('app.py', 'w') as f:
    f.write('''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25646)
''')

# Create requirements.txt
with open('requirements.txt', 'w') as f:
    f.write('''Flask==2.0.1
Werkzeug==2.0.1
''')

# Install the required packages
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Launch the Flask server
subprocess.run(['python', 'app.py'])
