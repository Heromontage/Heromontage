import sys
from PIL import Image

def image_to_ascii(image_path, width=100):
    img = Image.open(image_path)
    # Convert to grayscale
    gray = img.convert('L')
    # Aspect ratio correction: terminal chars are taller than wide
    # Assume char height ~2 * width
    aspect = 0.5
    height = int(width * gray.size[1] / gray.size[0] * aspect)
    resized = gray.resize((width, height))
    # ASCII characters from dark to light
    ascii_chars = '@%#*+=-:. '
    # Map pixel values (0-255) to ascii_chars indices
    def pixel_to_ascii(val):
        return ascii_chars[val * (len(ascii_chars)-1) // 255]
    lines = []
    for y in range(resized.height):
        line = ''.join(pixel_to_ascii(resized.getpixel((x, y))) for x in range(resized.width))
        lines.append(line)
    return lines

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python ascii_gen.py <image_path> [width]')
        sys.exit(1)
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    lines = image_to_ascii(sys.argv[1], width)
    for line in lines:
        print(line)