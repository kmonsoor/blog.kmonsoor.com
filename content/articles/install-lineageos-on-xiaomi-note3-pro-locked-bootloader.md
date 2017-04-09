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
  * Tool to boot into EDL-download mode. Here.
  * Custom TWRP recovery image, ZCX_TWRP_0917.zip. Here.
  * MIUI Developer ROM for Kenzo. Version 6.11.3_20161103 is proven to be working. Other version may not. Get it here.
  * Updated firmware for kenzo. Get it here. Details here.
  * The main OS; LineageOS 14.1, get the latest one from this page.
  * Google Playstore and other necessary services packed in one, possible by Open GApps Project. Get yours here. Make sure you have selected Arm64-7.1-Pico package.
  * (optional) SU package to able to use your device as "rooted"
  
 
