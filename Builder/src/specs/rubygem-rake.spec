%global realversion 10.1.1
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname rubygem-rake

%global gemname rake

%global gemdir /usr/lib64/ruby/gems/1.8
%global geminstdir %{gemdir}/gems/%{gemname}-%{realversion}
%global gemspecdir %{gemdir}/specifications/
%global gemcachedir %{gemdir}/cache/

%global rubyabi 1.8

Summary: a modular Ruby webserver interface
Name: EXTRlitprake_CXP9031045
Version: %{rpmversion}
Release: 1
Group: Development/Languages
License: MIT
URL: http://www.ericsson.com/
Source0: %{gemname}-%{realversion}.tar.gz
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{realversion}
Provides: rubygem-%{gemname} = %{realversion}
Packager:  %{packager}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.
repackaged by Ericsson from GitHUB source code.


%prep
%setup -q -c -T
mkdir -p .%{gemdir}

%build

%install
%{__install} -d -m0755 %{buildroot}%{geminstdir}
%{__install} -d -m0755 %{buildroot}/usr/bin
%{__install} -d -m0755 %{buildroot}%{gemspecdir}
%{__install} -d -m0755 %{buildroot}%{gemcachedir}
cp -a  %{_builddir}%{gemname}-%{gemname}-%{realversion}/* %{buildroot}%{geminstdir}
cp -a  %{_builddir}%{gemname}-%{gemname}-%{realversion}/bin/rake %{buildroot}/usr/bin/rake
cp -a  %{_builddir}%{gemname}-%{realversion}.gem %{buildroot}%{gemcachedir}%{gemname}-%{realversion}.gem
cp -a  %{_builddir}%{gemname}-%{realversion}.gemspec %{buildroot}%{gemspecdir}%{gemname}-%{realversion}.gemspec

%files
%defattr(-,root,root,-)
%{geminstdir}
%{gemspecdir}
%{gemcachedir}
/usr/bin/rake
