yastfli (Yet Another Script To Flash LiveOS ISOs)
=================================================

Introduction
------------

`yastfli`, pronounced *just fly*, is a simple script that copies Fedora Live
ISOs to USB memory sticks or external drives and adds an overlay for persistent
storage. It supports `ext4` and `FAT32` for the data partition, as well as
image or directory overlays for `ext4`.

I started writing `yastfli` after investigating why `livecd-iso-to-disk` had
not been fully functional since Fedora 37 [1][2][3][4]. This is not an attempt
to replace `livecd-iso-to-disk`, which offers many features beyond what I
intend to add to `yastfli`. However, possibly due to its inherent complexity,
no one has stepped up to fix it so far. This has led to several community
efforts, including this one, to create a simpler script that can at least add
an overlay for persistent storage to Fedora Live images.

- [1] https://bugzilla.redhat.com/show_bug.cgi?id=2180524
- [2] https://bugzilla.redhat.com/show_bug.cgi?id=2152842
- [3] https://github.com/livecd-tools/livecd-tools/issues/253
- [4] https://github.com/livecd-tools/livecd-tools/issues/262

How to use yastfli
------------------

In normal mode, `yastfli` destroys all existing data on the target drive.  
If you need a tool that preserves existing data while adding a new Live OS,
`yastfli` is not suitable.  
If you are unsure what that means, this tool is probably not for you either.  
It only takes one moment of confusion between `/dev/sda` and `/dev/sdb` to wipe
your hard drive and cause serious data loss.

With that disclaimer out of the way, let's take a quick look at the help option.

``` 
 SYNTAX

 (sudo) yastfli [options] --iso <path> --target <device>

 OPTIONS

 --directory|-d
   Use a directory overlay instead of an image file.
   Cannot be used with FAT32. The size option is ignored.
   Default: false.

 --filesystem|-f [ext4|fat32]
   Filesystem of the data partition.
   Default: ext4.

 --iso|-i
   Path to the Live ISO file.

 --label|-l
   Label of the data partition.
   Default: LIVE.

 --no-overlay|-n
   Do not create an overlay.
   Default: false.

 --preserve|-p
   Do not format EFI and data partitions.
   Deletes EFI, images, and LiveOS folders instead. Deletes overlay.
   Default: false.

 --size-mb|-s
   Size in MB of the overlay file.
   Cannot exceed 4095 for FAT32 data partitions.
   Default: 512.

 --target|-t
   Target device, e.g. /dev/sda.

 --help|-h
   Display this help message.
```

You will need root access, or the ability to run `yastfli` with `sudo`.
At a minimum, you must provide the path to the ISO file and the target
device.

    sudo ./yastfli -i path/to/ISO -t /dev/sdX

If no other arguments are provided, `yastfli` will use `ext4` for the data
partition and create a 512M overlay image.

To create a larger overlay image, use the `-s` option:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -s 2048

To use `FAT32` instead of `ext4` for the data partition, use `-f fat32`. The
overlay image will be limited to 4095M, and a directory overlay cannot be used:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -s 2048 -f fat32

To use a directory overlay, the data partition must be `ext4` (the default).
Enable it with `-d`:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -d

To skip creating any overlay, use `-n`. Any overlay-related options provided in
error will be ignored:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -n

To set a custom label for the data partition, use `-l mylabel`. This option
works with all other options, but note that the label is not sanitised to
comply with filesystem requirements:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -l MY_LABEL

Preserve mode
-------------

While `--preserve` (`-p`) is just another option like those above, it requires
further explanation, so it has its own section.

**Disclaimer:** You should not use `yastfli` with any device containing data
you cannot afford to lose. This includes using the preserve option, as things
can still go wrong from time to time.

In normal mode, `yastfli` formats the entire target device and creates two
partitions: an EFI partition and a data partition.  
The preserve option skips formatting and instead deletes the EFI and `images`
folders on the EFI partition, as well as the `LiveOS` folder on the data
partition, which contains the overlay, whether it is a file overlay or a
directory overlay.

The preserve feature assumes that you have already created a bootable LiveOS
device with `yastfli` and only want to refresh the image without deleting files
or folders on the data partition outside the LiveOS structure.

With this in mind, options like `--filesystem` (`-f`) or `--label` (`-l`) are
irrelevant when using preserve, as they only apply when formatting. You also
cannot use a directory overlay if the data partition is FAT32.

To use the preserve option, simply add it to the command line:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -p

You can combine it with some other options, such as a directory overlay on
`ext4`:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -p -d

Or specify a custom overlay size:

    sudo ./yastfli -i path/to/ISO -t /dev/sdX -p -s 2048

Does yastfli work with other distributions?
-------------------------------------------

`yastfli` can write OpenSUSE Live images, but they do not boot. Ubuntu uses a
very different structure, and there are other tools better suited for it.

In summary, it may be possible to write some other distributions, but it is
unlikely to result in a bootable Live OS with a persistent overlay.
