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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.8.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8.0-1
+ Revision: 767040
- version update 2.8.0

* Sat Sep 10 2011 Alexander Barakin <abarakin@mandriva.org> 2.6.0-3
+ Revision: 699181
- after bootstrap

* Fri Sep 09 2011 Andrey Smirnov <asmirnov@mandriva.org> 2.6.0-2
+ Revision: 699168
- bump release
- remove rspec-core from reqs

* Thu Sep 08 2011 Andrey Smirnov <asmirnov@mandriva.org> 2.6.0-1
+ Revision: 699030
- missing rdoc fix
- imported package rubygem-rspec-expectations

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 604553
- import rubygem-rspec-expectations

