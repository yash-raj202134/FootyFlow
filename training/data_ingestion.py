from roboflow import Roboflow

import os
import shutil
from dotenv import load_dotenv , set_key
load_dotenv() 


rf = Roboflow(api_key=os.getenv("roboflow_api_key"))

os.chdir('./training')

project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(1)
dataset = version.download("yolov5")


# Save dataset.location path 


shutil.move('football-players-detection-1/train',
            'football-players-detection-1/football-players-detection-1/train'
            )

shutil.move('football-players-detection-1/test',
            'football-players-detection-1/football-players-detection-1/test'
            )

shutil.move('football-players-detection-1/valid',
            'football-players-detection-1/football-players-detection-1/valid'
            )



