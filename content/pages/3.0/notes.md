Title: Nuvola Player 3.0 Release Notes
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.0.0 was released on December 30th, 2015. It is the first release of the
    third generation of a runtime for web-based music streaming services that provides more native
    user experience and integration with Linux desktop environments than usual web browsers can offer.
    Nuvola Players handles multimedia keys, shows desktop notifications, integrates with various
    sound indicators, media player applets, GNOME lock screen and launchers and more.


**Nuvola Player 3.0.0** was released on December 30th, 2015 and the latest
[maintenance release **3.0.10**](#maintenance) was released on September 1st, 2017.
Continue reading these release notes,
[explore all features](:3.0/explore.html) or just [jump to installation instructions](:3.0/install.html).

About Nuvola Player
===================

**Nuvola Player** is a runtime for web-based music streaming services providing more native user
experience and integration with Linux desktop environments than usual web browsers can offer.
It tries to feel and look like a native application as possible. However, it cannot overcome common
drawbacks of web-based music streaming: some music streaming services require Flash plugin and web
apps usually have higher memory usage than native apps.

What's New {: #news}
==========

Nuvola Player 3 has been rewritten from scratch and contains plenty of improvements over Nuvola
Player 2.

No Hacks for Flash Support
--------------------------

Nuvola Player 2 uses graphical toolkit GTK+ version 3 for its user interface, while Adobe Flash,
Gnash and Lightspark use GTK+ version 2. The old GTK+ 2 and the new GTK+ 3 are not compatible,
so they cannot live in the same process. The problem is that the first generation WebKitGtk+ web
rendering engine used in Nuvola Player 2 runs plugins in the same process as the rest of the user
interface, so GTK+ 2 based Flash plugins cannot be loaded without conflicts with GTK+ 3.

**Nuvola Player 2 has to employ an ugly hack to support Flash**: run the Flash plugin in its own
non-conflicting process via nspluginwrapper. However, this approach has several disadvantages:

  * nspluginwrapper only supports only 32bit Flash plugin. As a result, you have to install hundreds
    of 32bit libraries on you 64bit system to be able to run 32bit Flash plugin. Yes, this is
    insane.

  * Memory usage is higher and performance is lower.

  * Wrapped Flash plugin is less stable, it often crashes and takes down whole Nuvola Player
    2 application.

**Nuvola Player 3 doesn't need any hacks to support Flash plugin**, because it is built on top of
WebKit2Gtk+, the second generation of this web rendering library.
The major diference is that plugins are run in a separate GTK+ 2 compatible process, so there is no
need to use nspluginwrapper and install 32bit libraries on 64bit system. There is also one extra
benefit: If Flash plugin crashes, it doesn't take down whole Nuvola Player application.

 Gallery
+[Nuvola Player 2 requires a plenty of 32bit libraries on 64bit system because of Flash plugin compatibility hack.](images/3.0/new/nuvola_player_2_flash_deps.png|256x192)
+[Nuvola Player 3 doesn't suffer from Flash plugin incompatibility issue.](images/3.0/new/nuvola_player_3_flash_deps.png|256x192)

Independent Instances
--------------------------

It was possible to have only one instance of **Nuvola Player 2** shared by all streaming services
and switch between them. In **Nuvola Player 3**, it's possible to run multiple services side-by-side
([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1007185)).
The services selector launches new instance for each service and creates a desktop application
shortcut ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1211351))
when a particular service starts. As a result, you can than pin it to the Unity Launcher or
GNOME Activities dock and launch it directly in the future.

 Gallery
+[Multiple services pinned to Unity Launcher.](images/3.0/unity/unity_launcher_multiple_pinned.png|256x192)
+[Multiple services pinned to GNOME Activities dock.](images/3.0/gnome/gnome_many_favorites.png|256x192)

Tiliado Repository
--------------------------

While Nuvola Player 2 repository provided packages only for Ubuntu and Debian, Nuvola Player 3
brings official support and packages also for Fedora. However, the Fedora packages may be
discontinued if there isn't enough financial support from Fedora users to justify existence of these
packages.

As I have received many complains that installation of Nuvola Player 2 was not easy enough for less
experienced users, I've created a graphical installer specially designed for them. However, power
users can of course still add Nuvola Player repository to software sources manually using terminal
kung-fu. The graphical installer is pretty handy though and I always use it when I test Nuvola
Player in clean systems in VirtualBox ;-)

Since I dislike the short nine-month support window of interim Ubuntu releases and their consecutive
removal from Launchpad build machines, I decided to abandon Launchpad and host APT repository on my
server like I did so with the repository for Debian. A side benefit is that packages won't get stuck
in Launchpad build queue. In addition, RPM packages for Fedora are also hosted on this server, all
in one place.

New Codebase
--------------------------

Since Nuvola Player 3 codebase was written from scratch, it doesn't have to carry a huge bag of backward
compatibility, which limited improvements in Nuvola Player 2, and it's easier to use new technologies.
Consequently, Nuvola Player 3 uses header bar with client side decorations and App Menu in GNOME,
but classic window decorations and global menu bar in Unity. Also, JavaScript API for service integration
scripts has been reworked to be more flexible.

Other changes
--------------------------

  * Added manager of keyboard shortcuts
    ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1294082)) and added support
    for **global keyboard shortcuts**
    ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1200911)). You can,
    for example, define a keyboard shortcut to show currently playing track in notification
    ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1207926))
  * Menu bar has been replaced with **header bar** (with client-side decorations in GNOME).
  * **Command line interface** has been reworked. See ``nuvolaplayer3ctl --help``. It is no possible to
    invoke toggle and radio actions (e.g. thumbs up/down, star rating;
    [feature request](https://bugs.launchpad.net/nuvola-player/+bug/1084145))
  * Unity Quick list integration was enhanced to show state of toggle actions (e.g. thumbs up/down,
    [feature request](https://bugs.launchpad.net/nuvola-player/+bug/1081077)) and radio actions
    (e.g. star rating)
  * Queue page of Google Play Music is not used as a start-up page
    ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1306678))


Streaming Services
==================

On February 22th 2016, Nuvola Player 3 shipped with 19 music streaming services.
See [Nuvola Player hompage](https://tiliado.eu/nuvolaplayer/) for more up-to-date list.

 * [8tracks 5.2](https://github.com/tiliado/nuvola-app-8tracks)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Amazon Cloud Player 5.3](https://github.com/tiliado/nuvola-app-amazon-cloud-player)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Bandcamp 2.2](https://github.com/tiliado/nuvola-app-bandcamp)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Deezer 2.5](https://github.com/tiliado/nuvola-app-deezer)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Google Calendar 1.2](https://github.com/tiliado/nuvola-app-google-calendar)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Google Play Music 5.18](https://github.com/tiliado/nuvola-app-google-play-music)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [Groove 1.3](https://github.com/tiliado/nuvola-app-groove)
   maintained by [Joel Cumberland](https://github.com/jrosco)
 * [Jango 2.3](https://github.com/tiliado/nuvola-app-jango)
   maintained by [Stefano Bagnatica](https://github.com/thepisu)
 * [KEXP Live Stream 1.2](https://github.com/tiliado/nuvola-app-kexp)
   maintained by [Michael Nye](https://github.com/thenyeguy)
 * [Logitech Media Server 2.2](https://github.com/tiliado/nuvola-app-logitech-media-server)
   maintained by [Steffen Coenen](https://github.com/Tar-Dingens)
 * [Mixcloud 3.2](https://github.com/tiliado/nuvola-app-mixcloud)
   maintained by [Samuel Mansour](https://github.com/s83)
 * [Plex Music 1.3](https://github.com/tiliado/nuvola-app-plex)
   maintained by [SkyghiS](https://github.com/skyghis)
 * [SiriusXM 1.3](https://github.com/tiliado/nuvola-app-siriusxm)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [SoundCloud 1.3](https://github.com/tiliado/nuvola-app-soundcloud)
   maintained by [KiXaM](https://github.com/kixam)
 * [Spotify 2.3](https://github.com/tiliado/nuvola-app-spotify)
   maintained by [Michael Nye](https://github.com/thenyeguy)
 * [TuneIn 1.3](https://github.com/tiliado/nuvola-app-tunein)
   maintained by [Aurélien Jabot](https://github.com/ajabot)
 * [Yandex Music 1.4](https://github.com/tiliado/nuvola-app-yandex-music)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)
 * [YouTube 1.3](https://github.com/tiliado/nuvola-app-youtube)
   maintained by [Joel Cumberland](https://github.com/jrosco)
 * [ownCloud Music 1.2](https://github.com/tiliado/nuvola-app-owncloud-music)
   maintained by [Jiří Janoušek](https://github.com/fenryxo)

Explore Features
================

<div class="row">
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-gnome"><img src=":images/3.0/gnome/gnome_add_to_favorites[256x192].png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-gnome">GNOME</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-unity"><img src=":images/3.0/unity/unity_google_play_music_launcher_thumbs_up[256x192].png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-unity">Unity</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-terminal"><img src=":images/3.0/unity/unity_nuvolactl_multiple_apps[256x192].png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-terminal">Terminal & scripts</a>
      </div>
    </div>
  </div>
</div>

Missing Features
================

Since I didn't want to postpone release of Nuvola Player 3 again and again, I decided not to
implement some features available in Nuvola Player 2 for now. As a result, following features are
missing in Nuvola Player 3 and might be added later upon demand from users: Libre.fm scrobbling,
translations and file downloads. 

Limited Support and Commercial Support
======================================

Nuvola Player 3 project provides free support on best-effort basis without any guarantees.
Officially supported distributions include [Ubuntu](./install-ubuntu.html) 16.04, 16.10 and 17.04,
[Fedora](./install-fedora.html) 24-25, and [Debian](./install-debian.html) 
Stretch and Sid. The Nuvola Player developer has tested installation and functionality in clean
virtualized instances of these distributions and can assure reasonable user support in case of
problems. However, Nuvola Player should also work on
[other modern Linux distributions](./install-other-linux.html), but user experience might
not be optimal (e.g. inconsistent look and behavior) and quality of user support depends on
complexity of an issue.

If free support on best-effort basic is not sufficient, you can contract the Nuvola Player developer
for a commercial support.

Project Funding
===============

My work on Nuvola Player is [funded by Nuvola Patrons](https://tiliado.eu/nuvolaplayer/funding/).
My dream is to work as an independent developer on open source software for all people around the
world, software for you. If you like Nuvola Player, or even use it every day, you can
[show your gratitude by supporting the project](https://tiliado.eu/nuvolaplayer/funding/).

Thank you and happy listening!

Jiří Janoušek

Maintenance Releases {: #maintenance}
====================

Nuvola Player 3.0.10
-------------------

Maintenance release **3.0.10** was released on September 1st, 2017. It fixes high CPU usage under Wayland
and exchanges “Stable Release” designation for “Legacy Release”.

Nuvola Player 3.0.9
-------------------

Maintenance release **3.0.9** was released on July 18th, 2017.

* WebKitGTK+ ≥ 2.16.3 is required as it fixes many web compatibility issues.
* Welcome text updated with with the link to Nuvola’s Medium blog and information about Nuvola 3.0.x End of Life schedule.

Nuvola Player 3.0.8
-------------------

Maintenance release **3.0.8** was released on April 15th, 2017, addressing following issues:

  * Missing license file.
  * Updated copyright year in the About dialog.
  * Fixed start-up WM Class in the desktop file. Issue: tiliado/nuvolaplayer#305
  * Build script fixed to require Diorite 0.2.2.
  * Fixed crash with Valac 0.36.

Nuvola Player 3.0.7
-------------------

Maintenance release **3.0.7** was released on February 26th, 2017, addressing following issues:

  * NuvolaPlayer/SoundCloud 3.0.5 menu item 'Unknown application name'.
    Issue: tiliado/nuvolaplayer#301
  * SoundCloud 3.0.5 crashes when started from a Ubuntu Launcher.
    Issue: tiliado/nuvolaplayer#302
  * Web App scripts should provide own desktop files.
    Issue: tiliado/nuvolaplayer#263

In addition, Nuvola 3.0.6 no longer supports scripts not built with
the [Nuvola SDK](https://github.com/tiliado/nuvolasdk). This backward
incompatible change is necessary for a smooth transition to Nuvola 4.0.

Nuvola Player 3.0.6
-------------------

Maintenance release **3.0.6** was released on February 25th, 2017, addressing the same issues as 3.0.7 but with
an insufficient fix for NuvolaPlayer/SoundCloud 3.0.5 menu item 'Unknown application name'.

Nuvola Player 3.0.5
-------------------

Maintenance release **3.0.5** was released on February 18th, 2017, addressing following issues:

  * False positive "Too many flash plugins" has been fixed.
    Issue: tiliado/nuvolaplayer#159
  * Repeated Runner: prefix in debugging output has been suppressed.
    Issue: tiliado/nuvolaplayer#265
  * Nuvola is compatible with scripts built with the Nuvola SDK build system
    providing own desktop launchers. Moreover, scripts without the desktop files
    are deprecated and might not function properly in the next release.
    Issue: tiliado/nuvolaplayer#263
  * The usage of the old Tiliado API has been removed along with the donation bar.
  * Frequent deadlocks of the web rendering process of recent versions of WebKitGTK
    have been addressed.
    Issue: tiliado/nuvolaplayer#279
  * A workaround addressing a bug in older graphics drivers is now disabled with recent versions
    of WebKitGTK as it is no longer necessary and causes huge CPU usage under Wayland.
    Issue: tiliado/nuvolaplayer#260

Nuvola Player 3.0.4
-------------------

Maintenance release **3.0.4** was released on September 17th, 2016, addressing following issues:

  * A crash under Wayland session was fixed (GDK_BACKEND set to x11).
    Issue: tiliado/nuvolaplayer#181
  * The accelerated compositing mode is disabled with WebKitGTK < 2.13.4 due to a WebKitGTK+ bug that may crash systems with certain graphic cards.
    Upstream: https://bugs.webkit.org/show_bug.cgi?id=126122
    Issue: tiliado/nuvolaplayer#245
  * A non-functional local-storage-directory setting was removed as it produced a console warning.
  * The design of the Welcome screen was improved.
  * It is possible to disable media keys in the Preferences dialog.
    Issue: tiliado/nuvolaplayer#237

Nuvola Player 3.0.3
-------------------

Maintenance release **3.0.3** was released on June 4th, 2016, addressing following issues:

  * A wrong implementation of the CanPlay and CanPause flags of the Media Player Remote Interface Specification (MPRIS)
    was fixed resolving issues with Unity Sound Indicator as a result. Issue: tiliado/nuvolaplayer#224
  * Console warnings produced when notifications component were being disabled were fixed.
    Issue: tiliado/nuvolaplayer#227
  * Initialization of the Web Worker process is more robust. Blank incompletely loaded and improperly initialized
    web pages should no longer occur.
  * Notifications API is no longer called if it is disabled as it is obviously not functional and produces only console
    warnings. Issue: tiliado/nuvolaplayer#227
  * JavaScript API got new Nuvola.VERSION and Nuvola.API_VERSION constants for scripts to be able to detect whether
    currently running instance is NP 3.0.3 or higher and it is possible to run code which caused improper Web Worker
    initialization in older versions.
  * A version of the LibSoup library is shown in `nuvolaplayer3 --version` and in the About dialog. In addition,
    JavaScript API got Nuvola.LIBSOUP_VERSION, Nuvola.LIBSOUP_MAJOR, Nuvola.LIBSOUP_MINOR and LIBSOUP_MICRO constants
    for script to detect not new enough versions and to recommend upgrading. Issue: tiliado/nuvola-app-spotify#13

Nuvola Player 3.0.2
-------------------
Maintenance release **3.0.2** was released on April 29th, 2016, addressing following issues:

  * Added hint how to edit/remove keyboard shortcut in the Keyboard shortcuts tab of the Preferences dialog.
    Issue: tiliado/nuvolaplayer#217
  * WebView used to fail to initialize properly sometimes resulting in empty non-functional window. 
    This should not occur any more. Issue: tiliado/nuvolaplayer#207
  * WebKitGTK version information was added to the JavaScript API for web app scripts to check whether they are
    compatible and notify user if they are not. Issue: tiliado/nuvolaplayer#215
  * Ubuntu 14.04: WebKitGTK 2.8.5 packages have been uploaded to the Nuvola Player repository and Nuvola Player now uses
    this version instead the old packages from the official Ubuntu archive. this should fix various rendering and
    integration issues that happened only in Ubuntu 14.04. Issue: tiliado/nuvolaplayer#216
  * Fedora 22 and 23: Nuvola Player package also depends on the webkitgtk4-plugin-process-gtk2 package.
    Issue: tiliado/nuvolaplayer#223

Nuvola Player 3.0.1
-------------------

Maintenance release **3.0.1** was released on February 14th, 2016, addressing following issues:

  * Configuration option `--with-appindicator` was removed as AppIndicator integration is currently
    unmaintained. Issues: tiliado/nuvolaplayer#201 and tiliado/nuvolaplayer#45

  * Web app integration template was moved to
    [its own repository](https://github.com/tiliado/nuvola-app-template)
    to keep it up-to-date independently on Nuvola Player releases. Developer documentation was
    updated accordingly.

  * The `nuvolaplayer3 --help` screen now lists also the `-a/--app-id` argument used to launch
    a particular service. Issue: tiliado/nuvolaplayer#147
    
  * All pop-up windows now can pop up a new window, which is required by the SoundCloud's
    log-in-via-Google feature, for instance. Issue: tiliado/nuvola-app-soundcloud#3


[TOC]
