import os
# import sys
# import shutil
from PIL import Image, ImageDraw
import cv2

margin = 100
bottom_margin = 100  # (currently unused in this version)

# Values used to build file/folder names
folder_prefix = "SA "
folder_suffix = " S 230724"
image_prefix = "SA"
image_suffix = ")_S.JPG"

# Numeric ranges for folders/files
start_folder = 285
end_folder = 315
start_photo = 153
end_photo = 183
photo_variant_start = 1
photo_variant_end = 10

def is_gray(r, g, b, tolerance=10):
    base_r, base_g, base_b = 20, 20, 10  # Dark gray reference
    return (
        abs(r - base_r) <= tolerance and
        abs(g - base_g) <= tolerance and
        abs(b - base_b) <= tolerance
    )

def center_crop(img, dim):
    """Crop the image from the center with the specified dimensions."""
    width, height = img.shape[1], img.shape[0]
    crop_width = dim[0] if dim[0] < img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1] < img.shape[0] else img.shape[0]
    mid_x, mid_y = int(width / 2), int(height / 2)
    cw2, ch2 = int(crop_width / 2), int(crop_height / 2)
    crop_img = img[mid_y - ch2:mid_y + ch2, mid_x - cw2:mid_x + cw2]
    return crop_img

def process_images(image_path, copy_hd_dir, copy_224_dir):
    # Create output directories if they do not exist
    if not os.path.exists(copy_hd_dir):
        os.mkdir(copy_hd_dir)
    if not os.path.exists(copy_224_dir):
        os.mkdir(copy_224_dir)

    # Read the image with OpenCV for center cropping
    if os.path.exists(image_path):
        image_cv = cv2.imread(image_path)
        if image_cv is not None:
            image_cv_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

            # Center crop
            ccrop_img = center_crop(image_cv_rgb, (2500, 2500))

            # Convert cropped image from OpenCV (numpy) to PIL for gray-pixel analysis
            pil_image = Image.fromarray(ccrop_img)
            pil_image = pil_image.convert("RGB")

            marked_image = pil_image.copy()
            draw = ImageDraw.Draw(marked_image)

            # Dimensions of the cropped image
            width, height = pil_image.size
            gray_points = []

            # Inspect each pixel and mark gray tones
            for y in range(height):
                for x in range(width):
                    r, g, b = pil_image.getpixel((x, y))
                    if is_gray(r, g, b):
                        gray_points.append((x, y))
                        draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill="red")

            # Compute crop bounds based on first/last gray points (X-axis)
            if gray_points:
                first_point_x = min(gray_points, key=lambda p: p[0])
                last_point_x = max(gray_points, key=lambda p: p[0])

                center_x = (first_point_x[0] + last_point_x[0]) // 2
                width_distance = abs(last_point_x[0] - first_point_x[0])

                min_x = max(center_x - width_distance // 2 - margin, 0)
                max_x = min(center_x + width_distance // 2 + margin, width)

                # Crop using the computed bounds
                # NOTE: This uses (min_x, min_x, max_x, max_x) intentionally, as in your original code
                cropped_image = pil_image.crop((min_x, min_x, max_x, max_x))

                # Save cropped image into Copy_HD with original name + ".jpg"
                basename = os.path.basename(image_path)
                cropped_image.save(f"{copy_hd_dir}/{basename}.jpg")

                # Resize cropped image to 224x224 and save into Copy_224
                resized = cropped_image.resize((224, 224))
                resized.save(f"{copy_224_dir}/{basename}.jpg")

                print(f"Image processed and saved into Copy_HD and Copy_224: {basename}")

if __name__ == "__main__":
    j = start_photo
    # while loop over photo indices
    while j < end_photo:
        for i in range(start_folder, end_folder):
            for k in range(photo_variant_start, photo_variant_end):
                path = (
                    "./" + folder_prefix + str(i) + folder_suffix + "/"
                    + image_prefix + str(j) + " (" + str(k) + image_suffix
                )
                copy_hd = "./" + folder_prefix + str(i) + folder_suffix + "/" + "Copia_HD"
                copy_224 = "./" + folder_prefix + str(i) + folder_suffix + "/" + "Copia_224"

                print(path)
                process_images(path, copy_hd, copy_224)

            j = j + 1

            