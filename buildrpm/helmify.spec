
%global debug_package %{nil}
Name:           helmify
Version:        0.4.20
Release:        1%{?dist}
Summary:        Create Helm charts from Kubernetes YAML
License:        MIT
URL:            https://github.com/arttor/helmify
Source0:        %{name}-%{version}.tar.bz2

%description
Helmify creates a Helm chart from Kubernetes YAML resources.

%prep
%setup -q

%build
go build -o helmify ./cmd/helmify

%install
install -Dpm 0755 helmify %{buildroot}%{_bindir}/helmify

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
%{_bindir}/helmify

%changelog
* Tue Nov 17 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 0.4.20-1
- Add RPM packaging for helmify
