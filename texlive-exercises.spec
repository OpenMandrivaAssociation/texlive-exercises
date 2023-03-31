Name:		texlive-exercises
Version:	55188
Release:	2
Summary:	Typeset exercises and solutions with automatic addition of points
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exercises
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines the environments exercise and solution.
The layout of these environments can be customized. The --
optional -- points in the exercises can be added automatically.
The package also permits to hide the solutions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/exercises
%{_texmfdistdir}/tex/latex/exercises
%doc %{_texmfdistdir}/doc/latex/exercises

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
