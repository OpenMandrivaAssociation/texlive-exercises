%global tl_name exercises
%global tl_revision 55188

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset exercises and solutions with automatic addition of points
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exercises
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercises.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines the environments exercise and solution. The layout
of these environments can be customized. The -- optional -- points in
the exercises can be added automatically. The package also permits to
hide the solutions.

