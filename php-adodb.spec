Summary:	Active Data Objects Data Base (ADOdb)
Name:		php-adodb
Version:	5.16a
Release:	%mkrel 1
License:	BSD
Group:		Development/PHP
URL:		http://adodb.sourceforge.net/
Source0:	http://downloads.sourceforge.net/adodb/adodb516a.zip
BuildRequires:	unzip
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


%changelog
* Tue Apr 10 2012 Oden Eriksson <oeriksson@mandriva.com> 2:5.16a-1mdv2012.0
+ Revision: 790133
- 5.16a

* Sun Aug 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2:5.12-1
+ Revision: 694460
- 5.12

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2:5.11-2
+ Revision: 679252
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2:5.11-1mdv2011.0
+ Revision: 602335
- 5.11

* Mon Dec 28 2009 Oden Eriksson <oeriksson@mandriva.com> 2:5.10-1mdv2010.1
+ Revision: 482988
- 5.10

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 2:5.09a-2mdv2010.0
+ Revision: 397258
- Rebuild

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2:5.09a-1mdv2010.0
+ Revision: 397150
- new version
- install under %%{_datadir}/php, so as to be in php include_path directly
- spec cleanup

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2:5.05-2mdv2009.1
+ Revision: 321698
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2:5.05-1mdv2009.0
+ Revision: 239115
- 5.05

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 2:4.95-1mdv2008.0
+ Revision: 81132
- 4.95

* Fri Aug 31 2007 Helio Chissini de Castro <helio@mandriva.com> 1:5.01-1mdv2008.0
+ Revision: 76441
- New upstream version

* Wed Jul 25 2007 Funda Wang <fwang@mandriva.org> 1:4.95a-1mdv2008.0
+ Revision: 55434
- New version


* Mon Aug 21 2006 Oden Eriksson <oeriksson@mandriva.com> 1:4.91-1mdv2007.0
- 4.91

* Fri May 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1:4.81-1mdk
- 4.81 (Minor bugfixes)

* Wed Mar 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1:4.80-1mdk
- 4.80 (Minor bugfixes)

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1:4.68-1mdk
- 4.68

* Tue Jul 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.64-2mdk 
- used %%mkrel

* Wed Jun 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.64-1mdk 
- new version
- introduce epoch
- rpmbuildupate aware
- renamed to php-adodb
- install in /usr/share/php-adodb
- don't skip rpm automatic dependencies computing
- use perl instead of dos2unix to fix encodings

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 4.54-1mdk
- rename the package (ADOdb/adodb)
- new url
- move to /usr/share/adodb
- fix file permissions and anti ^M's

* Thu Nov 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.54-1mdk
- 4.54
- use rpm magic to speed up the build

* Wed May 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.22-1mdk
- 4.22

* Wed May 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.00-2mdk
- fix deps

* Tue Oct 21 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.00-1mdk
- 4.00

* Fri Aug 22 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.72-1mdk
- 3.72

