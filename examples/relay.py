import automationhat as ah
import time

ah.light.power.write(1)

while True:
    ah.relay.one.toggle()
    ah.relay.two.toggle()
    ah.relay.three.toggle()
    time.sleep(0.1)
