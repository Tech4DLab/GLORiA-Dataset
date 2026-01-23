from PIL import Image, ImageDraw

# Load the image
image_path = "pez_hd2.JPG"
image = Image.open(image_path)
image = image.convert("RGB")  # Ensure the image is in RGB format

# Create a copy to mark the points
marked_image = image.copy()
draw = ImageDraw.Draw(marked_image)

# Image dimensions
width, height = image.size

# List to store gray-tone points
gray_points = []

# Function to check whether a pixel matches the target gray tone
def is_gray(r, g, b, tolerance=10):
    base_r, base_g, base_b = 20, 20, 10  # Darker gray reference
    return (
        abs(r - base_r) <= tolerance and
        abs(g - base_g) <= tolerance and
        abs(b - base_b) <= tolerance
    )

# Inspect each pixel
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        # Check if the pixel matches the gray tone
        if is_gray(r, g, b):
            gray_points.append((x, y))
            # Mark the pixel in red on the copied image
            draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill="red")

# Determine crop boundaries based on the first and last detected points
if gray_points:
    # First and last points for height (Y-axis)
    first_point_y = gray_points[0]
    last_point_y = gray_points[-1]

    # First and last points for width (X-axis)
    first_point_x = min(gray_points, key=lambda p: p[0])
    last_point_x = max(gray_points, key=lambda p: p[0])

    # Compute center point
    center_x = (first_point_x[0] + last_point_x[0]) // 2
    center_y = (first_point_y[1] + last_point_y[1]) // 2

    # Compute distances
    height_distance = abs(last_point_y[1] - first_point_y[1])
    width_distance = abs(last_point_x[0] - first_point_x[0])

    # Define margins
    margin = 50          # General margin
    bottom_margin = 100  # Extra bottom margin

    # Compute crop boundaries (clipped to image limits)
    min_x = max(center_x - width_distance // 2 - margin, 0)
    max_x = min(center_x + width_distance // 2 + margin, width)
    min_y = max(center_y - height_distance // 2 - margin, 0)
    max_y = min(center_y + height_distance // 2 + bottom_margin, height)

    # Crop the image
    cropped_image = image.crop((min_x, min_y, max_x, max_y))

    # Save outputs
    cropped_image.save("cropped_image_with_margin.jpg")
    cropped_image.show()

    marked_image.save("gray_marked_image.jpg")
    marked_image.show()

    print("Cropped image saved as 'cropped_image_with_margin.jpg'")
else:
    print("No pixels matching the specified gray tones were found.")

