Title: Install Nuvola Player 3.0 on Other Linux
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.0 is the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.

Nuvola Player 3 project officially supports and provides packages for
[Ubuntu](./install-ubuntu.html) 16.04-17.04,
[Fedora](./install-fedora.html) 24-25
and [Debian](./install-debian.html) Stretch and Sid.
However, Nuvola Player should also work on other modern Linux distributions, but
user experience might not be optimal (e.g. inconsistent look and behaviour) and quality of user
support depends on complexity of an issue.


Nuvola Player 3 should work also on modern linux distributions which meet minimal requirements listed bellow,
but hasn't been tested here by the developer and support may be limited for that reason.
You can take a look at [a list of unofficial packages](https://github.com/tiliado/nuvolaplayer/wiki/Unofficial)
provided by a community or [build Nuvola Player from source](#build-source).

Build Nuvola Player from Source {: #build-source} 
===============================

Get Source Code
---------------

You can download [a release tarball](https://github.com/tiliado/nuvolaplayer/releases)
or [clone git repository](https://github.com/tiliado/nuvolaplayer/tree/3.0.x).

Install Dependencies
--------------------

  * [Python 2](http://python.org) >= 2.7 (recommended)
    or [Python 3](http://python.org) >= 3.4 (not well tested)
  * [Vala](https://wiki.gnome.org/Projects/Vala) >= 0.22.1
  * [Diorite library](https://github.com/tiliado/diorite)
  * [glib-2.0](https://wiki.gnome.org/Projects/GLib) >= 2.40
  * [gio-2.0](https://wiki.gnome.org/Projects/GLib) >= 2.40
  * [gobject-2.0](https://wiki.gnome.org/Projects/GLib) >= 2.40
  * [gthread-2.0](https://wiki.gnome.org/Projects/GLib) >= 2.40
  * [gtk+-3.0](http://www.gtk.org/) >= 3.10
  * [gdk-3.0](http://www.gtk.org/) >= 3.10
  * [gdk-x11-3.0](http://www.gtk.org/) >= 3.10
  * [x11](http://www.x.org/wiki/) >= 0.5
  * [json-glib-1.0](https://wiki.gnome.org/Projects/JsonGlib) >= 0.7
  * [libarchive](http://www.libarchive.org/) >= 3.1
  * [webkit2gtk-3.0](http://webkitgtk.org/) >= 2.4
  * [javascriptcoregtk-3.0](http://webkitgtk.org/) >= 2.4
  * [libnotify](https://git.gnome.org/browse/libnotify/) >= 0.7
  * optional unity >= 3.0
  * optional dbusmenu-glib-0.4 >= 0.4 

Format Support Issues {: #format-support}
=====================

Streaming services use following technologies for audio playback:

* **Adobe Flash** - you will need a NPAPI based Flash plugin (not PAPI) - see [Flash download page](http://get.adobe.com/flashplayer/)
* **HTML5 Audio with MP3 format** - you will need a functional [GStreamer stack](http://gstreamer.freedesktop.org/modules/)
  with a MP3 decoder. I'd recommend to install modules `gst-plugins-base`, `gst-plugins-good`, `gst-plugins-ugly` and `gst-plugins-bad`.

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

[TOC]
