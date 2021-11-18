---
Title: Increase virtual-disk size in VirtualBox on Windows 7
Date: 2012-05-26 08:02
Update: 2017-01-01 11:59
Tags: virtualbox, vpc, ubuntu, Linux, windows, storage
Slug: increase-virtual-disk-size-in-virtualbox-windows
Status: Published
Summary: Stuck with your small virtual disk partition for VirtualBox? I also stuck with same problem; researched many forums, and here is the gist. Find out how.
---

Are you stuck with your small virtual disk partition for VirtualBox? You created the partition for some testing & practicing, now it needs more space. I was also stuck with the same problem; so I researched many forums, and here is the gist.

[Note: This procedure won't work for VM with snapshots. So, please take note the fact about your system beforehand.]

 * Download [Gparted](http://gparted.org/download.php), disk manager for Linux. It'll come as an ISO file.
 * Boot into your guest OS, check,  with df command,  which partition you need to grow. Take note of that specific mounted HD, such as /dev/hdb/sda3
 * Take backup of your existing data, as I WILL NOT TAKE ANY RESPONSIBILITY IF YOU DAMAGE YOUR DATA.
 * In host OS, Goto the command prompt by running, cmd.exe
 * Navigate to the Virtualbox installation folder
 * Execute the command:

```shell-session
C:\ VBoxManage modifyhd X:\yourVM_DiskPath_InHost\yourVM_Disk.vdi  --resize 40960
```

  you will see progress as below:

![10% ... 20% .. .. 100%](http://i.imgur.com/iYORelg.png)

  If you fail with a message like thid

> "VBoxManage.exe: error: Resize hard disk operation for this format is not implemented yet!"

  Now, you need this tool [CloneVDI.exe](https://forums.virtualbox.org/download/file.php?id=7579) from this VirtualBox forum-post. If you're using this tool, remember to check "Increase virtual drive size to " with your desired size.

![VDI_tool](http://i.imgur.com/YB49ZVk.png)

 * Now, Load the ISO file to the CD/DVD drive of your virtual Linux.

![GParted.iso loaded on IDE Primary Master](http://i.imgur.com/UKyPkl8.png)

 * Boot the Guest OS; from the boot menu, select CD/DVD drive, then it will boot in GParted tiny OS. Now the PartitionManager tool will come up automatically, like below:

![Gparted partition-manager](http://i.imgur.com/aK9kAtK.jpg)

 * Now "shrink/Grow" or "Move" your desired partition, but be careful. Don't rename any of them. Be careful about your data.
 * Don't worry, unless you clicked Apply, nothing has actually took place. When you are done with moving and resizing, you have to click **`Apply`** to commit the change

![just before applying](http://i.imgur.com/wUMCHVQ.jpg)

 * Once completed, close Gparted, and then shutdown the OS
 * Unload the ISO aka virtual CD from virtual OS
 * Boot into the virtual OS again
 * Now, check that if the desired partition grew or not by using the `df` command

Thanks for visiting my blog. If it just helped you, please feel free to "Like" or "share".  Also, your suggestion or comment would be great as well.

---
If you find this post helpful, you can show your support [through Patreon](https://www.patreon.com/kmonsoor) or [Paypal](https://paypal.me/KhaledMonsoor/) or by [buying me a coffee](https://ko-fi.com/kmonsoor). *Thanks!*
