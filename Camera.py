import cv2


class Camera:
    def __init__(self,CAM_ID):

        self.CAM = cv2.VideoCapture(CAM_ID)
        
        if not self.CAM.isOpened():
            print("❌无法打开摄像头，请检查是否被其他程序占用")
            exit()
        print("✅摄像头已打开")

    def release(self):  
        self.release()
        print("✅摄像头已释放")

    def get_frame(self):
        while 1:
            ret, frame = self.CAM.read()
            if not ret:
                break
        return frame






