#============引入头文件============#
import cv2
import sys
import time

#============rknn模型加载==========#  
from rknn_func.rknnpool import rknnPoolExecutor
from rknn_func.func import myFunc

from ultralytics import YOLO

class Model_Type:
    Type_PT = 1
    Type_ONNX = 2
    Type_RKNN = 3

class Model_Loader:

    def __init__(self,ModelPath,ModelType):
        self.model_path = ModelPath
        self.model_type = Model_Type.Type_ONNX
        self.model = None

    #模型初始化
    def Model_Init(self):
        if   self.model_type == Model_Type.Type_PT :
            self.model = YOLO(self.model_path)

        elif self.model_type == Model_Type.Type_ONNX :
            self.model = YOLO(self.model_path)

        elif self.model_type == Model_Type.Type_RKNN :
            self.pool = rknnPoolExecutor(rknnModel=self.model_path, TPEs=3, func=myFunc)
          

    #图形识别，帧更新
    def Update(self,frame):
        if   self.model_type == "pt":
            result = self.model.predict(frame, conf=0.5, verbose=False)
            return result[0].plot()
        
        elif self.model_type == "onnx":
            result = self.model.predict(frame, conf=0.5, verbose=False)
            return result[0].plot()

        elif self.model_type == "rknn":
            self.pool.put(frame)
            (frame, center), flag = self.pool.get()
            result = frame.copy()
            return result 
                    
        