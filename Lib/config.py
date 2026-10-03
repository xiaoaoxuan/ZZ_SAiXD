import sys

#摄像头id
class Config_Camera:
    ID_CAM = "/dev/video0"



#模型
class Config_Model:
    PATH_DEFAULT_MODEL_RKNN = sys.path[0] + "/ModelFile/yolov5s_relu_tk2_RK3588_i8.rknn"
    PATH_DEFAULT_MODEL_ONNX = sys.path[0] + "/ModelFile/1.onnx"


#Servo 
class Config_Servo:
    CONUT = 2
    DEFAULT_SPEED_MAX = 1000
    DEFAULT_SPEED_MIN = 10
    DEFAULT_POS_MAX = 1023    # 12位数字舵机极限
    DEFAULT_POS_MIN = 10
    DEFAULT_SPEED = 500
