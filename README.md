# 🐟 GLORiA Dataset – Fish && Origins 

[![Dataset](https://img.shields.io/badge/Dataset-Zenodo-blue)](https://doi.org/10.5281/zenodo.20540572)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)](https://www.python.org/)

## 👀 Overview

The **GLORiA Dataset** is an image collection designed for the study and classification of fish according to their origin. It includes images of three highly relevant species in aquaculture and fisheries:  

- **Argyrosomus regius** (*Meagre*)  
- **Dicentrarchus labrax** (*European seabass*)  
- **Sparus aurata** (*Gilthead seabream*)  

Each specimen is categorized into three groups based on its provenance:  

- **C** → Captive (aquaculture)  
- **E** → Escaped (individuals that escaped from farms)  
- **W** → Wild  

The dataset is organized into species and class specific folders, with an additional test set containing images from fish markets and also includes processed and augmented versions. It can be used in computer vision tasks such as automatic classification, deep learning experiments and comparative studies between wild and farmed fish.  

The complete dataset is available on Zenodo:

> **GLORiA Dataset:** https://doi.org/10.5281/zenodo.20540572

This GitHub repository provides the code used to preprocess, crop, resize, segment, and organize the images included in the dataset.
 
## 🎯 Key Features
- Provide an open resource for research on fish origin classification.  
- Enable the study of morphological differences between wild, farmed and escaped fish.  
- Contribute to projects on AI for aquaculture and sustainability.  

## 🗂️ Repository Structure
```
.
├── README.md            # Project documentation
├── LICENSE              # MIT License
├── Images               # Sample images and visual references
├── Segmentation
│   ├── model.tflite     # MediaPipe segmentation model
│   ├── auto_seg.py      # Automatic image segmentation script
│   └── seg_fold.py      # Batch segmentation over folder structure
└── Crop
    ├── color.py         # Gray-based color detection and cropping
    ├── color2.py        # Alternative color-based cropping strategy
    ├── resize.py        # Image resizing utilities (e.g., 224×224)
    └── crop.py          # Automated cropping based on detected regions


    
```
## 📊 Dataset Summary

The main laboratory subset contains **9,511 images** from three fish species.

| Origin Category | *A. regius* | *D. labrax* | *S. aurata* | Total |
|---|---:|---:|---:|---:|
| Wild / `S` | 0 | 988 | 2,627 | 3,615 |
| Escaped / `E` | 620 | 866 | 355 | 1,841 |
| Captive / `C` | 767 | 1,432 | 1,856 | 4,055 |
| **Total** | **1,387** | **3,286** | **4,838** | **9,511** |

<details>
<summary><strong>📸 View image samples</strong></summary>

<p align="center">
  <img src="Images/AR087 (2)_E.JPG" width="400">
  <img src="Images/DL13_S.jpeg" width="305">
</p>
<p align="center">
  <img src="Images/DL209 (16)_E.jpg" width="300">
  <img src="Images/SA209 (6)_E.JPG" width="300">
</p>
<p align="center">
  <img src="Images/SA210_C.jpeg" width="320">
  <img src="Images/SA216 (12)_E.jpg" width="305">
</p>

</details>

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Tech4DLab/GLORiA-Dataset.git
cd GLORiA-Dataset
```

Create a Python environment:

```bash
python -m venv gloria_env
```

Activate it:

```bash
# Linux / macOS
source gloria_env/bin/activate

# Windows
gloria_env\Scripts\activate
```

Install the basic dependencies:

```bash
pip install opencv-python pillow numpy mediapipe
```

Depending on the segmentation workflow used, additional dependencies may be required.

---

## 🚀 Usage

### 1. Resize images to 224 × 224

The script `Crop/resize.py` resizes images to 224 × 224 pixels and stores them in an output folder.

By default, the script processes images from the current folder and saves the resized images in:

```text
./copia_224/
```

Example:

```bash
cd Crop
python resize.py
```

Recommended workflow:

```text
input_images/
├── image_1.jpg
├── image_2.jpg
└── image_3.jpg
```

Expected output:

```text
input_images/
└── copia_224/
    ├── image_1.jpg
    ├── image_2.jpg
    └── image_3.jpg
```

---

### 2. Center crop and resize images

The script `Crop/crop.py` performs a center crop and creates two output folders:

```text
Copia_HD/
Copia_224/
```

Example:

```bash
python Crop/crop.py image_1.jpg image_2.jpg image_3.jpg
```

Expected outputs:

```text
Copia_HD/    # Cropped high-resolution copies
Copia_224/   # Cropped and resized 224 × 224 copies
```

> **Important:** Some preprocessing scripts may overwrite or modify input images during execution. We strongly recommend working on a copy of the original dataset.

---

### 3. Automatic segmentation

The `Segmentation/` folder contains scripts for applying automatic segmentation to fish images.

General workflow:

```bash
cd Segmentation
python auto_seg.py
```

The segmentation process uses the available model files and produces masks or processed images depending on the script configuration.

Before running the segmentation scripts, check that:

- the input images are in the expected folder,
- `model.tflite` is available,
- the required dependencies are installed,
- the output folder has write permissions.

---

### 4. Batch processing over folders

For large datasets organized by species and origin category, use the folder-based scripts to apply preprocessing over multiple subfolders.

Recommended input structure:

```text
Dataset/
├── A. regius/
│   ├── C/
│   └── E/
├── D. labrax/
│   ├── C/
│   ├── E/
│   └── S/
└── S. aurata/
    ├── C/
    ├── E/
    └── S/
```

## 🔗 Citation

If you use this dataset in your research, please cite:

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## 🤝 Acknowledgments

The study was funded by the project “GLObal change Resilience in Aquaculture-TOOls for Long-term Sustainability (GLORiA-TOOLS),” supported by the Biodiversity Foundation of the Spanish Ministry for the Ecological Transition and Demographic Challenge through the Pleamar Program and co-financed by the European Maritime, Fisheries and Aquaculture Fund (EMFAF).

Project context: [GLORiA](https://github.com/Tech4DLab/GLORIA).

## 📬 Contact

| Name | Role | GitHub | Contact | Deparment | 
|------|------|--------|---------|---------|
| [Mario Jerez Tallón](https://github.com/Mariojt72) | Author | @Mariojt72 | mario.jerez@ua.es | Computer Technology
| [Ismael Beviá Ballesteros](https://github.com/ibevias) | Co-authors | @ibevias | ismael.bevias@ua.es | Computer Technology
| Dr. Kilian Toledo-Guedes | PI | – | ktoledo@ua.es | Marine Sciences
| Jaime Fernandez del Campo | Data curation | – | jaime.fdezdelcampo@ua.es | Marine Sciences
| David Pitarch Font | Data curation | – | david.pitarch@ua.es | Marine Sciences
| [Dr. Nahuel Emiliano Garcia d'Urso](https://github.com/nawue) | Co-authors | @nawue | nahuel.garcia@ua.es | Computer Technology
| Dr. Andrés Fuster Guilló | PI | – | fuster@ua.es | Computer Technology
| Dr. Jorge Azorín López | PI | – | jazorin@ua.es | Computer Technology
