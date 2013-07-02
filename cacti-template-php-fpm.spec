%define		template	php-fpm
%include	/usr/lib/rpm/macros.perl
Summary:	PHP-FPM Status template for Cacti
Name:		cacti-template-%{template}
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/cacti-template-php-fpm/archive/%{version}.tar.gz
# Source0-md5:	5af0510dd8fcd917226c31aed2d14afc
URL:		https://github.com/glensc/cacti-template-php-fpm
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
mv cacti-template-php-fpm-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p get_php_fpm_status.pl $RPM_BUILD_ROOT%{scriptsdir}
cp -p cacti_graph_template_php-fpm_statistic.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_graph_template_php-fpm_statistic.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{scriptsdir}/get_php_fpm_status.pl
%{resourcedir}/*.xml
