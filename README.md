# debloat-android-phone-noroot
Easily debloat android phones without root!

note: this is a tool I personally use for convenience when I factory reset or buy a new phone or something and find that it's either risky to root or impossible. I feel like this should still be public for simplicity's sake however.

This was created using an LG Risio 4 (LG K31 Cricket)

# Getting Started
You need the following:

-ADB\
-Command-line application\
-Linux PC. Untested on Win/Mac.\
-Whatever USB cable your phone uses\
-A phone that actually turns on and operates\
-Python 3+

How to use ADB: https://www.xda-developers.com/install-adb-windows-macos-linux/


# What does this do and how does it work?

Removing applications using pm on android will remove applications from your user account on the device, while leaving the applications still on the device. This makes it relatively harmless and it's entirely possible to simple re-add the applications at a later date.

You also should get the added benefit of increased battery life if you nuke Google. Nobody really knows why GSF takes so much battery but it is what it is.

# So I have all the requirements. What do I do?

Run the adb devices and ensure your device connects and is seen. Next, simply run the run.py file in this folder to get started.

# Removing a specific app fucked up X on my phone what the fuck?! How do I get it back?

If you're still able to boot the device up to at least the lock screen, you can simply re-add the application package by executing "cmd package install-existing PACKAGENAME" without quotes. If the device fails to fully boot up, fortunately (and unfortunately) a hard reset will fix the issue right up.

You can see all the packages which were removed by this program by going into the ./logs/ directory.

If you want to go undo what you have done in entirety, select option 3.

 # More info

 If you want to add more bullshit Android packages to the bloatware command list, make a pull request and I'll put them in there. I hate the fact that Android has to ship so heavily laden with bloatware to the point that it eats a notice-able fraction of the device's battery life (and performance big time) and it's often the reason iPhone users believe Android phones are worse than they really honestly are.

 If you really wish to debloat an Android phone, I highly recommend installing TWRP and rooting it to get proper system access, but I also understand that not all phones are root-able and the users of said phones may want to clean up their devices too.
