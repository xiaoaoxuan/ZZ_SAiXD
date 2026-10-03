import cv2
import Servo
import Camera
from Lib.config import Config_Camera,Config_Model,Config_Servo
from Model_Loader import Model_Loader,Model_Type



#====初始化部分====#


def init():
    MODEL = Model_Loader(Config_Model.PATH_DEFAULT_MODEL_RKNN,Model_Type.Type_RKNN)
    CAM   = Camera(Config_Camera.ID_CAM) 
    SERVO = None ##
    



def loop():
    while 1:

        
        pass

    






if __name__ == "__main__":
    init()
    loop()