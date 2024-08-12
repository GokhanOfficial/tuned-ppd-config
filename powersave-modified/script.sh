#!/bin/bash

echo "low" | sudo tee "/sys/class/drm/card1/device/power_dpm_force_performance_level" > /dev/null

