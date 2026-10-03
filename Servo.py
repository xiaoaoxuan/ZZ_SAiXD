from Lib.config import Servo
from Lib.uptech import UpTech
import time 

class Servo_D:

    def __init__(self, Count):
        self.Count = Count
        self.Sero = UpTech()
        self.Sero.CDS_Open()
        for SID in range(max(1,min(255,Count))):
            # 默认初始化模式为舵机模式
            self.Sero.CDS_SetMode(SID,self.Sero.CDS_MODE_SERVO)
        time.sleep(0.3)

    #设置所有舵机模式
    def Set_ALL_Mode(self,Mode):
        if Mode == self.Sero.CDS_MODE_SERVO or Mode == self.Sero.CDS_MODE_MOTOR:
            for SID in range(max( 1, min( 255, self.Count))):
                self.Sero.CDS_SetMode( SID, Mode)

    #设置所有舵机角度
    def Set_ALL_Angel( self, Angle, Speed=Servo.DEFAULT_SPEED):
        for SID in range(max(1,min(255,self.Count))):
            self.Sero.CDS_SetAngle( SID, Angle, Servo.DEFAULT_SPEED)

    #设置单个舵机角度
    def Set_Angel( self, SID, Angle, Speed=Servo.DEFAULT_SPEED):
        self.Sero.CDS_SetAngle( SID, Angle, Speed)

