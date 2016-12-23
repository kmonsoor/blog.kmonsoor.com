---
Title: Increase virtual disk size in VirtualBox on Windows 7:Step-by-step
Date: 2012-05-26 08:02
Tags: virtualbox, vpc, ubuntu, linux, windows
Slug: increase-virtual-disk-size-in-virtualbox-windows7-opensuse
Status: Published
Summary: Stuck with your small virtual disk partition for VirtualBox? You created for some testing & practicing, now it needs space. I also stuck with same problem; researched many forums, and here is the gist. Find out how.

---
 
Stuck with your small virtual disk partition for VirtualBox? You created for some testing & practicing, now it needs space. I also stuck with same problem; researched many forums, and here is the gist.

[Note: This procedure won't work for VM with snapshots. So, plz take note about your system beforehand.]

 * Download Gparted, disk manager for Linux. It'll come as an ISO file.
 * Boot into your guest OS, check,  with df command,  which partition you need to grow. Take note of that specific mounted HD, such as /dev/hdb/sda3
 * Take backup of your existing data, as I WILL NOT TAKE ANY RESPONSIBILITY IF YOU DAMAGE YOUR DATA.
 * In host OS, Goto the command prompt by running, cmd.exe
 * Navigate to the Virtualbox installation folder
 * Execute command: 
     
`VBoxManage modifyhd X:\yourVM_DiskPath_InHost\yourVM_Disk.vdi  --resize 40960`
     
  you will see progress as below:

![10% ... 20% .. .. 100%](http://i.imgur.com/iYORelg.png)
 
  If you fail with message like

> "VBoxManage.exe: error: Resize hard disk operation for this format is not implemented yet!"

  you need to use this tool [CloneVDI.exe](https://forums.virtualbox.org/download/file.php?id=7579) from this VirtualBox forum-post. If using this tool, remember to check "Increase virtual drive size to " with your desired size.

![VDI_tool](http://i.imgur.com/YB49ZVk.png)

 * Now, Load the ISO file to the CD/DVD drive of your virtual Linux.

![GParted.iso loaded on IDE Primary Master](http://i.imgur.com/UKyPkl8.png)

 * Boot the Guest OS; from the boot menu, select CD/DVD drive, then it will be booted in GParted tiny OS. Now the PartitionManager tool will come up automatically, like below:

![](http://i.imgur.com/aK9kAtK.jpg)

 * Now "shrink/Grow" or "Move" your desired partion, but be careful. Don't rename any of them. Be careful about your data.
 * Don't worry, unless you clicked Apply, nothing has happened really. When you are done with moving and resizing, you have to click `Apply` to commit the change

![](http://i.imgur.com/wUMCHVQ.jpg)

 * when completed, close Gparted, and then shutdown the OS
 * Unload the ISO aka virtual CD from virtual OS
 * Boot into the virtual OS again
 * Now, check that if the desired partition grew or not by df command

Thanks for visiting my blog. If it just helped it, please feel free to "Like" or "share".  Also, your suggestion or comment would be greatly inspiring.

You may also like to encourage me by [buying me a coffee](paypal.me/kmonsoor/).
