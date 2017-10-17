import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("itcollege")


import ntptime
ntptime.settime()

import ubinascii as binascii
name = "esp-%s" % binascii.hexlify(wlan.config("mac")[-3:]).decode("ascii")

import gc
gc.collect()
