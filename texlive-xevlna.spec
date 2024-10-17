Name:		texlive-xevlna
Version:	43864
Release:	2
Summary:	Insert non-breakable spaces using XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/xevlna
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will directly insert nonbreakable spaces (in Czech,
vlna or vlnka), after nonsyllabic prepositions and single
letter conjuctions, while the document is being typeset. (The
macros recognised maths and verbatim by TeX means.) (Inserting
nonbreakable spaces by a preprocessor will probably never be
fully reliable, because user defined macros and environments
cannot reliably be recognised.) The package works both with
(Plain) XeTeX and with XeLaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xevlna/xevlna.sty
%doc %{_texmfdistdir}/doc/xelatex/xevlna/License.txt
%doc %{_texmfdistdir}/doc/xelatex/xevlna/README
%doc %{_texmfdistdir}/doc/xelatex/xevlna/xevlna-inc.tex
%doc %{_texmfdistdir}/doc/xelatex/xevlna/xevlna.pdf
%doc %{_texmfdistdir}/doc/xelatex/xevlna/xevlna.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
