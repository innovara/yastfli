Name:           yastfli
Version:        0.0.1
Release:        1%{?dist}
Summary:        Script to copy Fedora Live ISOs onto USB memory sticks and external drives
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
yastfli, pronounced justfly, is a relatively simple script to copy Fedora Live
ISOs onto USB memory sticks and external drives, with an overlay for permanent
storage. It supports ext4 and fat32 for the data partition, as well as image or
directory types of overlay for ext4.


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
* Fri Feb 28 2025 Manuel Fombuena <mfombuena@innovara.co.uk>
- Version 0.0.1-1: first rpm package

