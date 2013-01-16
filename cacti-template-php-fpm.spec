%define		template	php-fpm
%include	/usr/lib/rpm/macros.perl
Summary:	PHP-FPM Status template for Cacti
Name:		cacti-template-%{template}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/download/file.php?id=24260&/cacti-php-fpm.tar.gz
# Source0-md5:	c1bf81122c4dbbe84391cf24f855c049
URL:		http://forums.cacti.net/viewtopic.php?f=12&t=41580
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
PHP-FPM Status template for Cacti.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p cacti_check_php-fpm.pl $RPM_BUILD_ROOT%{scriptsdir}
cp -p cacti_graph_template_php-fpm_fastcgi_stats.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_graph_template_php-fpm_fastcgi_stats.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{scriptsdir}/cacti_check_php-fpm.pl
%{resourcedir}/*.xml
