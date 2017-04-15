---
Title: Install LineageOS (CM) 14.1(Nougat) on Redmi-Note-3-pro (Kenzo) with locked bootloader
Date: 2017-04-08
Tags: OSS, Android, custom-rom, Xiaomi
Slug: install-lineageos-on-xiaomi-note3-pro-locked-bootloader
Status: Draft
Summary: Install LineageOS (CM) 14.1(Nougat) on Redmi-Note-3-pro (Kenzo) with locked bootloader
---

Install LineageOS (CM) 14.1(Nougat) on Redmi-Note-3-pro (Kenzo) with locked bootloader
======================================================================================

STOP HERE !

 1. If you are not familiar with the terms like root, flash, bootloader, cyanogenMod, custom-rom etc., please stop right now. This post isn't for you.
 2. Any attempt to any of these below may potentially brick your device and/or invalidate your warranty.
 3. In any case, I will NOT take any responsibility for any kind of consequence, damage or anything. 
 
 YOU HAVE BEEN WARNED !
 ...
 ..
 .
 
 Now, as you are insisting, let's go ...
 
 First things first
 ------------------
  * Make sure your device is "Xiaomi Redmi Note 3 (with Qualcomm Snapdragon SoC)". Physically, it is 150mm(=15cm) in length.
  * Any other kind of Note-3 will not (or may not) work in this method; rather it may cause bricking the device.
  * Backup ! Backup ! Backup everything you will ever need !
  
How this method works
---------------------
  * When you have locked bootloader, only Mi's own flash tool lets you flash anything. So, you'll flash the device with a MIUI Developer's ROM; but with different `Recovery.img`.
  * Now, with that custom recovery image, you will push the target OS, which is LineageOS in this case.
  * Then, you'll need to install Google `Playstore` app to be able to install app from Playstore
 
 Downloads, you must
 -------------------
 In sequence by when you will need it:
  * Tool to boot into EDL-download mode. [Here](https://www.androidfilehost.com/?fid=24591000424940129).
  * Mi Flash tool. [Here](http://api.bbs.miui.com/url/MiFlash). [To learn more](http://en.miui.com/thread-345974-1-1.html)
  * Custom TWRP recovery image, ZCX_TWRP_0917.zip. [Here](https://www.androidfilehost.com/?fid=24727332921017084).
  * MIUI Developer ROM for Kenzo. Version 6.11.3_20161103 is proven to be working. Other version may not. [Get it here](http://bigota.d.miui.com/6.11.3/kenzo_global_images_6.11.3_20161103.0000.00_6.0_global_f7309f8161.tgz).
  * Updated firmware for kenzo. [Get it here](https://www.androidfilehost.com/?fid=817550096634761596). Details [here](https://forum.xda-developers.com/redmi-note-3/how-to/cm14-14-1-aosp-n-firmware-kenzo-kate-t3507789).
  * The main target OS; LineageOS 14.1, get the latest one from [this page](https://download.lineageos.org/kenzo).
  * Google Playstore and other necessary services packed in one, possible by Open GApps Project. Get yours here. Make sure you have selected **Arm64-7.1-Pico** package.
  * (optional) SU package to able to use your device as "rooted"
 
 
 Prepare your PC and Phone
 -------------------------
 * Make sure phone can be properly connected to PC through USB
 * Install Mi Flash tool on your PC. Make sure it can detect your phone properly after the setup.
 * Copy all the binaries to a external SD-card. If you have an OTG cable, you can also use a USB drive; however, you have to make sure that the USB drive is formatted in FAT32 format. Formatted using NTFS format or anything else will NOT be usable.
 * Enable Developer options on the phone. Then, enable `Anvanced Rebbot`, and ADB access.
 
 
 Install the Recovery Image
 --------------------------
  * Reboot your phone to download mode
  * using the EDL tool, go to EDL mode on phone. This step is critical; without EDL mode, this method wont work.
  * Flash the MIUI dev edition with other recovery
  
 
