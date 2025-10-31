Name:           yastfli
Version:        0.0.4
Release:        1%{?dist}
Summary:        Script to copy Fedora Live ISOs to USB drives with persistent storage
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/innovara/yastfli
Source0:        %{name}-%{version}.tar.gz

Requires:       bash
Requires:       coreutils
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       findutils
Requires:       parted
Requires:       rsync
Requires:       sed
Requires:       udisks2
Requires:       util-linux
Requires:       util-linux-core


%description
yastfli, pronounced "just fly", is a simple script that copies Fedora Live ISOs
to USB memory sticks or external drives and adds an overlay for persistent
storage. It supports ext4 and FAT32 data partitions, as well as image or
directory overlays for ext4.


%prep


%autosetup


%build


%install

mkdir -p %{buildroot}/%{_bindir}
%{__install} -Dm755 %{name} %{buildroot}/%{_bindir}

%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/%{name}


%post


%preun


%postun


%changelog
* Fri Oct 31 2025 Manuel Fombuena <mfombuena@innovara.tech> - 0.0.4-1
- AI-assisted proofreading of documentation
- Implement rpmlint fixes

* Mon Apr 14 2025 Manuel Fombuena <mfombuena@innovara.tech> - 0.0.3-1
- Add support for Fedora 42

* Tue Mar 4 2025 Manuel Fombuena <mfombuena@innovara.tech> - 0.0.2-1
- Add new clean up routine

* Fri Feb 28 2025 Manuel Fombuena <mfombuena@innovara.tech> - 0.0.1-1
- First rpm package
