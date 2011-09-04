%define fontname liberation
%define archivename %{name}-%{version}
%define common_desc \
The Liberation Fonts are intended to be replacements for the three most \
commonly used fonts on Microsoft systems: Times New Roman, Arial, and Courier \
New.

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:             %{fontname}-fonts
Summary:          Fonts to replace commonly used Microsoft Windows fonts
Version:          1.05.1.20090721
Release:          4%{?dist}
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:          Liberation
Group:            User Interface/X
URL:              https://fedorahosted.org/liberation-fonts/
Source0:          https://fedorahosted.org/releases/l/i/liberation-fonts/%{name}-%{version}.tar.gz

BuildRoot:        %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils
BuildRequires:    fontforge >= 20090408

%description
%common_desc

Meta-package of Liberation fonts which installs Sans, Serif, and Monospace
families.

%package -n %{fontname}-fonts-common
Summary:          Shared common files of Liberation font families
Group:            User Interface/X
Requires:         fontpackages-filesystem >= 1.13
Obsoletes:        liberation-fonts < 1.04.93-7
Obsoletes:        liberation-fonts-compat <= 1.05.1.20090630

%description -n %{fontname}-fonts-common
%common_desc

Shared common files of Liberation font families.

%files -n %{fontname}-fonts-common
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING License.txt README
%dir %{_fontdir}
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}

%package -n %{fontname}-sans-fonts
Summary:      Sans-serif fonts to replace commonly used Microsoft Arial
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This is Sans-serif TrueType fonts that replaced commonly used Microsoft Arial.

%_font_pkg -n sans LiberationSans-*.ttf

%package -n %{fontname}-serif-fonts
Summary:      Serif fonts to replace commonly used Microsoft Times New Roman
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This is Serif TrueType fonts that replaced commonly used Microsoft Times New \
Roman.

%_font_pkg -n serif LiberationSerif-*.ttf

%package -n %{fontname}-mono-fonts
Summary:      Monospace fonts to replace commonly used Microsoft Courier New
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}

%description -n %{fontname}-mono-fonts
%common_desc

This is Monospace TrueType fonts that replaced commonly used Microsoft Courier \
New.

%_font_pkg -n mono LiberationMono-*.ttf

%prep
%setup -q -n %{name}-%{version}

%build
%__make build

%install
%__rm -rf %{buildroot}
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
%__ln_s %{_fontdir} %{buildroot}%{catalogue}/%{name}
# fonts.{dir,scale}
mkfontdir %{buildroot}%{_fontdir}
mkfontscale %{buildroot}%{_fontdir}

%clean
%__rm -rf %{buildroot}

%changelog
* Wed Jan 13 2010 Caius 'kaio' Chance <cchance@redhat.com> - 1.05.1.20090721-4
- Resolves: rhbz#554913
- Fixed macro typo.

* Wed Jan 13 2010 Caius 'kaio' Chance <cchance@redhat.com> - 1.05.1.20090721-3
- Resolves: rhbz#554913
- Fixed rpmlint errors.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.05.1.20090721-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05.1.20090721-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Caius 'kaio' Chance <k at kaio.me> - 1.05.1.20090721-1.fc12
- Fixed fontforge scripting of sfd -> ttf generation.
- Checked existance of traditionat kern table in Sans and Serif.

* Tue Jul 14 2009 Caius 'kaio' Chance <k at kaio.me> - 1.05.1.20090713-2.fc12
- Required fontforge ver 20090408 which supports generation with traditional
  kern table. (rhbz#503430)

* Mon Jul 13 2009 Caius 'kaio' Chance <k at kaio.me> - 1.05.1.20090713-1.fc12
- Updated to upstream 1.05.1.20090713.
- Generate TTFs with traditional kern table via fontforge scripts. (rh#503430)

* Mon Jul 06 2009 Caius 'kaio' Chance <k at kaio.me> - 1.05.1.20090706-1.fc12
- Updated to upstream 1.05.1.20090706.
- Reconverted from original TTF with traditional kern table. (rh#503430)

* Tue Jun 30 2009 Caius 'kaio' Chance <k at kaio.me> - 1.05.1.20090630-1.fc12
- Updated to upstream 1.05.1.20090630.
- Reconverted from original TTF with better procedures of data conservation.

* Tue May 19 2009 Jens Petersen <petersen@redhat.com> - 1.04.93-11
- remove redundant obsoletes, provides and conflicts from new subpackages

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Caius Chance <cchance@redhat.com> - 1.04.93-9.fc11
- Fixed inter-subpackage dependencies with reference of dejavu.

* Wed Feb 04 2009 Caius Chance <cchance@redhat.com> - 1.04.93-8.fc11
- Fixed inter-subpackage dependencies.

* Wed Feb 04 2009 Caius Chance <cchance@redhat.com> - 1.04.93-7.fc11
- Create -compat subpackage as meta-package for installing all font families.

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 1.04.93-6.fc11
- Fix busted inter-subpackage dependencies

* Tue Jan 20 2009 Caius Chance <cchance@redhat.com> - 1.04.93-5.fc11
- Resolved: rhbz#477410
- Refined .spec file based on Mailhot's review on rhbz.

* Mon Jan 19 2009 Caius Chance <cchance@redhat.com> - 1.04.93-4.fc11
- Resolves: thbz#477410
- Package renaming for post-1.13 fontpackages macros.

* Fri Jan 09 2009 Caius Chance <cchance@redhat.com> - 1.04.93-3.fc11
- Resolves: rhbz#477410 (Convert to new font packaging guidelines.)

* Tue Dec 09 2008 Caius Chance <cchance@redhat.com> - 1.04.93-2.fc11
- Resolves: rhbz#474522 (Cent sign is not coressed in Sans & Mono.)

* Wed Dec 03 2008 Caius Chance <cchance@redhat.com> - 1.04.93-1.fc11
- Resolves: rhbz#473481
  (Blurriness of Greek letter m (U+03BC) in Liberation Sans Regular.)

* Thu Jul 17 2008 Caius Chance <cchance@redhat.com> - 1.04.90-1.fc10
- Resolves: rhbz#258592
  (Incorrect glyph points and missing hinting instructions for U+0079, U+03BC,
   U+0431, U+2010..2012.)

* Thu Jul 17 2008 Caius Chance <cchance@redhat.com> - 1.04-1.fc10
- Resolves: rhbz#455717 (Update sources to version 1.04.)
- Improved .spec file.

* Thu Jun 12 2008 Caius Chance <cchance@redhat.com> - 1.04-0.1.beta2.fc10
- Updated source version to 1.04.beta2.
- Removed License.txt and COPYING as already included in sources.

* Thu Apr 10 2008 Caius Chance <cchance@redhat.com> - 1.03-1.fc9
- Resolves: rhbz#251890 (Exchanged and incomplete glyphs.)
- Repack source tarball and re-align source version number.

* Mon Mar 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.02-2
- correct license tag, license explanation added

* Tue Mar 25 2008 Caius Chance <cchance@redhat.com> - 1.02-1.fc9
- Resolves: rhbz#240525 (Alignment mismatch of dot accents.)

* Wed Jan 16 2008 Caius Chance <cchance@redhat.com> - 1.01-1.fc9
- Moved source tarball from cvs to separated storage.

* Mon Jan 14 2008 Caius Chance <cchance@redhat.com> - 1.0-1.fc9
- Resolves: rhbz#428596 (Liberation fonts need to be updated to latest font.)

* Wed Nov 28 2007 Caius Chance <cchance@redhat.com> - 0.2-4.fc9
- Resolves: rhbz#367791 (remove 59-liberation-fonts.conf)

* Wed Sep 12 2007 Jens Petersen <petersen@redhat.com> - 0.2-3.fc8
- add fontdir macro
- create fonts.dir and fonts.scale (reported by Mark Alford, #245961)
- add catalogue symlink

* Wed Sep 12 2007 Jens Petersen <petersen@redhat.com> - 0.2-2.fc8
- update license field to GPLv2

* Thu Jun 14 2007 Caius Chance <cchance@redhat.com> 0.2-1.fc8
- Updated new source tarball from upstream: '-3' (version 0.2).

* Tue May 15 2007 Matthias Clasen <mclasen@redhat.com> 0.1-9
- Bump revision

* Tue May 15 2007 Matthias Clasen <mclasen@redhat.com> 0.1-8
- Change the license tag to "GPL + font exception"

* Mon May 14 2007 Matthias Clasen <mclasen@redhat.com> 0.1-7
- Correct the source url

* Mon May 14 2007 Matthias Clasen <mclasen@redhat.com> 0.1-6
- Incorporate package review feedback

* Fri May 11 2007 Matthias Clasen <mclasen@redhat.com> 0.1-5
- Bring the package in sync with Fedora packaging standards

* Wed Apr 25 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-4
- Require fontconfig package for post and postun

* Tue Apr 24 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-3
- Bump version to fix issue in RHEL4 RHN

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-2rhis
- New license file

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-1rhis
- Inital packaging
