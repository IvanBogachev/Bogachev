import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]

def decimal2binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]


GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        num = input("Введите число от 0 до 255:")
        if type(num) == int:
            print("Введено не целое число")
            break
        try:
            num = int(num)
            if 0<=num<=255:
                GPIO.output(dac, decimal2binary(num))
                volt = float(num)/ 256 * 3.3
                print("Выходное напряжение: ", volt, " вольт")
          
            else:
               
                if num < 0:
                    print("Введено отрицательное число!!!")
                elif num > 255:
                    print("Введено число превышающеее возможности 8-разрядного ЦАП!!!")
                else:
                    print("Введено не число!!!")
        except Exception:
            if num == "q": break            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    





