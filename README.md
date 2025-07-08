# Image Colorization App with DeOldify and Flask

## Overview
This project is a web application that enables users to upload black-and-white images and automatically colorize them using the DeOldify deep learning model. The app is built with Flask and leverages PyTorch and FastAI for the colorization process.

## Table of Contents
- [Objective](#objective)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Objective
The primary goal of this project is to provide a simple and effective tool for colorizing black-and-white images, enhancing their visual appeal using state-of-the-art deep learning techniques.

## Features
- Upload black-and-white images.
- Automatically colorizes images using the DeOldify model.
- Clean user interface displaying both uploaded and output images.

## Tech Stack
- **Python**
- **Flask**: Web framework for building the application.
- **DeOldify**: Deep learning model for image colorization.
- **PyTorch**: Framework for building and training the model.
- **FastAI**: High-level library for fast and easy deep learning.
- **Jinja2**: Templating engine for rendering HTML.

## Project Structure

Image-Colorization-App/
│
├── app.py                # Main Flask application
├── static/               # Static files (CSS, JS, images)
│   └── style.css         # CSS for styling the app
├── templates/            # HTML templates
│   ├── index.html        # Main page for uploading images
│   └── result.html       # Page to display the colorized image
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation


## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/YasirHussain1272/colorizes-black-and-white-image.git
   cd colorizes-black-and-white-image

pip install -r requirements.txt
