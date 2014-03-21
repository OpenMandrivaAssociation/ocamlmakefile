Summary:	Automated compilation of complex OCaml-projects
Name:		ocamlmakefile
Version:	6.37.0
Release:	1
License:	LGPLv2.1+ with OCaml linking exception
Group:		Development/Other
Url:		https://bitbucket.org/mmottl/ocaml-makefile
Source0:	https://bitbucket.org/mmottl/ocaml-makefile/downloads/ocaml-makefile-%{version}.tar.gz
Source1:	README.examples.idl
BuildArch:	noarch

%description
A general makefile for the Objective Caml programming language
OCamlMakefile is a general makefile which allows a programmer to
create quickly customized makefiles for a project written in the
Objective Caml programming language. Typically, a customized makefile
consists of the definition of a few variables, and an inclusion of
the general makefile provided by this package.

%files
%doc COPYING.txt README.md CHANGES.txt
%dir %{_datadir}/ocamlmakefile
%{_datadir}/ocamlmakefile/OCamlMakefile

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation and examples files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description doc
The %{name}-doc package contains documentation and examples files for
developing applications that use %{name}.

%files doc
%doc calc camlp4 gtk idl threads

#----------------------------------------------------------------------------

%prep
%setup -q -n ocaml-makefile-%{version}
install -m 0644 %{SOURCE1} ./

%build

%install
# OCamlMakefile
install -d -m 0755 %{buildroot}%{_datadir}/ocamlmakefile
sed -i -e "s|/usr/local/lib|/usr/lib|g" OCamlMakefile
install -m 0644 OCamlMakefile %{buildroot}%{_datadir}/ocamlmakefile/

# examples/
for d in calc camlp4 gtk idl threads; do
  sed -i -e "s|../OCamlMakefile|%{_datadir}/ocamlmakefile/OCamlMakefile|g" ./$d/Makefile;
done
cp ./README.examples.idl ./calc/README
cp ./README.examples.idl ./idl/README

