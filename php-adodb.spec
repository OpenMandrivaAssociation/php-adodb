%define base_name	adodb
%define name		php-%{base_name}
%define	maj_ver		4
%define	min_ver		95a
%define version		%{maj_ver}.%{min_ver}
%define	src_ver		%{maj_ver}%{min_ver}

Summary:	Active Data Objects Data Base (ADOdb)
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Epoch:		1
License:	BSD
Group:		Development/Other
URL:		http://adodb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/adodb/%{base_name}%{src_ver}.tar.bz2
BuildArch:	noarch
Obsoletes:	ADOdb
Obsoletes:	%{base_name}
Provides:	ADOdb
Provides:	%{base_name}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP is a wonderful language for building dynamic web pages.
Unfortunately, PHP's database access functions are not
standardised. Every database extension uses a different and
incompatibile API. This creates a need for a database class
library to hide the differences between the different databases
(encapsulate the differences) so we can easily switch databases. 

%prep
%setup -q -n adodb

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

find . -name CVS -o -name .cvs\* -o -name .#\* | xargs rm -rf

# fix encoding
for file in `find . -type f`; do
    perl -pi -e 'BEGIN {exit unless -T $ARGV[0];} tr/\r//d;' $file
done

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}/var/www/icons
install -d %{buildroot}%{_datadir}/%{name}
cp -aRf * %{buildroot}%{_datadir}/%{name}

install -m644 cute_icons_for_site/* %{buildroot}/var/www/icons/

# cleanup
rm -rf %{buildroot}%{_datadir}/adodb/cute_icons_for_site
rm -rf %{buildroot}%{_datadir}/adodb/docs
rm -f %{buildroot}%{_datadir}/*.zip
rm -f %{buildroot}%{_datadir}/*.txt

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt docs/*
%{_datadir}/%{name}
/var/www/icons/*
