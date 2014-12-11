Summary:	Generic monitor edid files
Name:		edidbins
Version:	1.1
Release:	1
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/torvalds/linux/tree/master/Documentation/EDID
BuildArch:	noarch 

#The tarball for these files was generated from the cloned sources from the above url. The files were copied to a directory edidbins and then compressed with "tar -Jcvf kernel-edidbins edidbins/*" It is unlikely that these sources will change. Proprietary edid's should have their own package.

Source0:	kernel-edidbins-%{version}.tar.xz
BuildRequires:	binutils
BuildRequires:	dos2unix
BuildRequires:	util-linux

%description
Provides five binary edid files to give to support kernel edid loading feature


%prep
%setup -q -n %{name}

%build
export CC=gcc

%make 

%install
mkdir -p %{buildroot}/lib/firmware/edid
cp -avf *.bin %{buildroot}/lib/firmware/edid

%files
%defattr(0644,root,root,0755)
/lib/firmware/edid/*.bin
