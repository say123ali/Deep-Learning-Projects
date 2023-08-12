# Deep-Learning-Projects
### 1. Case Study: Helmet Detection
#### Detecting Motorcylist with or without Helmet. Multiple Object Detection in one Image
### 2. Clothing Apparel Detection
### 3. Agricultural Plant Disease Classification
# Plant Disease Classification

## Description

In agriculture, leaf diseases cause a major decrease in both quality and quantity of yields. Automating plant disease detection using Computer Vision could play a role in early detection and prevention of diseases.


## Architecture


## Data

We will use dataset gathered by the awesome folks at PlantVillage(https://plantvillage.psu.edu/).

Dataset Link:- 
https://www.dropbox.com/s/hgt9uystjlinzlp/plantVillage.zip

## Data Description

Dataset Size :-
*     Number of train images: 44014
*     Number of validation images: 11004
*     Number of classes: 39
Dataset Download

`wget https://www.dropbox.com/s/hgt9uystjlinzlp/plantVillage.zip`

`unzip plantVillage.zip`

##### Import Monk library
##### Place monk inside your project folder
    `import os`
    `import sys`
    `sys.path.append("./monk/")`
    `import psutil`
    `from pytorch_prototype import prototype`
    
## Data Augmentation

We will be implementing data augmentation by using the Augmentor Library(https://github.com/mdbloice/Augmentor)
## Training

## Train test validation
## Performance tuning
## Possible tuning analytic
## Comparison with benchmarks
## Deployment

## Conclusion
### 4. Lung Cancer Detection on Histopathological image dataset
C25000 LUNG AND COLON HISTOPATHOLOGICAL IMAGE DATASET

The dataset contains color 25,000 images with 5 classes of 5,000 images each. All images are 768 x 768 pixels in size and are in jpeg file format. Our dataset can be downloaded as a 1.85 GB zip file LC25000.zip. After unzipping, the main folder lung_colon_image_set contains two subfolders: colon_image_sets and lung_image_sets.

The subfolder colon_image_sets contains two secondary subfolders: colon_aca subfolder with 5000 images of colon adenocarcinomas and colon_n subfolder with 5000 images of benign colonic tissues.

The subfolder lung_image_sets contains three secondary subfolders: lung_aca subfolder with 5000 images of lung adenocarcinomas, lung_scc subfolder with 5000 images of lung squamous cell carcinomas, and lung_n subfolder with 5000 images of benign lung tissues.

This dataset can be downloaded from the link below:

https://academictorrents.com/details/7a638ed187a6180fd6e464b3666a6ea0499af4af
