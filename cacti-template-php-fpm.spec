%define		template	php-fpm
Summary:	PHP-FPM Pool Status template for Cacti
Name:		cacti-template-%{template}
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/cacti-template-php-fpm/archive/%{version}/%{template}-%{version}.tar.gz
# Source0-md5:	d3f32f5e2fccb4169901a73f54ba20cc
URL:		https://github.com/glensc/cacti-template-php-fpm
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	cacti >= 0.8.8a
Suggests:	perl-FCGI-Client
Suggests:	perl-Moose
Suggests:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
PHP-FPM Pool Status template for Cacti.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p get_php_fpm_status.pl $RPM_BUILD_ROOT%{scriptsdir}
cp -p cacti_graph_template_php-fpm_pool_status.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_graph_template_php-fpm_pool_status.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{scriptsdir}/get_php_fpm_status.pl
%{resourcedir}/*.xml
