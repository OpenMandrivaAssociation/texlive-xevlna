# revision 30086
# category Package
# catalog-ctan /macros/xetex/generic/xevlna
# catalog-date 2013-04-23 11:12:19 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-xevlna
Version:	1.0
Release:	3
Summary:	Insert non-breakable spaces using XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/xevlna
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xevlna.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
