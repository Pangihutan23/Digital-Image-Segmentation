import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, "Citra")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_image(Citra):
    img = Image.open(Citra)
    return np.array(img)

def save_image(image, output):
    Image.fromarray(image).save(output)

def normalize(image):
    image = np.clip(image, 0, 255)
    return image.astype(np.uint8)

def convolve(img, kernel):
    h, w = img.shape
    kh, kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2

    padded = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='reflect')
    out = np.zeros_like(img, dtype=float)

    for y in range(h):
        for x in range(w):
            region = padded[y:y+kh, x:x+kw]
            out[y, x] = np.sum(region * kernel)

    return out


def edge_roberts(img):
    kx = np.array([[1, 0], [0, -1]])
    ky = np.array([[0, 1], [-1, 0]])
    gx = convolve(img, kx)
    gy = convolve(img, ky)
    return np.sqrt(gx**2 + gy**2)

def edge_prewitt(img):
    kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    gx = convolve(img, kx)
    gy = convolve(img, ky)
    return np.sqrt(gx**2 + gy**2)

def edge_sobel(img):
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    gx = convolve(img, kx)
    gy = convolve(img, ky)
    return np.sqrt(gx**2 + gy**2)

def edge_frei_chen(img):
    sqrt2 = np.sqrt(2)
    kx = np.array([[-1, 0, 1], [-sqrt2, 0, sqrt2], [-1, 0, 1]])
    ky = np.array([[-1, -sqrt2, -1], [0, 0, 0], [1, sqrt2, 1]])
    gx = convolve(img, kx)
    gy = convolve(img, ky)
    return np.sqrt(gx**2 + gy**2)


def process_and_display_all():
    image_files = ['portrait.jpg', 'landscape.jpg', 'salt and pepper.jpg', 'gaussian.jpg']

    operators = [
        ('Roberts', edge_roberts),
        ('Prewitt', edge_prewitt),
        ('Sobel', edge_sobel),
        ('Frei-Chen', edge_frei_chen)
    ]

    for image_file in image_files:
        full_path = os.path.join(IMAGE_FOLDER, image_file)

        try:
            original = load_image(full_path)
            clean_name = image_file.split('.')[0]

            fig, axes = plt.subplots(2, 2, figsize=(10, 8))
            axes = axes.ravel()
            fig.suptitle(f'Edge Detection - {clean_name.title()}', fontsize=14, fontweight='bold')

            for i, (op_name, op_func) in enumerate(operators):
                result = normalize(op_func(original))
                axes[i].imshow(result, cmap='gray')
                axes[i].set_title(op_name)
                axes[i].axis('off')

                output_path = os.path.join(OUTPUT_FOLDER, f"{clean_name}_{op_name.lower()}.png")
                save_image(result, output_path)

            plt.tight_layout()
            comparison_path = os.path.join(OUTPUT_FOLDER, f"{clean_name}_comparison.png")
            plt.savefig(comparison_path, dpi=150, bbox_inches='tight')
            plt.show()

            print(f"✓ {clean_name} selesai -> {comparison_path}")

        except Exception as e:
            print(f"✗ Error {image_file}: {e}")


if __name__ == "__main__":
    process_and_display_all()
    print("\nSemua gambar telah diproses dan ditampilkan!")
