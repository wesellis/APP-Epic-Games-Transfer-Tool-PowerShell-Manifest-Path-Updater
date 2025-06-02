"""
Create a simple icon for the Epic Games Manifest Updater
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create a simple icon for the application"""
    # Create a 256x256 image with Epic Games-like colors
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle with Epic Games-like gradient colors
    padding = 20
    circle_bbox = [padding, padding, size - padding, size - padding]
    
    # Draw multiple circles for gradient effect
    for i in range(20):
        offset = i * 2
        color_intensity = 255 - (i * 8)
        color = (color_intensity, color_intensity // 2, color_intensity // 4, 255)
        draw.ellipse([
            circle_bbox[0] + offset,
            circle_bbox[1] + offset,
            circle_bbox[2] - offset,
            circle_bbox[3] - offset
        ], fill=color)
    
    # Draw "E" for Epic
    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    # Get text size and center it
    text = "E"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - 10
    
    # Draw text with shadow
    draw.text((text_x + 3, text_y + 3), text, fill=(0, 0, 0, 128), font=font)
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    # Save as ICO
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    icons = []
    
    for size_tuple in sizes:
        icon = img.resize(size_tuple, Image.Resampling.LANCZOS)
        icons.append(icon)
    
    icons[0].save('icon.ico', format='ICO', sizes=[icon.size for icon in icons])
    print("✓ Created icon.ico")

if __name__ == "__main__":
    try:
        create_icon()
    except ImportError:
        print("PIL/Pillow not available - creating simple text icon")
        # Create a simple text file that PyInstaller can use
        with open('icon.ico', 'wb') as f:
            f.write(b'')  # Empty file, PyInstaller will handle gracefully
