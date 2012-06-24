%include	/usr/lib/rpm/macros.perl
%define		pdir	Number
%define		pnam	Spell
Summary:	Number::Spell Perl module
Summary(cs):	Modul Number::Spell pro Perl
Summary(da):	Perlmodul Number::Spell
Summary(de):	Number::Spell Perl Modul
Summary(es):	M�dulo de Perl Number::Spell
Summary(fr):	Module Perl Number::Spell
Summary(it):	Modulo di Perl Number::Spell
Summary(ja):	Number::Spell Perl �⥸�塼��
Summary(ko):	Number::Spell �� ����
Summary(no):	Perlmodul Number::Spell
Summary(pl):	Modu� Perla Number::Spell
Summary(pt):	M�dulo de Perl Number::Spell
Summary(pt_BR):	M�dulo Perl Number::Spell
Summary(ru):	������ ��� Perl Number::Spell
Summary(sv):	Number::Spell Perlmodul
Summary(uk):	������ ��� Perl Number::Spell
Summary(zh_CN):	Number::Spell Perl ģ��
Name:		perl-Number-Spell
Version:	0.04
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers.
Currently only integers are supported.

%description -l pl
Ten modu� daje mo�liwo�� zapisu s�ownego liczb. Na razie obs�uguje
tylko liczby ca�kowite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%{perl_sitelib}/Number/Spell.pm
%dir %{perl_sitelib}/auto/Number
%dir %{perl_sitelib}/auto/Number/Spell
%{perl_sitelib}/auto/Number/Spell/autosplit.ix
%{_mandir}/man3/*
