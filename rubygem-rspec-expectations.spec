%define oname rspec-expectations

Name:       rubygem-%{oname}
Version:    2.8.0
Release:	2
Summary:    Behaviour Driven Development for Ruby
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/rspec/rspec-expectations
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
Requires:   rubygems
Requires:   rubygem(diff-lcs) >= 1.1.2
Requires:   rubygem(cucumber) >= 0.6.2
Requires:   rubygem(aruba) >= 0.1.1
Requires:   rubygem(rspec-core)
Requires:   rubygem(rspec-mocks)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
rspec expectations (should[_not] and matchers)


%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# remove vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
#%{ruby_gemdir}/gems/%{oname}-%{version}/.document
#%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
#%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
