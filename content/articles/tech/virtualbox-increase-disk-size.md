Title: Increase virtual disk size in VirtualBox, host: Windows 7, Guest: OpenSuse. Format: Step-by-step
Date: 2012-05-26 20:19
Author: kmonsoor
Category: configuration, freeware, Linux, software, tutorial, Windows 7
Tags: enterprise-it, linux, opensuse, software, Step-by-step, suse, technology, vdi, virtual disk, virtualbox, vmware, windows 7
Slug: virtualbox-increase-disk-size
Status: published

<div>

[![](http://kmonsoor.files.wordpress.com/2012/05/virtualbox_logo_small.jpg "Virtualbox_logo_small")](http://kmonsoor.files.wordpress.com/2012/05/virtualbox_logo_small.jpg)

</div>

<div>

</div>

<div>

</div>

<div>

   Stuck with your small virtual disk partition for VirtualBox? You
created for some testing & practicing, now it needs space. I also stuck
with same problem; researched many forums, and here is the gist. Find
out how \>\>\>

</div>

<!--more-->

**[ Update**: (Thanks to user, Suman) This procedure **won't work for VM
with snapshots**. So, plz take note about your system beforehand. **]**

-   Download [***Gparted***, disk manager for
    Linux](http://sourceforge.net/projects/gparted/). It'll come as an
    ISO file.
-   Boot into your guest OS, check,  with ***df*** command,  which
    partition you need to grow. Take note of that specific mounted HD,
    such as /dev/hdb/sda3
-   Take backup of your existing data, as I **WILL NOT** TAKE ANY
    RESPONSIBILITY IF YOU DAMAGE YOUR DATA.
-   In host OS, Goto the command prompt by running, ***cmd.exe***
-   Navigate to the Virtualbox installation folder
-   Execute command:*VBoxManage modifyhd
    X:\\yourVM\_DiskPath\_InHost\\yourVM\_Disk.vdi  --resize 40960* you
    will see progress as below:
-   [![](https://kmonsoor.files.wordpress.com/2012/05/screenshot002.png "ScreenShot002")](http://kmonsoor.files.wordpress.com/2012/05/screenshot002.png)

<!-- -->

-   If you fail with message like ***"VBoxManage.exe: error: Resize hard
    disk operation for this format is not impleme***  
    ***nted yet!***", you need to use this tool
    ([CloneVDI.exe](https://forums.virtualbox.org/download/file.php?id=7579))
    from this [VirtualBox
    forum-post](https://forums.virtualbox.org/viewtopic.php?f=6&t=22422).
    If using this tool, **remember** to check "**Increase virtual drive
    size to** " with your desired size.
-   [![VDI\_tool](https://kmonsoor.files.wordpress.com/2012/05/vdi_tool.png)](https://forums.virtualbox.org/download/file.php?id=7579)
-   Now, Load the ISO file to the CD/DVD drive of your virtual Linux
-   <p>
    [caption id="attachment\_185" align="aligncenter"
    width="375"][![](http://kmonsoor.files.wordpress.com/2012/05/mysuse-gparted.png "GParted ISO loaded")](http://kmonsoor.files.wordpress.com/2012/05/mysuse-gparted.png)
    GParted.iso loaded on IDE Primary Master[/caption]
-   Boot the Guest OS; from the boot menu, select CD/DVD drive, then it
    will be booted in GParted tiny OS,
-   Now the PartitionManager tool will come up automatically, like
    below:
-   [![](http://kmonsoor.files.wordpress.com/2012/05/gparted.jpg?w=300 "gparted")](http://kmonsoor.files.wordpress.com/2012/05/gparted.jpg)
-   Now shrink/Grow or Move your desired partion, but be careful. Don't
    rename them and care about your data.
-   Don't worry, unless you clicked ***Apply***, nothing has happened
    really. When you are done with moving and resizing, you have to
    click ***Apply***to commit the change
-   [![](http://kmonsoor.files.wordpress.com/2012/05/gparted11.jpg?w=300 "gparted11")](http://kmonsoor.files.wordpress.com/2012/05/gparted11.jpg)
-   when completed, close Gparted, and then shutdown the OS
-   Unload the ISO aka virtual CD from virtual OS
-   Boot into the OS again
-   Now, check that if the desired partition grew or not by df command

Thanks for visiting my blog. Please don't forget to "Like" or "+1" be
clicking below.  Also, your suggestion or comment would be greatly
helpful.

You may also like to encourage me by [buying me a
coffee](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4H7BX94Z8MW9W).
