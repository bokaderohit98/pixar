# P!XAR
###### The project aims at colorizing black and white pictures using deep-learning, more specifically by making use of U-Net architecture and LAB color format.

# _____________

# Getting started

### 1. Install Dependencies and Unet Model
`python setup.py`
###### Due to large size of the model it can't be pushed to github. Therefor it's hosted on google drive. The setup script would download all the required dependencies and the model at appropriate location.

### 2. Start development server 
`python app.py`

### 3. Mock a client
`python client.py -i image_name.extension`

###### The image provided in client script must be present in **client_images** folder and the results would be stored in **client_images** folder as well.    