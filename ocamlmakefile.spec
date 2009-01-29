Name:           ocamlmakefile
Version:        6.29.1
Release:        %mkrel 1
Summary:        Automated compilation of complex OCaml-projects
License:        LGPL
Group:          Development/Other
URL:            http://www.ocaml.info/home/ocaml_sources.html#ocaml-make
Source0:        http://hg.ocaml.info/release/ocaml-make/archive/ocaml-make-release-%{version}.tar.bz2
Source1:        SOURCES/README.examples.idl
# curl http://hg.ocaml.info/release/ocaml-make/archive/release-%{version}.tar.bz2 > ocaml-make-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A general makefile for the Objective Caml programming language
OCamlMakefile is a general makefile which allows a programmer to
create quickly customized makefiles for a project written in the
Objective Caml programming language. Typically, a customized makefile
consists of the definition of a few variables, and an inclusion of
the general makefile provided by this package.

%package        doc
Summary:        Documentation and examples files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation and examples files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-make-release-%{version}
install -m 0644 %{SOURCE1} ./

%build

%install
rm -rf %{buildroot}

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


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.txt Changes
%dir %{_datadir}/ocamlmakefile
%{_datadir}/ocamlmakefile/OCamlMakefile

%files doc
%defattr(-,root,root)
%doc calc camlp4 gtk idl threads

