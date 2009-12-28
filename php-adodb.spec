Summary:	Active Data Objects Data Base (ADOdb)
Name:		php-adodb
Version:	5.10
Release:	%mkrel 1
License:	BSD
Group:		Development/PHP
URL:		http://adodb.sourceforge.net/
Source0:	http://downloads.sourceforge.net/adodb/adodb510.tgz
BuildArch:	noarch
Epoch:		2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP is a wonderful language for building dynamic web pages. Unfortunately,
PHP's database access functions are not standardised. Every database
extension uses a different and incompatibile API. This creates a need for a
database class library to hide the differences between the different databases
(encapsulate the differences) so we can easily switch databases. 

%prep
%setup -q -n adodb5

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/www/icons
install -d %{buildroot}%{_datadir}/php/adodb
cp -aRf * %{buildroot}%{_datadir}/php/adodb

install -m644 cute_icons_for_site/* %{buildroot}/var/www/icons/

# cleanup
rm -rf %{buildroot}%{_datadir}/php/adodb/cute_icons_for_site
rm -rf %{buildroot}%{_datadir}/php/adodb/docs
rm -f %{buildroot}%{_datadir}/php/adodb/*.txt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt docs/*
%{_datadir}/php/adodb
/var/www/icons/*
