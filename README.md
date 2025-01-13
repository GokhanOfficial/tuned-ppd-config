My Repository for Linux Experience (Acer Aspire A515-47)

# My Bash/Python Scripts
bmp_to_jpg.py: Converts all .bmp files to .jpg files. Move original photos to "Original" folder.
png_to_jpg.py: Converts all .png files to .jpg files. Move original photos to "Original" folder.
check_mp3_mp4_integrity.py: Checks all .mp3 and .mp4 files integrity with ffmpeg and ask for deleting broken files.
photo_check.py: Check all .jpg and .bmp files for integrity errors. Ask for deleting broken files.
jpg_compress.py: Compress .jpg files with selected compression ratio.
remove_space_after_folder_names.sh: Removes space chracter after folder and file names. There is space chracters because rclone Google Drive downloading.

# Tuned-PPD Config
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

# Quanta-HD-User-Facing-0x0408-0x4035_linux
This is a clone from this repository:
https://github.com/fus0g/Quanta-HD-User-Facing-0x0408-0x4035_linux
