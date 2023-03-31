Summary:	Generic monitor edid files
Name:		edidbins
Version:	1.1
Release:	8
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/torvalds/linux/tree/master/Documentation/EDID
BuildArch:	noarch
#The tarball for these files was generated from the cloned sources from the above url. The files were copied to a directory edidbins and then compressed with "tar -Jcvf kernel-edidbins edidbins/*" It is unlikely that these sources will change. Proprietary edid's should have their own package.
Source0:	kernel-edidbins-%{version}.tar.xz
BuildRequires:	dos2unix

%description
Provides five binary edid files to give to support kernel edid loading feature.

%prep
%autosetup -n %{name} -p1

#force gcc
sed -i 's/@cc/@gcc/' Makefile

%build

%make_build

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/edid
cp -avf *.bin %{buildroot}%{_prefix}/lib/firmware/edid

%files
%defattr(0644,root,root,0755)
%{_prefix}/lib/firmware/edid/*.bin
