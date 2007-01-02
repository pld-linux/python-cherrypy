%define 	fname	CherryPy
%define		module	cherrypy
#
Summary:	A pythonic, object-oriented web development framework
Summary(pl.UTF-8):   Pythonowy, zorientowany obiektowo szkielet do tworzenia WWW
Name:		python-%{module}
Version:	2.2.1
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/cherrypy/%{fname}-%{version}.tar.gz
# Source0-md5:	14bf17b0706bc480342cb8fcfaed74cd
Patch0:		%{name}-autoreload.patch
URL:		http://www.cherrypy.org
BuildRequires:	python >= 1:2.5
%pyrequires_eq	python-modules
Requires:	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CherryPy is a pythonic, object-oriented web development framework.

CherryPy allows developers to build web applications in much the same
way they would build any other object-oriented Python program. This
usually results in smaller source code developed in less time.

CherryPy is now more than three years old and it is has proven very
fast and stable. It is being used in production by many sites, from
the simplest ones to the most demanding ones.

Oh, and most importantly: CherryPy is fun to work with :-)

%description -l pl.UTF-8
CherryPy to pythonowy, obiektowo zorientowany szkielet do tworzenia
WWW.

CherryPy pozwala programistom tworzyć aplikacje WWW w sposób bardzo
podobny do tworzenia każdego innego obiektowo zorientowanego programu
w Pythonie. Wynikiem tego jest zwykle mniejszy kod źródłowy stworzony
w krótszym czasie.

CherryPy ma już nieco ponad trzy lata i okazał się być bardzo szybki i
stabilny. Jest używany produkcyjnie przez wiele serwisów, od
najprostszych do bardziej wymagających.

I najważniejsze - praca z CherryPy jest zabawą :-)

%package examples
Summary:	Example files for CherryPy
Summary(pl.UTF-8):   Pliki przykładów dla CherryPy
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for CherryPy.

%description examples -l pl.UTF-8
Pliki przykładów dla CherryPy.

%prep
%setup -q -n %{fname}-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tutorial

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/ -name \*.py | xargs rm -f

cp -r cherrypy/tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt CHERRYPYTEAM.txt README.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/CherryPy*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
