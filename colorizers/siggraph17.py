from flask import Flask, render_template, request
import os
import uuid
import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms
from colorizers.siggraph17 import Siggraph17

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = Siggraph17(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Convert to grayscale
    gray_img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    color_input = transform(Image.fromarray(gray_img)).unsqueeze(0)

    with torch.no_grad():
        output_ab = model(color_input)

    # Convert back to image
    output_ab = output_ab.squeeze(0).permute(1, 2, 0).numpy()
    output_ab = cv2.resize(output_ab, (gray_img.shape[1], gray_img.shape[0]))
    output_ab = (output_ab * 128).astype(np.uint8)

    # Convert to Lab and then to BGR
    lab = np.zeros((gray_img.shape[0], gray_img.shape[1], 3), dtype=np.uint8)
    lab[:, :, 0] = gray_img
    lab[:, :, 1:] = output_ab
    bgr_result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    colorized_name = f"colorized_{filename}"
    colorized_path = os.path.join(UPLOAD_FOLDER, colorized_name)
    cv2.imwrite(colorized_path, bgr_result)

    return render_template('result.html', original=filename, colorized=colorized_name)

if __name__ == '__main__':
    app.run(debug=True)
