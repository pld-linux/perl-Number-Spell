%include	/usr/lib/rpm/macros.perl

%define		pdir	Number
%define		pnam	Spell

Summary:	Number-Spell perl module
Summary(pl):	Modu³ perla Number-Spell
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers.
Currently only integers are supported.

%description -l pl
Ten modu³ daje mo¿liwo¶æ zapisu s³ownego liczb. Na razie obs³uguje
tylko liczby ca³kowite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Number/Spell.pm
%{_mandir}/man3/*
