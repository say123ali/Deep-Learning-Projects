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


Name of different classes: -



| id |	labels                                |
|------------------------------------------|
| 0	 |Strawberry___healthy                   |
| 1	 |background                             |
| 2	 |Grape___Black_rot                      |
| 3	 |Potato___Early_blight                  |
| 4	 |Blueberry___healthy                    |
| 5	 |Corn_(maize)___healthy                 |
| 6	 |Tomato___Target_Spot                   |
| 7	 |Peach___healthy                        |
| 8	 |Potato___Late_blight                   |
| 9	 |Tomato___Late_blight                   |
| 10 |Tomato___Tomato_mosaic_virus          |
| 11	|Pepper	_bell___healthy                |
| 12	|Orange___Haunglongbing_(Citrus_greening) |
| 13	|Tomato___Leaf_Mold                    |
| 14	|Grape___Leaf_blight_(Isariopsis_Leaf_Spot) |
| 15	|Cherry_(including_sour)___Powdery_mildew |
| 16	|Apple___Cedar_apple_rust              |
| 17	|Tomato___Bacterial_spot               |
| 18	|Grape___healthy                       |
| 19	|Tomato___Early_blight                 |
| 20	|Corn_(maize)___Common_rust_           |
| 21	|Grape___Esca_(Black_Measles)          |
| 22	|Raspberry___healthy                   |
| 23	|Tomato___healthy                      |
| 24	|Cherry_(including_sour)___healthy     |
| 25	|Tomato___Tomato_Yellow_Leaf_Curl_Virus |
| 26	|Apple___Apple_scab                    |
| 27	|Corn_(maize)___Northern_Leaf_Blight   |
| 28	|Tomato___Spider_mites Two-spotted_spider_mite |
| 29	|Peach___Bacterial_spot                |
| 30	|Pepper	_bell___Bacterial_spot         |
| 31	|Tomato___Septoria_leaf_spot           |
| 32	|Squash___Powdery_mildew               |
| 33	|Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot |
| 34	|Apple___Black_rot                     |
| 35	|Apple___healthy                       |
| 36	|Strawberry___Leaf_scorch              |
| 37	|Potato___healthy                      |
| 38	|Soybean___healthy                     |


	

## Possible use cases in different domain


## Installation and Setup

Installation
01. Clone library from github

    `git clone https://github.com/Tessellate-Imaging/monk_v1`
 
2. Setup virtual environment

    `virtualenv -p python3 monk`
 
    `workon monk`
 
3. Setup Dependencies

 ##### Install dependencies for Linux CPU-only
 
    `cd monk_v1/installation`
 
    `pip install -r requirements-cpu.txt`
 
 ##### Install dependencies for MacOS CPU-only
 
    `cd monk_v1/installation`
 
    `pip install -r requirements-cpu_macos.txt`
 
 ##### Install dependencies for systems with GPU
 
For CUDA == 9.0

    `cd monk_v1/installation`
 
    `pip install -r requirements-cu9.txt`
 
For CUDA == 10.0 (Colab/Kaggle)

    `cd monk_v1/installation`
 
    `pip install -r requirements-cu10.txt`
 

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

`!pip install Augmentor`

`import Augmentor`

`p = Augmentor.Pipeline("C:\\Users\soura\Desktop\Images")`

`p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)`

`p.rotate90(probability=0.5)`

`p.rotate270(probability=0.5)`

`p.flip_left_right(probability=0.75)`

`p.flip_top_bottom(probability=0.5)`

`p.crop_random(probability=1, percentage_area=0.5)`

`p.resize(probability=1.0, width=80, height=80)`

`p.random_brightness(probability = 0.5, min_factor=0.4, max_factor=0.9)`

`p.random_color(probability=0.5, min_factor=0.4, max_factor=0.9)`

`p.random_contrast(probability=0.5, min_factor=0.9, max_factor=1.4)`

`p.random_distortion(probability=0.5, grid_width=7, grid_height=8, magnitude=9)`

`p.random_erasing(probability=0.5, rectangle_area=0.4)`

`p.zoom(probability=0.7, min_factor=1.1, max_factor=1.5)`

###### #change the samples size according to requirements
`p.sample(100)`


## Hyperparameter Tuning

###
###
###
###


## Training

## Train test validation
## Performance tuning
## Possible tuning analytic
## Comparison with benchmarks
## Deployment

## Conclusion

