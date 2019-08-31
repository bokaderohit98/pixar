# P!XAR

###### The project aims at colorizing black and white pictures using deep-learning, more specifically by making use of U-Net architecture and LAB color format.


## Getting started

### 0. Install Git LFS

###### Since One of the model size exceeds 50mb it is hosted using Git LFS to clone the repo you need to install Git LFS first in your machine.

[Install Git LFS from here](https://help.github.com/en/articles/installing-git-large-file-storage)

### 1. Install Dependencies

`python ./setup/downloadDependencies.py`

### 2. Download Unet

`python ./setup/downloadModel.py`

###### Due to large size of the model it has to be hosted on google drive. But this script lets you download the model at the appropriate location. Just run the script and complete google auth to download the Unet Model.

### 3. Start development server

`python server.py`

### 4. Mock a client (If you need to test a api)

`python client.py -i image_name.extension -p pixify_image?`

###### Args:

- -i : name of image present in client_images folder
- -p : whether to pixify images or not. Accepted values are 'True' or 'False'

###### The image provided in client script must be present in **client_images** folder and the results would be stored in **client_images** folder as well.

###### If the input images is to be pixified then the image should be really small in dimensions otherwise it would lead to exhaustion of resources.


### 5. Head over to localhost:5000 to see the app in action.

###### For Client side development clone [this repository](https://github.com/bokaderohit98/pixar-ui) in current folder. i.e. in pixar. And follow the instructions give in the repository.

---
## API Reference 

### /
- Home endpoint
- returns index.html

### /path:path_name
- Endpoint to serve static files
- path_name is the path to any static file on server

### /api?pixify=value
- Api endpoint to color and pixify image.
- Here value can be `True` or `False` depending upon whether you want to increase the resolution of image or not. 