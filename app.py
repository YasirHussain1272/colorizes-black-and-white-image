"""
from flask import Flask, render_template, request
from deoldify.visualize import get_image_colorizer
from fastai.vision import *
import os
from PIL import Image
from pathlib import Path

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load DeOldify Colorizer
colorizer = get_image_colorizer(artistic=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colorize', methods=['POST'])
def colorize():
    file = request.files['image']
    if not file:
        return 'No file uploaded', 400

    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    file.save(input_path)

    # Colorize image
    

    colorizer.plot_transformed_image(
        path=Path(input_path),
        results_dir=Path(app.config['UPLOAD_FOLDER']),
        render_factor=35,
        display_render_factor=False,
        figsize=(20, 20)
    )



    return render_template('result.html', output_image='output.png', input_image='input.png')

if __name__ == '__main__':
    app.run(debug=True)
"""

from pathlib import Path
from deoldify.visualize import get_image_colorizer
from deoldify.device_id import DeviceId
from deoldify import device
import fastai
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

# Set device
#device.set(DeviceId.GPU)  # or DeviceId.CPU
device.set(DeviceId.CPU)

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = Path('static/results')  # ✅ convert to Path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load DeOldify model
colorizer = get_image_colorizer(artistic=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Colorize image
        result_path = colorizer.plot_transformed_image(
            path=image_path,
            results_dir=RESULT_FOLDER,
            render_factor=35,
            display_render_factor=True,
            compare=False
        )

        result_filename = result_path.name
        return render_template(
    'result.html',
    input_image=os.path.join('static/uploads', filename).replace("\\", "/"),
    output_image=os.path.join('static/results', result_filename).replace("\\", "/")
)


if __name__ == '__main__':
    app.run(debug=True)
