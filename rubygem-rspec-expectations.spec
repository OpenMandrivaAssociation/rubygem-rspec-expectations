%define oname rspec-expectations

Name:       rubygem-%{oname}
Version:    2.6.0
Release:    %mkrel 3
Summary:    Behaviour Driven Development for Ruby
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/rspec/rspec-expectations
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(diff-lcs) >= 1.1.2
Requires:   rubygem(cucumber) >= 0.6.2
Requires:   rubygem(aruba) >= 0.1.1
Requires:   rubygem(rspec-core)
Requires:   rubygem(rspec-mocks)
BuildRequires: rubygems
BuildRequires: ruby-rdoc
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
rspec expectations (should[_not] and matchers)


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# remove vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/Guardfile
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/specs.watchr
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
