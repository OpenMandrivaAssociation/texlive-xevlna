%global tl_name xevlna
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Insert non-breakable spaces using XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/xevlna
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will directly insert nonbreakable spaces (in Czech, vlna or
vlnka), after nonsyllabic prepositions and single letter conjunctions,
while the document is being typeset. (The macros recognised maths and
verbatim by TeX means.) (Inserting nonbreakable spaces by a preprocessor
will probably never be fully reliable, because user defined macros and
environments cannot reliably be recognised.) The package works both with
(Plain) XeTeX and with XeLaTeX.

