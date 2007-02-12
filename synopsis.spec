Summary:	Synopsis - a source code introspection tool
Summary(pl.UTF-8):   Synopsis - narzędzie do badania kodu źródłowego
Name:		synopsis
Version:	0.8
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	http://synopsis.fresco.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	3001e54cf4af937c2fd7377a1debdbac
URL:		http://synopsis.fresco.org/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synopsis is a multi-language source code introspection tool that
provides a variety of representations for the parsed code to enable
further processing such as documentation extraction, reverse
engineering, and source-to-source translation.

Synopsis provides a framework of C++ and Python APIs to access
these representations and allows Processor objects to be defined
and composed into processing pipelines, making this framework very
flexible and extensible.

%description -l pl.UTF-8
Synopsis to narzędzie do badania kodu źródłowego w wielu językach
udostępniające wiele reprezentacji przeanalizowanego kodu, aby
umożliwić dalsze przetwarzanie takie jak tworzenie dokumentacji,
reverse engineering i tłumaczenie source-to-source.

Synopsis udostępnia szkielety API w C++ i Pythonie pozwalające na
dostęp do tych reprezentacji i umożliwiające definiowanie obiektów
Processor i umieszczanie ich w potokach przetwarzania, co czyni ten
szkielet bardzo elastycznym i rozszerzalnym.

%package devel
Summary:	Synopsis - header files
Summary(pl.UTF-8):   Synopsis - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Synopsis - header files.

%description devel -l pl.UTF-8
Synopsis - pliki nagłówkowe.

%prep
%setup -q

%build
CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcxxflags}"
export CC CXX CFLAGS CXXFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README share/doc/Synopsis/html/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libSynopsis.so
%{py_sitedir}/Synopsis

%files devel
%defattr(644,root,root,755)
%{_includedir}/Synopsis
%{_pkgconfigdir}/*.pc
