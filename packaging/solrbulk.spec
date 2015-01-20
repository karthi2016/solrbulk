Summary:    Fast parallel bulk loading utility for SOLR.
Name:       solrbulk
Version:    0.1.3
Release:    0
License:    MIT
BuildArch:  x86_64
BuildRoot:  %{_tmppath}/%{name}-build
Group:      System/Base
Vendor:     Leipzig University Library <http://ub.uni-leipzig.de>
URL:        https://github.com/miku/solrbulk

%description

Fast parallel bulk loading utility for SOLR.

%prep
# the set up macro unpacks the source bundle and changes in to the represented by
# %{name} which in this case would be my_maintenance_scripts. So your source bundle
# needs to have a top level directory inside called my_maintenance _scripts
# %setup -n %{name}

%build
# this section is empty for this example as we're not actually building anything

%install
# create directories where the files will be located
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin

# put the files in to the relevant directories.
# the argument on -m is the permissions expressed as octal. (See chmod man page for details.)
install -m 755 solrbulk $RPM_BUILD_ROOT/usr/local/sbin
install -m 755 solrbulk-tune $RPM_BUILD_ROOT/usr/local/sbin

%post
# the post section is where you can run commands after the rpm is installed.
# insserv /etc/init.d/my_maintenance

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

# list files owned by the package here
%files
%defattr(-,root,root)
/usr/local/sbin/solrbulk
/usr/local/sbin/solrbulk-tune


%changelog
* Tue Jan 20 2015 Martin Czygan
- 0.1.2 release
- added solrbulk-tune, an experimental parameter optimizing script

* Mon Jan 19 2015 Martin Czygan
- 0.1.1 release
