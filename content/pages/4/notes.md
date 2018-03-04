Title: Nuvola Apps 4 Release Notes
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Apps 4 is the fourth generation of a runtime for
    web-based music streaming services that provides more native user experience and integration
    with Linux desktop environments than usual web browsers can offer. Nuvola handles
    multimedia keys, shows desktop notifications, integrates with various sound indicators, media
    player applets, GNOME lock screen and launchers and more.
   
About Nuvola Apps
=================

**Nuvola Apps** is a runtime for web-based music streaming services providing more native user
experience and integration with Linux desktop environments than usual web browsers can offer. It
tries to feel and look like a native application as possible. However, it cannot overcome common
drawbacks of web-based music streaming: some music streaming services require Flash plugin and web
apps usually have higher memory usage than native apps.

What's New
==========

Nuvola 4 is constantly evolving, to **stay in touch**

 * Follow Nuvola Player on [Facebook](https://www.facebook.com/nuvolaplayer),
    [Google+](https://plus.google.com/110794636546911932554) or
    [Twitter](https://twitter.com/NuvolaPlayer).
  * Subscribe to the Nuvola Player Newsletter: [weekly](http://eepurl.com/bLbm5H)
    or [monthly](http://eepurl.com/bLbtM1).


Release 4.10
------------

Nuvola 4.10 was released on March 4th, 2018.

### New features

Nuvola introduces a new experimental backend based on Chromium Embedded Framework, which facilitates a switch to audio playback without Flash plugin. At present, only Spotify, Deezer, YouTube, Mixcloud, and BBC iPlayer use the new engine, mostly because these scripts simply does not work with the old WebKitGTK backend. The goal of the project is to eventually port all scripts from Flash plugin to HTML5-Audio-based playback.

### Enhancements

* **Amazon Cloud Player 5.6** by Andrew Stubbs: Updated album name extraction, added thumbs up/down actions and fixed compatibility with CEF backend.
* **BBC iPlayer 1.4** by Andrew Stubbs: Update live TV & radio integration; fixed compatibility with CEF backend.
* **Deezer 3.0** by Jiří Janoušek: Switched to HTML5 Audio playback instead of the Flash plugin; fixed "Add to Favorite tracks" action.
* **Micxloud 4.1** adopted by Jiří Janoušek: Ported to support the new interface and added CEF backend requirement.
* **Spotify 3.0** adopted by Jiří Janoušek: Updated to support new Spotify web player. Requires CEF backend.
* **YouTube 2.0** adopted by Jiří Janoušek: Fixed metadata parsing and ported to use HTML5 Audio/Video. Requires CEF backend.

### Under the hood

* `Nuvola.parseTimeUsec` now supports negative time specs.
* Increased requirements: Vala >= 0.38.4.
* New mandatory dependency: libarchive >= 3.2
* New optional dependencies: ValaCEF (`--no-cef`), Vala linter (`--no-vala-lint`).
* Source code was refactored to use a united coding style which is checked with Vala linter.
* Some configure options were renamed (e.g. `--noxxx` → `--no-xxx`)
* GIR generation is now optional, you can pass `--no-gir` to disable it.
* Welcome screen is now shown from App Runner process instead of the Nuvola Service process, which makes start-up faster.
* App Runner is now installed as `bin/nuvolaruntime` and can be invoked independently on Nuvola Service. However, some features are not available if the service cannot be launched via DBus activation.
* Nuvola Service lost most of command line parameters and cannot be used to launch scripts with `nuvola -a ID`. Use `nuvolaruntime` instead.
* The default unique id is now `eu.tiliado.WebRuntime`, which is used consistently.
* Test scripts from `web_apps` directory are no longer installed. You may install them manually if you deem it necessary.

### Nuvola SDK 4.10.0


* Nuvola 3.0 compatibility mode was removed.
* The `nuvola-app-xxx` binary launcher was replaced with a shell script, which is now always included. It requires Nuvola 4.10. Consequently, `--with-dbus-launcher` configure option was removed.
* Individual apps now use the `eu.tiliado.WebRuntimeApp...` unique id.
* AppStream Addon XML metadata are generated. Issue: [tiliado/nuvolasdk#1](https://github.com/tiliado/nuvolasdk/issues/1)

### Diorite 4.10.0

* Increased requirements: Vala >= 0.38.4.
* The VAPIDIR environment variable is supported to set extra Vala API directories.
* GIR generation is now optional, you can pass `--no-gir` to disable it.
* Fixed bug in Entry widget that prevented user input.
* Fixed bug when XDG Desktop Portal web browser selector was shown under a dialog window instead of above it.
* RequirementsParser supports 4 states: 
* New utility functions: Drt.print_variant()
* Added Drt.Event thread synchronization primitive.

Release 4.9
----------

Nuvola 4.9 was released on December 17th, 2017. It is mostly a maintenance release as most of energy is invested in the
Chromium port of Nuvola and the development of other features has slowed down. The current status of this ambitious
effort will be described in a separate announcement.

### Enhancements

  * **URL entry widget** was added: Press Ctrl+L or click the *gear menu* button → *Load URL* to display/change the
    current URL.
  * Updated script: **Yandex Music 1.5** was adopted by Aleksey Zhidkov and enhanced with an integrated Like button.
    An album art fix by Alexander Konarev has been also incorporated.
    Issue: [tiliado/nuvola-app-yandex-music#2](https://github.com/tiliado/nuvola-app-yandex-music/issues/2),
    [tiliado/nuvola-app-yandex-music#10](https://github.com/tiliado/nuvola-app-yandex-music/issues/10).
  * Updated script: **SiriusXM 1.4** by Jiří Janoušek. Metadata parsing adapted to recent SiriusXM changes.
  * Updated script: **BBC iPlayer 1.3** by Andrew Stubbs. Fixed integration of radio shows, added integration of
    progress bar, volume bar and skip action.
  * Page **loading indicator** was added.
    Issue: [tiliado/nuvolaruntime#229](https://github.com/tiliado/nuvolaruntime/issues/229)
  * If Bumblebeed is detected, Nuvola assumes that the integrated Intel graphics card is the primary and skips
    unnecessary checks for an NVidia flatpak driver.
    Issue: [tiliado/nuvolaruntime#380](https://github.com/tiliado/nuvolaruntime/issues/380)
  * Various fixes regarding VDPAU & VA-API drivers.
    Issue: [tiliado/nuvolaruntime#380](https://github.com/tiliado/nuvolaruntime/issues/380)

### Under the hood

  * WebKitGTK >= 2.18.0 is required.
  * If Nuvola is told that WebKitGTK supports MSE, it checks whether it is so and aborts otherwise. Don't use
    `--webkitgtk-supports-mse` if it isn't true.
  * Fixed various memory leaks.
  * Ongoing optimizations to replace synchronous IPC calls with asynchronous variants.
  * [ValaCEF project](https://github.com/tiliado/valacef) has been created to provide Nuvola with Vala bindings
    for Chromium Embedded Framework (CEF).

### Nuvola SDK 4.9.0

  * Default API version is 4.9.

### Diorite 4.9.0

  * New widget: Drtgtk.Entry - an enhanced version og Gtk.Entry.
  * Fixed parsing of RPC notifications.
    Issue: [tiliado/nuvolaruntime#385](https://github.com/tiliado/nuvolaruntime/issues/385)
  * New widget: Drtgtk.HeaderBarTitle - a custom title widget for Gtk.HeaderBar.
  * New utility function: System.cmdline_for_pid - Get command line of a process with given PID.
  * Better debugging: Distinguish between socket creation errors.
    Issue: [tiliado/nuvolaruntime#378](https://github.com/tiliado/nuvolaruntime/issues/378)
  * New namespace: Drt.Dbus -  DBus introspection and service activation.
  * New utility method: Drt.Flatpak.check_desktop_portal_available - to check whether a proper XDG Desktop Portal DBus
    interface is present.
  * New functionality: Functions to get, set and look up GTK+ 3 themes - see Drtgtk.DesktopShell.
  * New widget: Drtgtk.GtkThemeSelector - a selector to list and change a GTK+ theme.

Release 4.8
----------

Nuvola 4.8 was released on September 29th, 2017.

### New Features

  * New script: **Pocket Casts** by Jiří Janoušek. Pocket Casts is the only podcatcher you’ll ever need. Listen to your
    favorite shows in one place, keep in sync progress across various devices, find great new content with curated
    featured podcasts, currently trending podcasts and much more. Now also with desktop integration provided by Nuvola.
  * Updated script: **Groove Music script 2.0** by Joel Cumberland works again in Nuvola after being ported to use
    Media Source Extension instead of Flash plugin.
  * Updated script: **Amazon Cloud Player script 5.5** by Andrew Stubbs integrates a track progress bar and volume
    controls.
  * Updated script: **Google Play Music script 6.0** by Jiří Janoušek uses new asynchronous API to improve
    responsiveness and reduce lags, but also drops support for Nuvola 4.7 and older.

### Discontinued Features

 * **Spotify script** is temporarily unsupported until Nuvola is ported to Chromium Embedded framework because Spotify
   dropped support for WebKit browsers (including Nuvola and Safari).
 * **Yandex Music** script is currently orphaned and needs a new maintainer. The script is still shipped with Nuvola 4.8
   but may be removed in the future unless somebody adopts it. If anyone is interested, please get in touch with me at
   [Nuvola Devel mailing list](https://groups.google.com/d/forum/nuvola-player-devel).

### News for Script Maintainers

  * Asynchronous variants of various JavaScript API calls were introduced deprecating original synchronous methods.
    The async methods return
    [a Promise object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises),
    which is used to resolve the result of the async operation.
  * List of async methods: Notifications.isPersistenceSupportedAsync, Actions.isEnabledAsync, Actions.getStateAsync,
    Core.getComponentInfoAsync, Core.isComponentLoadedAsync, Core.isComponentActiveAsync,
    KeyValueStorage.setDefaultAsync, KeyValueStorage.hasKeyAsync, KeyValueStorage.getAsync and KeyValueStorage.setAsync.
  * New function: Nuvola.logException to log exceptions to terminal.
    JavaScript API reference now supports new annotations such as "Deprecated since", "Available since" and
    "asynchronous" function.

### Under the Hood

  * Nuvola uses new IPC API from Diorite 4.8 and replaced a lot of synchronous IPC calls between WebWorker and AppRunner
    processes with asynchronous variants. This should improve the performance of the WebKit WebProcess, reduce lags and
    prevent occasional deadlocks. However, scripts must use the newly-introduced async JavaScript API to reach the full
    potential. Google Play Music is the first one.

### Diorite 4.8.0

  * Various IPC classes were refactored and united into new API (Rpc prefix) and it is possible to respond to IPC
    messages asynchronously.
  * KeyValueStorage got async equivalents of non-void methods.

Release 4.7
----------

Nuvola 4.7 was released on September 1st, 2017.

### New Features

  * New web app:  Jupiter Broadcasting by Andrew Stubbs.
  * The genuine flatpak builds offers free trial and $1/month subscription.
  * For sake of transparency, preferences dialog shows placeholders for features which were disabled by a distributor.

### Bug Fixes:

  * VAAPI/VDPAU checks are not run under Wayland. Issue:
    [tiliado/nuvolaruntime#280](https://github.com/tiliado/nuvolaruntime/issues/280) Issue:
    [tiliado/nuvolaruntime#359](https://github.com/tiliado/nuvolaruntime/issues/359)
  * URL sandbox was not honoured properly: Issue:
    [tiliado/nuvolaruntime#367](https://github.com/tiliado/nuvolaruntime/issues/367)

### News for Script Maintainers:

  * API 4.6 is required for new scripts.

### Under the Hood:

  * Nuvola no longer bundles `*.vapi` files but depends on those of Valac 0.36.3. However, glib-2.0.vapi and
    webkit2gtk-web-extension-4.0.vapi must be patched to work properly (see `vapi/*.patch`). You may need to modify
    wscript if you don't use Valac 0.36. Issue:
    [tiliado/nuvolaruntime#369](https://github.com/tiliado/nuvolaruntime/issues/369)
  * Valac and GLib dependencies were raised to 0.36.3 and 2.52. Issue:
    [tiliado/nuvolaruntime#369](https://github.com/tiliado/nuvolaruntime/issues/369)
  * GIR XML and typelib files are generated. Introduces new dependency on g-ir-compiler.
  * There was a lot of refactoring to allow usage of Python-GObject and to support multiple web engines in future.
  * Future warning: Nuvola is likely to introduce dependency on Python 3.6.

### Nuvola SDK 4.7.0

  * desktop launcher: Spaces around the equals sign were removed because they confuse kbuildsycoca5. Issue:
    [tiliado/nuvolaruntime#365](https://github.com/tiliado/nuvolaruntime/issues/365)
    [Upstream ticket](https://bugs.kde.org/show_bug.cgi?id=310674)
  * Added individual version info properties - `nuvolasdk.VERSION_MAJOR/MINOR/MICRO`.
  * new-project: New `metadata.in.json` files use the latest Nuvola SDK version.

### Diorite 4.7.0

  * Diorite no longer bundles *.vapi files and depends on those of Vala 0.36.3.
  * GLib dependency has been raised to 2.52.0 to make use of Valac's GTask support.
  * Diorite GTK namespace was changed to Drtgtk.
  * GIR XML and typelib files are generated. Introduces new dependency on g-ir-compiler.

Release 4.6
-----------

Nuvola 4.6  was released on July 29, 2017.

### Gallery

 Gallery 2cols
+[BBC iPlayer script by Andrew Stubbs.](images/4/releases/nuvola_4.6_bbc_iplayer.png|320)
+[An example of an error dialog for the start-up check.](images/4/releases/nuvola_4.6_startup_check.png|320)

### New Features

  * Start-up system checks run in parallel to decrease start-up time. In case of any problem, only a single dialog is
    shown instead of multiple error dialogs or info bars.
  * WebKitGTK+ was upgraded to 2.16.6 fixing many security vulnerabilities and rendering issue.
  * Media Source Extension (MSE) is enabled in WebKitGTK as well as in Nuvola itself. This applies only to the genuine
    flatpak builds of Nuvola. MSE is required by some web apps for Flash-free audio/video playback.
  * New web app: BBC iPlayer by Andrew Stubbs. Note that this script requires MSE and may not work with third-party
   builds of Nuvola. Issue: [tiliado/nuvolaruntime#321](https://github.com/tiliado/nuvolaruntime/issues/321)

### Bug fixes

  * Graphics.dri2_get_driver_name() now throws error instead of an uncaught critical warning if it cannot connect to
    X Server.  Issue: [tiliado/nuvolaruntime#359](https://github.com/tiliado/nuvolaruntime/issues/359)
  * Fixed typo in Nuvola.parseTimeUsec. Issue:
    [tiliado/nuvolaruntime#357](https://github.com/tiliado/nuvolaruntime/issues/357)
  * int64 is used for track position to avoid integer overflow. Issue:
    [tiliado/nuvolaruntime#358](https://github.com/tiliado/nuvolaruntime/issues/358)
    
### News for Script Maintainers

  * Developer sidebar can now change track rating.
  * Media player API documentation was updated with track rating.

### Under the Hood

  * New dependency: [unit.js](https://github.com/unitjs/unit.js/releases/tag/v2.0.0) 2.0.0 
   (installed as /usr/share/javascript/unitjs/unit.js) is used for JavaScript unit tests (included in the test service
   - web_apps/test subdirectory).
  * Added support for org.gnome.SettingsDaemon.MediaKeys D-Bus name.
    [Upstream ticket](https://bugzilla.gnome.org/show_bug.cgi?id=781326).
  * The content of format support dialog was moved to Preferences dialog and various toggles were removed.
  * The content of bindings, models and interfaces directories was merged into components directory. 

### Nuvola SDK 4.6.0

  * genmakefile: Add `-link` suffix to compat symlinks to workaround Debian not being able to replace a directory with
    a symlink. Issue: [tiliado/nuvolaruntime#362](https://github.com/tiliado/nuvolaruntime/issues/362)
  * dbus launcher: Rename Diorite to Drt.
  * Added version info - nuvolasdk.VERSION.
  * genmakefile: It is possible to specify required Nuvola SDK version.

### Diorite 4.6.0

  * Namespaces have been united: Drt for Diorite and Drtdb for Diorite DB.
  * Added utils to interact with GLib event loop (Drt.EventLoop).
  * Added workaround for extra Variant unref in ApiNotifications (Drt.ApiChannel.(un)subscribe).
  * Added methods to (un)subscribe for ApiNotifications.
  * Added CSS style classes for badges (Drt.Css.BADGE_*).
  * Added various utility functions (Drt.Time.get_unix_time_now_utc, Drt.String.concat, Drt.String.append,
    Drt.variant_dump, Drt.variant_ref, Drt.variant_unref).
  * ApplicationWindow.app field is now protected (private previously).

Milestone 4.5
-------------

Nuvola 4.5 was released on June 24th, 2017.

### Gallery

 Gallery 2cols
+[You can seek with Media Player GNOME Shell extension](images/4/progress_volume_bar/gnome_mediaplayer_progressbar.png|320)
+[You can change volume with Media Player GNOME Shell extension](images/4/progress_volume_bar/gnome_mediaplayer_volumebar.png|320)
+[Developer's sidebar was updated with progress bar.](images/4/progress_volume_bar/gnome_mediaplayer_progressbar_developer.png|320)
+[Developer's sidebar was updated with volume slider.](images/4/progress_volume_bar/gnome_mediaplayer_volumebar_developer.png|320)

### New Features

  * Nuvola Apps Runtime supports **the integration of a progress bar and volume management**. Web app scripts
    which use this feature can not only provide track length & position and current volume but also allow
    a user to change that remotely, e.g. from
    [Media Player GNOME Shell extension](https://extensions.gnome.org/extension/55/media-player-indicator/).
    At present, only Deezer
    and Google Play Music scripts use these features, but others will follow.
    Issue: [tiliado/nuvolaruntime#22](https://github.com/tiliado/nuvolaruntime/issues/22) Issue: [tiliado/nuvolaruntime#155](https://github.com/tiliado/nuvolaruntime/issues/155)
  * If Nuvola Apps Runtime detects **a Nvidia graphics card**, it checks whether the flatpak extension with 
    corresponding graphics driver is installed. If it isn't, e.g. because of a bug in GNOME Software,
    an error message is shown to provide the user with installation instructions. Issue: [tiliado/nuvolaruntime#342](https://github.com/tiliado/nuvolaruntime/issues/342)
  * After a lot of effort, a workaround for **the instability of Flash plugin** was found out and is used until
    WebKitGTK developers find a proper fix. However, it is applied only in flatpak builds because it may have
    a negative impact on other WebKitGTK applications otherwise. Issue: [tiliado/nuvolaruntime#354](https://github.com/tiliado/nuvolaruntime/issues/354)

### Bug fixes

  * A wrong command in desktop launcher was fixed. Issue: [tiliado/nuvolaruntime#348](https://github.com/tiliado/nuvolaruntime/issues/348)
  * Fix wscript for non-git builds. Issue: [tiliado/diorite#16](https://github.com/tiliado/diorite/issues/16)

### News for Script Maintainers

  * `Nuvola.VERSION_MICRO` contains micro version of Nuvola Runtime.
  * `Nuvola.API_VERSION_MAJOR` and `Nuvola.API_VERSION_MINOR` are now deprecated aliases of `Nuvola.VERSION_MAJOR`
    and `Nuvola.VERSION_MINOR`.
  * [The tutorial](https://tiliado.github.io/nuvolaplayer/development/apps/tutorial.html) was updated to use Nuvola ADK 4.4.
  * Added documentation of [web app requirement flags](https://tiliado.github.io/nuvolaplayer/development/apps/tutorial.html#web-technologies).
  * Added documentation of [user agent quirks](https://tiliado.github.io/nuvolaplayer/development/apps/tutorial.html#user-agent-quirks).
  * New API for progress bar integration.
  * New API for volume management integration.
  * New utility functions `Nuvola.encodeVersion` and `Nuvola.checkVersion`.
  * `Nuvola.triggerMouseEvent` and `clickOnElement` support relative x & y coordinates, which is useful for clicking on
    a progress bar or a volume bar.

### Under the Hood

  * **New dependencies:** libdrm >= 2.2 and libdri2 >= 1.0
  * Nuvola checks whether VDPAU and VA-API drivers are installed and prints debugging information to console.
    **It will show error dialog in the future though, so make sure the drivers are installed.**
    Issue: [tiliado/nuvolaruntime#280](https://github.com/tiliado/nuvolaruntime/issues/280)
  * Internal icon loading code was refactored. Legacy icon.png and nuvolaplayer3_XXX icons are no longer supported.
    eu.tiliado.NuvolaAppXxx is used everywhere. Issue: [tiliado/nuvolaruntime#353](https://github.com/tiliado/nuvolaruntime/issues/353)

### Nuvola SDK 4.5

  * new-project, convert-project: An user is asked for a git name and a git email if they are not set.
  * Happy Songs demo was updated to include a progress bar and a volume level.
  * genmakefile: A wrong dbus launcher command in a desktop file was fixed. Issue: [tiliado/nuvolaruntime#348](https://github.com/tiliado/nuvolaruntime/issues/348)
  * genmakefile: Legacy nuvolaplayer3_xxx icon symlinks are created only in Nuvola 3.0.x compat mode.
    Issue: [tiliado/nuvolasdk#3](https://github.com/tiliado/nuvolasdk/issues/3)
  * Fixed compatibility with Nuvola 4.5.0.

### Diorite 4.5

  * Fix wscript for non-git builds. Issue: [tiliado/diorite#16](https://github.com/tiliado/diorite/issues/16)
  * Dioritedb has been refactored significantly.
  * Bundled glib.vapi is no longer used.
  * Various utility functions were added, see git log for details.

Milestone 4.4
---------------

The milestone 4.4 was released on May 27, 2017.

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
    superior user experience. Issue: [tiliado/nuvolaplayer#45](https://github.com/tiliado/nuvolaplayer/issues/45)
  * Users can easily clear cookies, cache and temporary files, IndexedDB and WebSQL databases and local storage
    from the Preferences dialog → tab Website Data. Issue: [tiliado/nuvolaplayer#331](https://github.com/tiliado/nuvolaplayer/issues/331)

### Enhancements

  * Versioning scheme was changed to be more compact, e.g. 4.4.1 instead of 3.1.4-1.gabcd. Nuvola 4.0 was re-targeted
    as Nuvola 5.0.
  * Nuvola can do its own user agent quirks (i.e. to disguise itself as a different web browser) in order to work
    around web pages that doesn't work with the WebKit's user agent string. Issue: [tiliado/nuvolaplayer#336](https://github.com/tiliado/nuvolaplayer/issues/336)
  * Flatpak builds use the latest stable WebKitGTK+ 2.16.3 bringing fixes for three security vulnerabilities as well as
    several crashes and rendering issues.

### Web App Scripts

  * Google Play Music script uses own user agent quirks to work around the malfunctioning Google sign-in web page.
    Issue: [tiliado/nuvolaplayer#336](https://github.com/tiliado/nuvolaplayer/issues/336)

### Bug fixes

  * The build script now raises error if it is ran with Python < 3.4.
  * Fixed a bug when the menus of tray icons and dock items were not updated.
  * Nuvola now aborts when required data files are not found (e.g. in incomplete installation) rather they running
    with errors in the background.
  * Obsolete test suite has been removed. A new one will be created during ongoing modernization.
    Issue: [tiliado/nuvolaplayer#335](https://github.com/tiliado/nuvolaplayer/issues/335)
  * Broken -L/--log-file options were removed. Issue: [tiliado/nuvolaplayer#338](https://github.com/tiliado/nuvolaplayer/issues/338)
  * Various fixes of HTTP Remote Control feature.

### Under the Hood

  * Nuvola's filesystem namespace was changed from `nuvolaplayer3` to `nuvolaruntime`. The data dir is installed at
    PREFIX/share/nuvolaruntime, libraries were renamed to `libnuvolaruntime-*.so` and binaries to `nuvola(ctl)`.
    Users' configuration, data and cache is migrated automatically.
  * Nuvola's git repository was moved to https://github.com/tiliado/nuvolaruntime.
  * WebKitGTK+ >= 2.16.0 is required as all new API is now used unconditionally to make maintenance easier.
  * Added optional dependency on appindicator3-0.1 >= 0.4. Use `./waf configure --noappindicator` to disable
    this dependency and related functionality (Tray icon feature).
  * Nuvola no longer bundles Engine.io-client JavaScript library but expect version 3.1.0 of it located at the
    JSDIR/engine.io-client/engine.io.js (JSDIR is DATADIR/javascript unless changed with --jsdir).
    Issue: [tiliado/nuvolaplayer#341](https://github.com/tiliado/nuvolaplayer/issues/341)
  * Nuvola no longer supports web app scripts without a desktop file.
  * Test suite was reintroduced (build/run-nuvolaruntime-tests). Issue: [tiliado/nuvolaplayer#335](https://github.com/tiliado/nuvolaplayer/issues/335)
  * A lot of refactoring and removal of obsolete code and other improvements.

### Nuvola SDK 4.4.0

  * Versioning scheme is synchronized with Nuvola Apps Runtime.
  * DBus Launcher has been ported to use the high level Start-up API of Nuvola and a data service have been removed
    because it is no longer used.
  * Compatibility with Nuvola Player 3.0.x must be enabled with the --compat flag passed to ./configure.
  * Web apps scripts are installed into the PREFIX/share/nuvolaruntime/web_apps directory used by Nuvola 4.4+
    but legacy symlinks in the PREFIX/share/nuvolaplayer3/web_apps directory are also provided for Nuvola 3.x.

### Diorite 4.4.0

  * Versioning scheme is synchronized with Nuvola Apps 4.4. Library names have been changed accordingly:
    dioriteglib-0.3 → dioriteglib4 and dioritegtk-0.3 → dioritegtk4.
  * Vala documentation is built by default. Requires valadoc >= 0.36 but can be disabled with --novaladoc
    flag.
  * Various utility functions were added. See git log for details.

Milestone 3.1.3 
---------------

The milestone 3.1.3 was released on April 30, 2017.

### New Features

  * elementaryOS Loki has been added among officially supported distributions. Nuvola flatpaks contain
    a work-in-progress GTK+ 3.22 port of the elementary theme to provide elementaryOS users with a native look.
    Installation instructions and documentation have been updated accordingly.
    Issue: [tiliado/nuvolaplayer#4](https://github.com/tiliado/nuvolaplayer/issues/4)
  * All three variants of the Arc theme have been added to Nuvola flatpaks. Issue: tiliado/nuvolaplayer/issues/318

### Enhancements

  * Ubuntu themes have been updated. Issue: [tiliado/nuvolaplayer#324](https://github.com/tiliado/nuvolaplayer/issues/324)
  * Initial start-up of flatpak builds is faster.
  * The text of Welcome dialog was moved to the first tab of the main window because it may contain useful information.
  * WebKitGTK+ 2.16 API to set network proxy is used replacing previous legacy hacks.
  * The official builds of Nuvola are marked as "genuine flatpak builds"

### Bug fixes

  * Apps that are not media players no longer steal media keys. Issue: [tiliado/nuvolaplayer#230](https://github.com/tiliado/nuvolaplayer/issues/230)
  * Fixed activation for Premium users. Issue: [tiliado/nuvolaplayer#325](https://github.com/tiliado/nuvolaplayer/issues/325)
  * App menu, toolbar & menu bar handling was refactored and double app menus fixed. Issue: [tiliado/diorite#4](https://github.com/tiliado/diorite/issues/4)

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
    Issue: [tiliado/nuvolaplayer#76](https://github.com/tiliado/nuvolaplayer/issues/76)
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
    Issue: [tiliado/nuvolaplayer#159](https://github.com/tiliado/nuvolaplayer/issues/159)
  * Repeated Runner: prefix in debugging output. Issue: [tiliado/nuvolaplayer#265](https://github.com/tiliado/nuvolaplayer/issues/265)
  * Disable LIBGL_DRI3_DISABLE workaround with WebKitGTK 2.14+ to fix performance issues.
    Issue: [tiliado/nuvolaplayer#260](https://github.com/tiliado/nuvolaplayer/issues/260)

### News for Script Maintainers

  * Documentation has been updated and Mantainer's Guide merged into the tutorial.
  * Format requirements flag were implemented but not yet documented.
  * Web app scripts are built with Nuvola SDK.

Milestone 3.1.1
---------------

The milestone 3.1.1 was released on October 2016.

### New Features

[Ability to both display and set track rating in Media Player Indicator GNOME Shell extension](:4/explore.html#media-player-indicator-extension)
:   Providing a streaming service supports it, Nuvola Player 4 exports track rating in MPRIS
    interface and a custom method to set rating of a track. Note that as of October 30th 2016,
    [Player Indicator git master version](:4/explore.html#media-player-indicator-extension) is required.

[HTTP Remote Control interface](:4/explore.html#remote-control-over-http)
:   This interface allows creation of client apps to control Nuvola Player over network via an Engine.io socket.

[Media Player Controller web page](:4/explore.html#media-player-controller-web-page)
:   This page is an example of a client using the HTTP Remote Control interface. It allows you to control Nuvola Player
    from any device with a web browser (e.g. a phone).
[Nuvola Controller Pebble Watchapp](:4/explore.html#nuvola-controller-pebble-watchapp)
:   This app for Pebble watches is another example of a client using the HTTP Remote Control interface. It allows you to control Nuvola Player
    from your wrist.
[Password Manager](:4/explore.html#password-manager)
:  With the Password Manager, you can store passwords from login forms in a secure keyring.

### Enhancements:

  * An option to always run in background regardless a song is playing or not. See in action in
    [Unity](./explore.html#play-in-background-with-notifications) or
    [GNOME](./explore.html#play-in-background-with-notifications_1).
  * Better support of HTML5 Audio. It is sufficient for ownCloud Music web app but more work is still necessary to support Google Play Music. Issue: [tiliado/nuvolaplayer#52](https://github.com/tiliado/nuvolaplayer/issues/52)
  * Pop-up windows are allowed to pop up a new window, which is required by the SoundCloud's log-in-via-Google feature. Issue: [tiliado/nuvola-app-soundcloud#3](https://github.com/tiliado/nuvola-app-soundcloud/issues/3)
  * A hint how to edit or remove a keyboard shortcut. Issue: [tiliado/nuvolaplayer#217](https://github.com/tiliado/nuvolaplayer/issues/217)
  * Users can disable media keys bindings in the Preferences dialog. Issue: [tiliado/nuvolaplayer#237](https://github.com/tiliado/nuvolaplayer/issues/237)
  * Inter process communication backed has been rewritten.
  * All web app scripts have been ported to comply with the latest guidelines.
  * Packaging improvements: support of independent installation of individual scripts and correct package metadata (e.g. license and homepage).

### Bug Fixes

  * Remove config option `--with-appindicator` as the AppIndicator integration is currently unmaintained. Issue: [tiliado/nuvolaplayer#201](https://github.com/tiliado/nuvolaplayer/issues/201), [tiliado/nuvolaplayer#45](https://github.com/tiliado/nuvolaplayer/issues/45)
  * Add missing `-a/--app-id` command-line argument to the `--help` screen. Issue: [tiliado/nuvolaplayer#147](https://github.com/tiliado/nuvolaplayer/issues/147) 
  * MPRIS implementation of CanPlay and CanPause flags has been fixed. Issue: [tiliado/nuvolaplayer#224](https://github.com/tiliado/nuvolaplayer/issues/224)
  * Warnings when Notifications is being disabled has been removed. Issue: [tiliado/nuvolaplayer#227](https://github.com/tiliado/nuvolaplayer/issues/227)
  * Don't use notifications API if disabled as it produces critical warnings. Issue: [tiliado/nuvolaplayer#227](https://github.com/tiliado/nuvolaplayer/issues/227)
  * Set GDK_BACKEND to x11 not to crash under Wayland. Issue: [tiliado/nuvolaplayer#181](https://github.com/tiliado/nuvolaplayer/issues/181)
  * Disable compositing mode in WebKitGTK < 2.13.4 as it may crash some websites. Issue: [tiliado/nuvolaplayer#245](https://github.com/tiliado/nuvolaplayer/issues/245)

### News for Script Maintainers:

  * Web app integration template has been moved to [its own repository](https://github.com/tiliado/nuvola-app-template).
  * Added information about Format Requirements Flags. Issue: [tiliado/nuvolaplayer#158](https://github.com/tiliado/nuvolaplayer/issues/158)
  * `Nuvola.VERSION` property contains Nuvola version encoded as single integer, e.g. e.g. 30105 for 3.1.5.
  * `Nuvola.API_VERSION` property contains Nuvola API version encoded as single integer, e.g. e.g. 301 for 3.1.
  * `Nuvola.WEBKITGTK_{VERSION,MAJOR,MINOR,MICRO}` properties contain version information about WebKitGTK+ library.
  * `Nuvola.LIBSOUP_{VERSION,MAJOR,MINOR,MICRO}` properties contain version information about Soup library.
  * New API to set rating.
  * It is possible to set a user agent string via the `user_agent` field of metadata.json. Issue: [tiliado/nuvolaplayer#91](https://github.com/tiliado/nuvolaplayer/issues/91)
  * It is possible to enable access to insecure content. This happens when a web page loaded over HTTPS protocol loads any content over HTTP protocol.
  * Developer documentation and guidelines have been updated.
  
### Changes in Dependencies

  * Increased: WebKitGTK >= 2.6.2, Valac >= 0.26.1, GLib >= 2.42.1 and GTK+ >= 3.14.5.
  * New: libuuid and libnm-(util/glib)

Install Nuvola
==============

Nuvola project provides **cross-distribution flatpak packages** of Nuvola 4, which contain all
requires dependencies. In order to install a particular Nuvola app, follow steps in the
[Nuvola Apps Repository Index](https://nuvola.tiliado.eu/) portal according to your distribution:

  * [Ubuntu 16.04 Xenial Xerus](https://nuvola.tiliado.eu/#!index!ubuntu!xenial)
  * [Ubuntu 16.10 Yakkety Yak](https://nuvola.tiliado.eu/#!index!ubuntu!yakkety)
  * [Ubuntu 17.04 Zesty Zapus](https://nuvola.tiliado.eu/#!index!ubuntu!zesty)
  * [elementaryOS 0.4 Loki](https://nuvola.tiliado.eu/#!index!elementary!loki)
  * [Debian 8 Jessie (oldstable)](https://nuvola.tiliado.eu/#!index!debian!jessie)
  * [Debian 9 Stretch (stable)](https://nuvola.tiliado.eu/#!index!debian!stretch)
  * [Debian 10 Buster (testing)](https://nuvola.tiliado.eu/#!index!debian!buster)
  * [Debian Sid (unstable)](https://nuvola.tiliado.eu/#!index!debian!sid)
  * [Fedora 26](https://nuvola.tiliado.eu/#!index!fedora!fc26)
  * [Fedora 25](https://nuvola.tiliado.eu/#!index!fedora!fc25)
  * [Fedora 24](https://nuvola.tiliado.eu/#!index!fedora!fc24)
  * [Arch Linux](https://nuvola.tiliado.eu/#!index!archlinux)
  * [Other linux](https://nuvola.tiliado.eu/#!index!other)


[TOC]
