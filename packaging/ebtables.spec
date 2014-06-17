Summary:        Ethernet Bridge frame table administration tool
Name:           ebtables
Version:        2.0.10
Release:        4
License:        GPL-2.0+
Group:          Security/Network
URL:            http://ebtables.sf.net/
Source:         http://downloads.sf.net/ebtables/%{name}-v%{version}.tar.gz

# Gbp-Ignore-Patches: 0 1
Patch0:         no-root-install.patch
Patch1:         no-as-needed.patch

%description
Ethernet bridge tables is a firewalling tool to transparantly filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no incompatibility issues.

%prep
%setup -q -n %{name}-v%{version}

# Gbp-Patch-Macros
%patch0 -p1
%patch1 -p1

%build
make \
    %{?_smp_mflags} \
    CFLAGS="${RPM_OPT_FLAGS}" \
    LIBDIR="%{_libdir}/ebtables" \
    BINDIR="/sbin" \
    LDFLAGS="${RPM_LD_FLAGS} -Wl,-z,now"

%install
make \
    DESTDIR="%{buildroot}" \
    LIBDIR="%{_libdir}/ebtables" \
    BINDIR="/sbin" \
    install

rm -rf %{buildroot}/etc/rc.d/init.d/ebtables
rm -rf %{buildroot}/usr/local/man/man8/ebtables.8

%files
%defattr(-,root,root)
%doc COPYING
%config(noreplace) %{_sysconfdir}/ethertypes
%config(noreplace) %{_sysconfdir}/sysconfig/ebtables-config
%{_libdir}/ebtables/*.so
/sbin/ebtables*

