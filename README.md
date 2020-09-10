# debloat-android-phone-noroot
Easily debloat android phones without root

# Getting Started
You need the following:

-ADB\
-Command-line application\
-Windows/Mac/Linux PC\
-Whatever USB cable your phone uses\
-A phone that actually turns on and operates\

How to use ADB: https://www.xda-developers.com/install-adb-windows-macos-linux/


# What does this do and how does it work?

Removing applications using pm on android will remove applications from your user account on the device, while leaving the applications still on the device. This makes it relatively harmless and it's entirely possible to simple re-add the applications at a later date.

# So I have all the requirements. What do I do?

Run the adb shell and ensure your device is fully connected, next pick a text file from this repository that matches your intent, copy the entire file, paste it into your terminal, and watch all the applications get removed/reinstalled.

# Removing a specific app fucked up X on my phone what the fuck?! How do I get it back?

If you're still able to boot the device up to at least the lock screen, you can simply re-add the application package by executing "cmd package install-existing <packagename>" without quotes. If the device fails to fully boot up, fortunately (and unfortunately) a hard reset will fix the issue right up.\
  
If you want to go undo what you have done in its entirety, I have another file with all the commands needed to undo everything done.
  
 # More info
 
 If you want to add more bullshit Android packages to the bloatware command list, make a pull request and I'll put them in there. I hate the fact that Android has to ship so heavily laden with bloatware to the point that it eats a notice-able fraction of the device's battery life and it's often the reason iPhone users believe Android phones are worse than they really are.\
 
 If you really wish to debloat an Android phone, I highly recommend installing TWRP and rooting it to get proper system access, but I also understand that not all phones are root-able and the users of said phones may want to clean up their devices too.
