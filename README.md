# yastfli (Yet Another Script To Flash LiveOS ISOs)

## Introduction
`yastfli`, pronounced justfly, is a relatively simple script to copy Fedora Live ISOs onto USB memory sticks and external drives, with an overlay for permanent storage. It supports `ext4` and `fat32` for the data partition, as well as image or directory types of overlay for `ext4`.

I came about writing it after I started looking into `livecd-iso-to-disk` not fully working since Fedora 37 [1][2][3][4]. It is not an attempt at replacing `livecd-iso-to-disk`, which has many options and it can do a lot more than I would ever care to add to `yastfli`. Possibly due to the inherent complexity of `livecd-iso-to-disk`, no one has stepped up to fix it so far, leading to some attempts amongst the community, including this, to produce a script that can, at least, add an overlay for permanent storage to Fedora Live.

[1] https://bugzilla.redhat.com/show_bug.cgi?id=2180524
[2] https://bugzilla.redhat.com/show_bug.cgi?id=2152842
[3] https://github.com/livecd-tools/livecd-tools/issues/253
[4] https://github.com/livecd-tools/livecd-tools/issues/262

## How to use it
`yastfli` will destroy all existing data on the target drive. If you are looking for a tool that would preserve existing data, while adding the new Live OS, `yastfli` is not the right tool. If you don't truly understand what I mean by that, this is probably not for you either. It only takes a moment of confusion between using `/dev/sda` or `/dev/sdb` to wipe out your hard drive and get yourself into a big mess.

With the above disclaimer out of the way, let’s take a quick look at the help option.

``` 
 SYNTAX

 (sudo) yastfli [options] --iso <path> --target <device>

 OPTIONS

 --directory|-d
   Use a directory overlay instead of an image file.
   It can't be used with fat32. Size option would be ignored.
   Default is false.

 --filesystem|-f [ext4|fat32]
   Filesystem of the data partition.
   Default is ext4.

 --iso|-i
   Path to Live ISO file.

 --label|-l
   Label of the data partition.
   Default is LIVE.

 --no-overlay|-n
   Don't create an overlay.
   Default is false.

 --size-mb|-s
   Size in MB of the overlay file.
   It can't be more than 4095 for fat32 data partitions.
   Default is 512.

 --target|-t
   Target device e.g. /dev/sda.

 --help|-h
   This help.
```
You will need root access or to be able to run `yastfli` with `sudo` and, at the very least, you will have to provide the path to the ISO file and the target device that you want to write it to.

```
sudo ./yastfli -i path/to/ISO -t /dev/sdX
```
If no other argument is provided, `yastfli` will use `ext4` for the data partition and create an overlay image of 512M.

To create a larger overlay image, you would use `-s size`.
```
sudo ./yastfli -i path/to/ISO -t /dev/sdX -s 2048
``` 
To use `fat32` instead of `ext4` for the data partition, you would use `-f fat32`. The size of the overlay image would be limited to 4095M and you would not be able to use a directory overlay.
```
sudo ./yastfli -i path/to/ISO -t /dev/sdX -s 2048 -f fat32
```
If you preferred to use a directory overlay, your only option is `ext4` which is the default file system for the data partition and you would enable it with `-d`.
```
sudo ./yastfli -i path/to/ISO -t /dev/sdX -d
```
If you did not want to create any overlay at all, you would use `-n`. Any overlay-related option used in error would be ignored.
```
sudo ./yastfli -i path/to/ISO -t /dev/sdX -n
```
If you preferred to use your own label for the data partition, you would use `-l mylabel`, which is compatible with all the other options, but be aware that it isn’t sanitised to make it compliant with either file format’s requirements.
```
sudo ./yastfli -i path/to/ISO -t /dev/sdX -l MY_LABEL
```
## Does it work with other distributions?
I know for a fact that it can write OpenSUSE Live, but it doesn’t boot. Ubuntu uses a very different structure, but you have plenty of other options for it. In summary, it is possible that you can complete the process with some other distributions but not very likely that it will actually result on a bootable Live OS with persistent overlay.