import cv2
import numpy as np
import mediapipe as mp
import os

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.components import containers

# Definitions
RegionOfInterest = vision.InteractiveSegmenterRegionOfInterest
NormalizedKeypoint = containers.keypoint.NormalizedKeypoint

# Model configuration
base_options = python.BaseOptions(model_asset_path='model.tflite')
options = vision.ImageSegmenterOptions(
    base_options=base_options,
    output_category_mask=True
)

# Keypoint coordinates in the image (0–1)
x = 0.5
y = 0.5

input_folder = "./Copia_224/"
output_folder = os.path.join(input_folder, "segmented")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all .jpg files in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):
        input_image_path = os.path.join(input_folder, filename)

        with vision.InteractiveSegmenter.create_from_options(options) as segmenter:
            image = mp.Image.create_from_file(input_image_path)
            roi = RegionOfInterest(
                format=RegionOfInterest.Format.KEYPOINT,
                keypoint=NormalizedKeypoint(x=x, y=y)
            )
            segmentation_result = segmenter.segment(image, roi)
            category_mask = segmentation_result.category_mask

        # Convert the original image to numpy format
        image_data = image.numpy_view()

        # Create a new output image with an additional alpha channel
        output_image = np.zeros(
            (image_data.shape[0], image_data.shape[1], 4),
            dtype=np.uint8
        )

        # Convert the category mask to numpy format
        category_mask_np = category_mask.numpy_view()

        # Apply segmentation condition: keep original colors and modify transparency
        condition = category_mask_np > 0.2

        # Copy original colors (RGB)
        output_image[..., :3] = image_data

        # Adjust transparency
        output_image[..., 3] = np.where(condition, 0, 255)

        output_image = cv2.cvtColor(output_image, cv2.COLOR_BGRA2RGBA)

        # Save the resulting image
        output_image_path = os.path.join(
            output_folder,
            filename.replace(".jpg", ".png").replace(".JPG", ".png")
        )

        # Ensure the alpha channel is saved correctly using PNG format
        cv2.imwrite(output_image_path, output_image)

        print(f"Processed: {filename} -> Saved at: {output_image_path}")

print("Processing completed for all images.")

