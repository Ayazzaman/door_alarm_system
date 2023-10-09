# door_alarm_system
A simple alarm system done as a project for a programming course.
This alarm system uses an arduino as its working brains and also utilizes a sonar sensor for the tracking.
The alarm system once setup after an initial calibration stores a decimal value of the distance between opposing doorsills and stores it.
Once armed, the sonar sensor continously measures the distance and compares it to the calibrated value, if the distance reading is lower than the calibrated reading, probably by an object coming in between the door sills, the alarm goes off
