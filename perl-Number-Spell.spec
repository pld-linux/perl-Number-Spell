#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Number
%define		pnam	Spell
Summary:	Number::Spell Perl module
Summary(cs.UTF-8):	Modul Number::Spell pro Perl
Summary(da.UTF-8):	Perlmodul Number::Spell
Summary(de.UTF-8):	Number::Spell Perl Modul
Summary(es.UTF-8):	Módulo de Perl Number::Spell
Summary(fr.UTF-8):	Module Perl Number::Spell
Summary(it.UTF-8):	Modulo di Perl Number::Spell
Summary(ja.UTF-8):	Number::Spell Perl モジュール
Summary(ko.UTF-8):	Number::Spell 펄 모줄
Summary(nb.UTF-8):	Perlmodul Number::Spell
Summary(pl.UTF-8):	Moduł Perla Number::Spell
Summary(pt.UTF-8):	Módulo de Perl Number::Spell
Summary(pt_BR.UTF-8):	Módulo Perl Number::Spell
Summary(ru.UTF-8):	Модуль для Perl Number::Spell
Summary(sv.UTF-8):	Number::Spell Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Number::Spell
Summary(zh_CN.UTF-8):	Number::Spell Perl 模块
Name:		perl-Number-Spell
Version:	0.04
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e30521cc7ff7677428794f46aaa37a57
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers.
Currently only integers are supported.

%description -l pl.UTF-8
Ten moduł daje możliwość zapisu słownego liczb. Na razie obsługuje
tylko liczby całkowite.

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
%doc Changes
%{perl_vendorlib}/Number/Spell.pm
%dir %{perl_vendorlib}/auto/Number
%dir %{perl_vendorlib}/auto/Number/Spell
%{perl_vendorlib}/auto/Number/Spell/autosplit.ix
%{_mandir}/man3/*
