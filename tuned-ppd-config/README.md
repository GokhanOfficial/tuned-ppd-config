# tuned-ppd-config
My Tuned-PPD Config for AMD Ryzen 5625U (Acer Aspire A515-47)

Need to install "tuned-ppd" package and copy this folders to "/etc/tuned/profiles/"
Also need to edit "/etc/tuned/ppd.conf" for control with KDE Power Schemes.

Powersave
- ACPI Platform Profile: powersave
- CPU Governor: powersave
- EPP Preference: power
- Panel Saving: 1
- Turbo Boost: Off
- CPU Limited: No (2300 MHz)
- iGPU Limited: Yes (200 MHz)
- ALPM: min_power

Balanced
- ACPI Platform Profile: balanced
- CPU Governor: powersave
- EPP Preference: balance-performance
- Panel Saving: 0
- Turbo Boost: Off
- CPU Limited: No (2300 MHz)
- iGPU Limited: No (1800 MHz)
- ALPM: medium_power

Performance
- ACPI Platform Profile: performance
- CPU Governor: performance
- EPP Preference: performance
- Panel Saving: 0
- Turbo Boost: On
- CPU Limited: No (4300 MHz)
- iGPU Limited: No (1800 MHz)
- APLM: max_performance
