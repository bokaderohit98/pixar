# P!XAR
###### The project aims at colorizing black and white pictures using deep-learning, more specifically by making use of U-Net architecture and LAB color format.

# _____________

# Getting started

### 1. Install Dependencies
`python downloadDependencies.py`

### 2. Download Unet
`python downloadModel.py`
###### Due to large size of the model it has to be hosted on google drive. But this script lets you download the model at the appropriate location. Just run the script and complete google auth to download the Unet Model.

### 3. Start development server 
`python app.py`

### 4. Mock a client
`python client.py -i image_name.extension`

###### The image provided in client script must be present in **client_images** folder and the results would be stored in **client_images** folder as well.    