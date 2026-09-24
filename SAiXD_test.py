#============引入头文件============#
import cv2
import sys
import time

#============rknn模型加载==========#  
from rknn_func.rknnpool import rknnPoolExecutor
from rknn_func.func import myFunc

#from ultralytics import YOLO

class Model_Loader:
    def __init__(self,ModelPath,ModelType):
        self.model_path = ModelPath
        self.model_type = ModelType #rknn pt onnx
        self.model = None
        self.pool  = None
        self.cam   = cv2.VideoCapture(0)

    #模型初始化
    def Model_Init(self):
        if   self.model_type == "pt":
            pass

        elif self.model_type == "rknn":
            self.pool = rknnPoolExecutor(rknnModel=self.model_path, TPEs=3, func=myFunc)
            
        elif self.model_type == "onnx":
            pass

    #图形识别，帧更新
    def Update(self,frame):
        if   self.model_type == "pt":
            pass
        
        elif self.model_type == "rknn":
            self.pool.put(frame)
            (frame, center), flag = self.pool.get()
            result = frame.copy()
            return result 
                    
        elif self.model_type == "onnx":
            pass



#====初始化部分====#
model_path = sys.path[0] + "/rknnModel/yolov5s_relu_tk2_RK3588_i8.rknn"
test = Model_Loader(model_path,"rknn")
test.Model_Init()

while 1:
    
    pass    




