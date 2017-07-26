import os
import readConfig

proDir=readConfig.proDir

def insert_img(driver, file_name):

    base_dir=str(proDir)
    base_dir=base_dir.replace("\\","/")
    imgPath=os.path.join(base_dir,"report","image")
    if not os.path.exists(imgPath):
        os.mkdir(imgPath)
    file_path=os.path.join(imgPath,file_name)
    print(file_path)
    driver.get_screenshot_as_file(file_path)


