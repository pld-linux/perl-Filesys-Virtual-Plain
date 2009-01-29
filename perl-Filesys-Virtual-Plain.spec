#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	Virtual-Plain
Summary:	Filesys::Virtual::Plain - A Plain virtual filesystem
Summary(pl.UTF-8):	Filesys::Virtual::Plain - prosty wirtualny system plików
Name:		perl-Filesys-Virtual-Plain
Version:	0.10
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	620f9a6e318ecf143cbcd9df0ea6eb29
URL:		http://search.cpan.org/dist/Filesys-Virtual-Plain/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Filesys-Virtual
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses Filesys::Virtual to implement plain filesystem. See
code for more info.

%description -l pl.UTF-8
Ten moduł wykorzystuje Filesys::Virtual do zaimplementowania prostego
systemu plików. Więcej informacji w kodzie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Filesys/Virtual/Plain.pm
%{_mandir}/man3/*
