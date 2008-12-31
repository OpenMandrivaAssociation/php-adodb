Summary:	Active Data Objects Data Base (ADOdb)
Name:		php-adodb
Version:	5.05
Release:	%mkrel 2
License:	BSD
Group:		Development/PHP
URL:		http://adodb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/adodb/adodb505.tgz
BuildArch:	noarch
Epoch:		2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP is a wonderful language for building dynamic web pages. Unfortunately,
PHP's database access functions are not standardised. Every database
extension uses a different and incompatibile API. This creates a need for a
database class library to hide the differences between the different databases
(encapsulate the differences) so we can easily switch databases. 

%prep

%setup -q -n adodb5

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
rm -rf %{buildroot}

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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt docs/*
%{_datadir}/%{name}
/var/www/icons/*
