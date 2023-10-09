from engi1020.arduino.api import*
from time import sleep
 
print('Grove Alarm System')
sleep(3)
print('Press 1 to calibrate and setup')
print('Press 2 to arm the alarm')
sleep(2)
print('To turn the alarm off, press and hold button for 5 seconds')
isArmed = False
isOff = False

while digital_read(6) == False:
    choice = input('Press a button: ')
    if choice  == '':
        break

    elif choice == '1':
        def_dist = ultra_get_centimeters(4)
        print(def_dist)

    elif choice == '2':
        isArmed = True
        while isArmed == True and digital_read(6) == False:
            dist = ultra_get_centimeters(4)
            print(dist)
            if dist < def_dist:
                isOff = True
                buzzer_frequency(5,500)
                oled_clear()
                oled_print('Intruder Detected!')

            while isOff == True:
                if digital_read(6) == True:
                    isOff = False
                    buzzer_stop(5)
                    oled_clear()
                    oled_print('Reset')
                    sleep(2)
                    oled_clear()
                    break
                
