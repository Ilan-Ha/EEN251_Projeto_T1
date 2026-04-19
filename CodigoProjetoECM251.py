from machine import Pin, time_pulse_us
from utime import sleep_us, sleep

relay = Pin(18, Pin.OUT)
trigger = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)
ldr = Pin(19, Pin.IN)
led = Pin(20, Pin.OUT)

DELAY_RELAY_ON = 3

DELAY_RELAY_OFF = 0

def ldr_led_control():
    if ldr.value():
        led.value(1)
    else:
        led.value(0)
      
def send_pulse_and_wait():
        """
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
        """
        trigger.value(0) # Stabilize the sensor
        sleep_us(5)
        trigger.value(1)
        # Send a 10us pulse.
        sleep_us(10)
        trigger.value(0)
        try:
            pulse_time = time_pulse_us(echo, 1, 30000)
            # time_pulse_us returns -2 if there was timeout waiting for condition; and -1 if there was timeout during the main measurement. It DOES NOT raise an exception
            # ...as of MicroPython 1.17: http://docs.micropython.org/en/v1.17/library/machine.html#machine.time_pulse_us
            if pulse_time < 0:
                MAX_RANGE_IN_CM = 500 # it's really ~400 but I've read people say they see it working up to ~460
                pulse_time = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

def distance_mm():
        """
        Get the distance in milimeters without floating point operations.
        """
        pulse_time = send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        mm = pulse_time * 100 // 582
        return mm
    
def turn_relay_on():
    relay.value(0)
    sleep(DELAY_RELAY_ON)
def turn_relay_off():
    relay.value(1)
    sleep(DELAY_RELAY_OFF)
    
def control_pump_by_distance_mm(target_distance_in_mm):
    if distance_mm() <= target_distance_in_mm:
        turn_relay_on()
    else:
        turn_relay_off()

while True:
    control_pump_by_distance_mm(110)
    ldr_led_control()
    
    
