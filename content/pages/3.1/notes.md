Title: Nuvola Player 3.1 Release Notes
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.1 is the second series of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration
    with Linux desktop environments than usual web browsers can offer. Nuvola Players handles
    multimedia keys, shows desktop notifications, integrates with various sound indicators, media
    player applets, GNOME lock screen and launchers and more.

!!! warning "Rolling Releases are for Patrons"
    Rolling Releases are provided for patrons as a benefit for their support. You will need to
    enter credentials of your Tiliado account with active
    [Nuvola Patron membership](https://tiliado.eu/nuvolaplayer/funding/)
    to access these builds.

Nuvola Player 3.1 was forked from release 3.0 on December 30, 2015 and many changes under the hood 
have been made and many new features & enhancements have been added since then. 
    
About Nuvola Player
===================

**Nuvola Player** is a runtime for web-based music streaming services providing more native user
experience and integration with Linux desktop environments than usual web browsers can offer. It
tries to feel and look like a native application as possible. However, it cannot overcome common
drawbacks of web-based music streaming: some music streaming services require Flash plugin and web
apps usually have higher memory usage than native apps.

What's New
==========

Nuvola Player 3.1 is constantly evolving, to **stay in touch**

 * Follow Nuvola Player on [Facebook](https://www.facebook.com/nuvolaplayer),
    [Google+](https://plus.google.com/110794636546911932554) or
    [Twitter](https://twitter.com/NuvolaPlayer).
  * Subscribe to the Nuvola Player Newsletter: [weekly](http://eepurl.com/bLbm5H)
    or [monthly](http://eepurl.com/bLbtM1).


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


Install Nuvola Player
=====================

<div class="row">
  <div class="col-sm-12 col-md-6">
    <div class="thumbnail">
      <a title="Install Nuvola Player in Ubuntu" href=":3.1/install.html#ubuntu"><img src="./images/dist-logos/ubuntu_vertical.png" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" title="Install Nuvola Player in Ubuntu" href=":3.1/install.html#ubuntu">Ubuntu</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-6">
    <div class="thumbnail">
      <a title="Install Nuvola Player in Fedora" href=":3.1/install.html#fedora"><img src="./images/dist-logos/fedora_vertical.png" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" title="Install Nuvola Player in Fedora" href=":3.1/install.html#fedora">Fedora</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-6">
    <div class="thumbnail">
      <a title="Install Nuvola Player in Debian" href=":3.1/install.html#debian"><img src="./images/dist-logos/debian_vertical.png" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" title="Install Nuvola Player in Debian" href=":3.1/install.html#debian">Debian</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-6">
    <div class="thumbnail">
      <a title="Install Nuvola Player" href=":3.1/install.html#other-linux"><img src="./images/nuvola-logos/install_vertical_3.png" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" title="Install Nuvola Player" href=":3.1/install.html#other-linux">Other Linux</a>
      </div>
    </div>
  </div>
</div>

Nuvola Player 3 project officially supports and provides packages for
[Ubuntu](:3.1/install.html#ubuntu) 15.04, 15.10, 16.04 and 16.10,
[Fedora](:3.1/install.html#fedora) 23-24 and
[Debian](:3.1/install.html#debian) Jessie, Stretch and Sid. The Nuvola Player
developer has tested installation and functionality in clean virtualized instances of these
distributions and can assure reasonable user support in case of problems.

However, Nuvola Player should also work on
[other modern Linux distributions](:3.1/install.html#other-linux), but user experience might
not be optimal (e.g. inconsistent look and behavior) and quality of user support depends on
complexity of an issue.


[TOC]
