# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
"""This example turns on the little red LED."""
from adafruit_circuitplayground import cp
from time import sleep

while True:
    cp.red_led = True
    sleep(1)
    cp.red_led = False
    sleep(1)
