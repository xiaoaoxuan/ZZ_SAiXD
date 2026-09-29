import cv2


class Camera:
    def __init__(self,CAM_ID):

        self.CAM = cv2.VideoCapture(CAM_ID)
        if not self.CAM.isOpened():
            print("无法打开摄像头，请检查是否被其他程序占用。")
            exit()
    def release(self):  
        self.release()

    def get_frame(self):
        while 1:
            ret, frame = self.read()
            if not ret:
                break

        return frame






