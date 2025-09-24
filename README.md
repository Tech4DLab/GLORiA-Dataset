# 🐟 GLORiA Dataset – Fish and Their Origins 

## 👀 Overview

The **GLORiA Dataset** is an image collection designed for the study and classification of fish according to their **origin**. It includes images of three highly relevant species in aquaculture and fisheries:  

- **Argyrosomus regius** (*meagre*)  
- **Dicentrarchus labrax** (*European seabass*)  
- **Sparus aurata** (*gilthead seabream*)  

Each specimen is categorized into three groups based on its provenance:  

- **C** → Captive (aquaculture)  
- **E** → Escaped (individuals that escaped from farms into the wild)  
- **W** → Wild  

The dataset is organized into species and class specific folders, with an additional test set containing images from fish markets and also includes processed and augmented versions. It can be used in computer vision tasks such as automatic classification, deep learning experiments and comparative studies between wild and farmed fish.  
 
## 🎯 Key Features
- Provide an open resource for research on fish origin classification.  
- Enable the study of morphological differences between wild, farmed and escaped fish.  
- Contribute to projects on AI for aquaculture and sustainability.  

## 🗂️ Repository Structure
```
.
├── README.md            # This file
├── LICENSE              # MIT License (or project-specific)
├── data/                # Folder that contains all the images included in the GLORiA Dataset
     ├── A_regius/
     │   ├── C/   # Captive
     │   ├── E/   # Escaped
     │   └── W/   # Wild
     ├── D_labrax/
     │   ├── C/   # Captive
     │   ├── E/   # Escaped
     │   └── W/   # Wild
     ├── S_aurata/
     │   ├── C/   # Captive
     │   ├── E/   # Escaped
     │   └── W/   # Wild
     └── test/              # Images from fish markets and fishmongers
```
