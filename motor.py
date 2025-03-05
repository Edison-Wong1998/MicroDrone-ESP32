import RPi.GPIO as GPIO

class ESCController:
    def __init__(self, pins):
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins, GPIO.OUT)
        self.pwms = [GPIO.PWM(pin, 500) for pin in pins]
        
    def arm(self):
        """电调初始化"""
        for pwm in self.pwms:
            pwm.start(0)
    
    def adjust_motors(self, roll, pitch):
        """简化版电机控制"""
        speeds = [
            50 + roll*10 - pitch*5,  # 电机1
            50 - roll*10 + pitch*5,  # 电机2
            50 + roll*10 + pitch*5,  # 电机3
            50 - roll*10 - pitch*5   # 电机4
        ]
        for pwm, speed in zip(self.pwms, speeds):
            pwm.ChangeDutyCycle(max(0, min(100, speed)))
    
    def stop(self):
        """紧急停止"""
        for pwm in self.pwms:
            pwm.stop()
        GPIO.cleanup()