Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki-recognize
Version: 	0.3.1.2
Release: 	2
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/%{name}-%version.tar.gz
URL: 		https://www.tegaki.org
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-setuptools
Requires:	tegaki-gui >= 0.3.1
BuildArch:	noarch

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -qn %{name}-%version
sed -i -e 's#Exec=.*#Exec=tegaki-recognize#' tegaki-recognize.desktop.in

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}%{_prefix}

rm -f %{buildroot}%{_datadir}/menu/tegaki-recognize

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{py_puresitedir}/tegaki*
%{_bindir}/tegaki-recognize
%{_datadir}/applications/tegaki-recognize.desktop
%{_datadir}/pixmaps/tegaki-recognize.svg


%changelog
* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.3.1.2-1mdv2011.0
+ Revision: 592301
- import tegaki-recognize

