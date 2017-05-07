Title: Nuvola Apps 3.1 Release Notes
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Apps 3.1 is the second series of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration
    with Linux desktop environments than usual web browsers can offer. Nuvola handles
    multimedia keys, shows desktop notifications, integrates with various sound indicators, media
    player applets, GNOME lock screen and launchers and more.

!!! warning "Rolling Releases are for PremiumPatron users"
    Rolling Releases are provided for Premium/Patron users as a benefit for their support. You will
    need to enter credentials of your Tiliado account with active
    [Nuvola Premium or Patron plan](https://tiliado.eu/nuvolaplayer/funding/)
    to access these builds.

Nuvola Apps 3.1 was forked from release 3.0 on December 30, 2015 and many changes under the hood 
have been made and many new features & enhancements have been added since then. 
    
About Nuvola Apps
=================

**Nuvola Apps** is a runtime for web-based music streaming services providing more native user
experience and integration with Linux desktop environments than usual web browsers can offer. It
tries to feel and look like a native application as possible. However, it cannot overcome common
drawbacks of web-based music streaming: some music streaming services require Flash plugin and web
apps usually have higher memory usage than native apps.

What's New
==========

Nuvola 3.1 is constantly evolving, to **stay in touch**

 * Follow Nuvola Player on [Facebook](https://www.facebook.com/nuvolaplayer),
    [Google+](https://plus.google.com/110794636546911932554) or
    [Twitter](https://twitter.com/NuvolaPlayer).
  * Subscribe to the Nuvola Player Newsletter: [weekly](http://eepurl.com/bLbm5H)
    or [monthly](http://eepurl.com/bLbtM1).

Milestone 3.1.4
---------------

The milestone 3.1.4 is still in development.

### Gallery

 Gallery 2cols
+[Preferences dialog and AppIndicator in Ubuntu's Unity.](images/3.1/appindicator/appindicator_unity_thumbs_up.png|320)
+[AppIndicator in Ubuntu's Unity while Nuvola is running in background.](images/3.1/appindicator/appindicator_unity_activate_window.png|320)
+[Preferences dialog and AppIndicator in elementaryOS.](images/3.1/appindicator/appindicator_pantheon_thumbs_up.png|320)
+[AppIndicator in elementaryOS while Nuvola is running in background.](images/3.1/appindicator/appindicator_pantheon_activate_window.png|320)
+[Preferences dialog and AppIndicator in GNOME Shell.](images/3.1/appindicator/appindicator_gnome_thumbs_up.png|320)
+[AppIndicator in GNOME Shell while Nuvola is running in background.](images/3.1/appindicator/appindicator_gnome_activate_window.png|320)
+[Website data manager.](images/3.1/features/website_data_manager.png|320)

### New Features

  * Tray icon feature can now use AppIndicator library instead of obsolete X11 tray icons. Although app indicators
    are mostly known from Ubuntu's Unity desktop, they also work in elementaryOS and GNOME Shell (with
    [AppIndicator extension](https://extensions.gnome.org/extension/615/appindicator-support)) and provide
    superior user experience. Issue: tiliado/nuvolaplayer#45
  * Users can easily clear cookies, cache and temporary files, IndexedDB and WebSQL databases and local storage
    from the Preferences dialog → tab Website Data. Issue: tiliado/nuvolaplayer#331

### Enhancements

  * Nuvola can do its own user agent quirks (i.e. to disguise itself as a different web browser) in order to work
    around web pages that doesn't work with the WebKit's user agent string. Issue: tiliado/nuvolaplayer#336

### Web App Scripts

  * Google Play Music script uses own user agent quirks to work around the malfunctioning Google sign-in web page.
    Issue: tiliado/nuvolaplayer#336

### Bug fixes

  * The build script now raises error if it is ran with Python < 3.4.
  * Fixed a bug when the menus of tray icons and dock items were not updated.
  * Nuvola now aborts when required data files are not found (e.g. in incomplete installation) rather they running
    with errors in the background.
  * Obsolete test suite has been removed. A new one will be created during ongoing modernization.
    Issue: tiliado/nuvolaplayer#335

### Under the Hood

  * WebKitGTK+ >= 2.16.0 is required as all new API is now used unconditionally to make maintenance easier.
  * Added optional dependency on appindicator3-0.1 >= 0.4. Use `./waf configure --noappindicator` to disable
    this dependency and related functionality (AppIndicator backend for Tray icon feature).

Milestone 3.1.3 
---------------

The milestone 3.1.2 was released on April 30, 2017.

### New Features

  * elementaryOS Loki has been added among officially supported distributions. Nuvola flatpaks contain
    a work-in-progress GTK+ 3.22 port of the elementary theme to provide elementaryOS users with a native look.
    Installation instructions and documentation have been updated accordingly.
    Issue: tiliado/nuvolaplayer#4
  * All three variants of the Arc theme have been added to Nuvola flatpaks. Issue: tiliado/nuvolaplayer/issues/318

### Enhancements

  * Ubuntu themes have been updated. Issue: tiliado/nuvolaplayer#324
  * Initial start-up of flatpak builds is faster.
  * The text of Welcome dialog was moved to the first tab of the main window because it may contain useful information.
  * WebKitGTK+ 2.16 API to set network proxy is used replacing previous legacy hacks.
  * The official builds of Nuvola are marked as "genuine flatpak builds"

### Bug fixes

  * Apps that are not media players no longer steal media keys. Issue: tiliado/nuvolaplayer#230
  * Fixed activation for Premium users. Issue: tiliado/nuvolaplayer#325
  * App menu, toolbar & menu bar handling was refactored and double app menus fixed. Issue: tiliado/diorite#4

### Under the Hood

  * Build script of Nuvola was reworked, ported to Waf 1.9.10 and supports branding. See Readme.md
    for more information.
  * Build script of Diorite was reworked and ported to Waf 1.9.10. See Diorite's Readme.md for more information.
  * Modernisation has begun. Dependencies were raised and legacy code is being removed.
  * All Python scripts require Python >= 3.4.
  * Code has been ported to Valac 0.36.


Milestone 3.1.2 
---------------

The milestone 3.1.2 was released on March 26, 2017 (123 commit since the 3.1.1 milestone).

### New Features

  * Nuvola Player was renamed to Nuvola Apps as non-media player apps (Google Calendar) were enabled
    and should be fully supported in the 4.0 release.
  * Nuvola Apps are distributed as [cross-distribution flatpak builds](https://nuvola.tiliado.eu/).
    There have been a lot of changes under the hood to support this transition.
  * The `nuvolaplayer3` and `nuvolaplayer3ctl` commands are deprecated in favor of `nuvola` and `nuvolactl`.
  * WebApp scripts provide own desktop files so the unnecessary create/delete desktop launchers actions
    were removed.

### Enhancements

  * Enhanced support of HTML5 Audio and Media Source Extension (MSE), which is currently enabled only
    in the BBC iPlayer script with a custom WebKitGTK+ build.
  * Album art is downloaded with WebKit's NetworkProcess to access images that are otherwise restricted.
    Issue: tiliado/nuvolaplayer#76
  * Preferences dialog: Components tab was renamed to Features as it is more user-friendly.

### Under the Hood

  * Inter-process communication has been reworked for greater flexibility as required by the HTTP Remote Control
    feature.
  * Nuvola and individual apps are DBus-activatable.
  * The unique name has been changed to `eu.tiliado.Nuvola` and most of the resources (e.g. icons) use this name.
  * AppData/AppStream metadata have been updated.
  * The build script now honors the VAPIDIR env variable.
  * Added a script to set up Nuvola CDK environment (`setup_nuvolacdk.sh`).

### Bug Fixes

  * "Too many flash plugins" false positives. Resolve symlinks and track final paths not to count duplicates.
    Issue: tiliado/nuvolaplayer#159
  * Repeated Runner: prefix in debugging output. Issue: tiliado/nuvolaplayer#265
  * Disable LIBGL_DRI3_DISABLE workaround with WebKitGTK 2.14+ to fix performance issues.
    Issue: tiliado/nuvolaplayer#260

### News for Script Maintainers

  * Documentation has been updated and Mantainer's Guide merged into the tutorial.
  * Format requirements flag were implemented but not yet documented.
  * Web app scripts are built with Nuvola SDK.

Milestone 3.1.1
---------------

The milestone 3.1.1 was released on October 2016.

### New Features

[Ability to both display and set track rating in Media Player Indicator GNOME Shell extension](:3.1/explore.html#media-player-indicator-extension)
:   Providing a streaming service supports it, Nuvola Player 3.1 exports track rating in MPRIS
    interface and a custom method to set rating of a track. Note that as of October 30th 2016,
    [Player Indicator git master version](:3.1/explore.html#media-player-indicator-extension) is required.

[HTTP Remote Control interface](:3.1/explore.html#remote-control-over-http)
:   This interface allows creation of client apps to control Nuvola Player over network via an Engine.io socket.

[Media Player Controller web page](:3.1/explore.html#media-player-controller-web-page)
:   This page is an example of a client using the HTTP Remote Control interface. It allows you to control Nuvola Player
    from any device with a web browser (e.g. a phone).
[Nuvola Controller Pebble Watchapp](:3.1/explore.html#nuvola-controller-pebble-watchapp)
:   This app for Pebble watches is another example of a client using the HTTP Remote Control interface. It allows you to control Nuvola Player
    from your wrist.
[Password Manager](:3.1/explore.html#password-manager)
:  With the Password Manager, you can store passwords from login forms in a secure keyring.

### Enhancements:

  * An option to always run in background regardless a song is playing or not. See in action in
    [Unity](./explore.html#play-in-background-with-notifications) or
    [GNOME](./explore.html#play-in-background-with-notifications_1).
  * Better support of HTML5 Audio. It is sufficient for ownCloud Music web app but more work is still necessary to support Google Play Music. Issue: tiliado/nuvolaplayer#52
  * Pop-up windows are allowed to pop up a new window, which is required by the SoundCloud's log-in-via-Google feature. Issue: tiliado/nuvola-app-soundcloud#3
  * A hint how to edit or remove a keyboard shortcut. Issue: tiliado/nuvolaplayer#217
  * Users can disable media keys bindings in the Preferences dialog. Issue: tiliado/nuvolaplayer#237
  * Inter process communication backed has been rewritten.
  * All web app scripts have been ported to comply with the latest guidelines.
  * Packaging improvements: support of independent installation of individual scripts and correct package metadata (e.g. license and homepage).

### Bug Fixes

  * Remove config option `--with-appindicator` as the AppIndicator integration is currently unmaintained. Issue: tiliado/nuvolaplayer#201, tiliado/nuvolaplayer#45
  * Add missing `-a/--app-id` command-line argument to the `--help` screen. Issue: tiliado/nuvolaplayer#147 
  * MPRIS implementation of CanPlay and CanPause flags has been fixed. Issue: tiliado/nuvolaplayer#224
  * Warnings when Notifications is being disabled has been removed. Issue: tiliado/nuvolaplayer#227
  * Don't use notifications API if disabled as it produces critical warnings. Issue: tiliado/nuvolaplayer#227
  * Set GDK_BACKEND to x11 not to crash under Wayland. Issue: tiliado/nuvolaplayer#181
  * Disable compositing mode in WebKitGTK < 2.13.4 as it may crash some websites. Issue: tiliado/nuvolaplayer#245

### News for Script Maintainers:

  * Web app integration template has been moved to [its own repository](https://github.com/tiliado/nuvola-app-template).
  * Added information about Format Requirements Flags. Issue: tiliado/nuvolaplayer#158
  * `Nuvola.VERSION` property contains Nuvola version encoded as single integer, e.g. e.g. 30105 for 3.1.5.
  * `Nuvola.API_VERSION` property contains Nuvola API version encoded as single integer, e.g. e.g. 301 for 3.1.
  * `Nuvola.WEBKITGTK_{VERSION,MAJOR,MINOR,MICRO}` properties contain version information about WebKitGTK+ library.
  * `Nuvola.LIBSOUP_{VERSION,MAJOR,MINOR,MICRO}` properties contain version information about Soup library.
  * New API to set rating.
  * It is possible to set a user agent string via the `user_agent` field of metadata.json. Issue: tiliado/nuvolaplayer#91
  * It is possible to enable access to insecure content. This happens when a web page loaded over HTTPS protocol loads any content over HTTP protocol.
  * Developer documentation and guidelines have been updated.
  
### Changes in Dependencies

  * Increased: WebKitGTK >= 2.6.2, Valac >= 0.26.1, GLib >= 2.42.1 and GTK+ >= 3.14.5.
  * New: libuuid and libnm-(util/glib)

Install Nuvola
==============

Nuvola project provides **cross-distribution flatpak packages** of Nuvola 3.1, which contain all
requires dependencies. In order to install a particular Nuvola app, follow steps in the
[Nuvola Apps Repository Index](https://nuvola.tiliado.eu/) portal according to your distribution:

  * [Ubuntu 16.04 Xenial Xerus](https://nuvola.tiliado.eu/#!index!ubuntu!xenial)
  * [Ubuntu 16.10 Yakkety Yak](https://nuvola.tiliado.eu/#!index!ubuntu!yakkety)
  * [Ubuntu 17.04 Zesty Zapus](https://nuvola.tiliado.eu/#!index!ubuntu!zesty)
  * [elementaryOS 0.4 Loki](https://nuvola.tiliado.eu/#!index!elementary!loki)
  * [Debian 8 Jessie (stable)](https://nuvola.tiliado.eu/#!index!debian!stretch)
  * [Debian 9 Stretch (testing)](https://nuvola.tiliado.eu/#!index!debian!jessie)
  * [Debian Sid (unstable)](https://nuvola.tiliado.eu/#!index!debian!sid)
  * [Fedora 25](https://nuvola.tiliado.eu/#!index!fedora!fc25)
  * [Fedora 24](https://nuvola.tiliado.eu/#!index!fedora!fc24)
  * [Arch Linux](https://nuvola.tiliado.eu/#!index!archlinux)
  * [Other linux](https://nuvola.tiliado.eu/#!index!other)


[TOC]
