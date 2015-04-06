Title: Nuvola Player 3.0 Release Notes
Image: images/3.0/unity/orig/unity_google_play_music_launcher_star_rating.png
Description: Nuvola Player 3.0 will be the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.


Nuvola Player 3.0 is currently in development. [Beta builds]({filename}./install.md) are available since February 8th, 2015.

About Nuvola Player
===================

**Nuvola Player** is a runtime for web-based music streaming services providing more native user experience and integration with Linux desktop environments
than usual web browsers can offer. It tries to feel and look like a native application as possible. However, it cannot overcome 
common drawbacks of web-based music streaming: some music streaming services require Flash plugin and web apps usually have higher memory usage than native apps.

What's New {: #news}
==========

Nuvola Player 3 has been rewritten from scratch and contains plenty of improvements over Nuvola Player 2.

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
    of 32bit libraries on you 64bit system to be able to run 32bit Flash plugin. Yes, this is insane.

  * Memory usage is higher and performance is lower.

  * Wrapped Flash plugin is less stable, it often crashes and takes down whole Nuvola Player
    2 application.

**Nuvola Player 3 doesn't need any hacks to support Flash plugin**, because it is built on top of
WebKit2Gtk+, the second generation of this web rendering library.
The major diference is that plugins are run in a separate GTK+ 2 compatible process, so there is no
need to use nspluginwrapper and install 32bit libraries on 64bit system. There is also one extra
benefit: If Flash plugin crashes, it doesn't take down whole Nuvola Player application.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Nuvola Player 2 requires a plenty of 32bit libraries on 64bit system because of Flash plugin compatibility hack." href="../images/3.0/new/orig/nuvola_player_2_flash_deps.png" class="thumbnail"><img src="../images/3.0/new/small/nuvola_player_2_flash_deps.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Nuvola Player 3 doesn't suffer from Flash plugin incompatibility issue ." href="../images/3.0/new/orig/nuvola_player_3_flash_deps.png" class="thumbnail"><img src="../images/3.0/new/small/nuvola_player_3_flash_deps.png" width="256" height="192" /></a></li>
</ul>
</div>

Independent Instances
--------------------------

It was possible to have only one instance of **Nuvola Player 2** shared by all streaming services
and switch between them. In **Nuvola Player 3**, it's possible to run multiple services side-by-side
([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1007185)).
The services selector launches new instance for each service and creates a desktop application
shortcut ([feature request](https://bugs.launchpad.net/nuvola-player/+bug/1211351))
when a particular service starts. As a result, you can than pin it to the Unity Launcher or
GNOME Activities dock and launch it directly in the future.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Multiple services pinned to Unity Launcher." href="../images/3.0/unity/orig/unity_launcher_multiple_pinned.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_launcher_multiple_pinned.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Multiple services pinned to GNOME Activities dock." href="../images/3.0/new/orig/gnome_many_favorites.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_many_favorites.png" width="256" height="192" /></a></li>
</ul>
</div>


Tiliado Repository
--------------------------

While Nuvola Player 2 repository provides packages only for Ubuntu and Debian, Nuvola Player 3 brings official
support and packages also for Fedora 20 and 21. As I have received many complains that installation of Nuvola Player
2 is not easy enough for less experienced users, I've created a graphical installer specially designed for them.
However, power users can of course still add Nuvola Player repository to software sources manually using terminal
kung-fu. The graphical installer is pretty handy though and I always use it when I test Nuvola Player in clean
systems in VirtualBox ;-)

Since I dislike the short nine-month support window of interim Ubuntu releases and their consecutive removal from
Launchpad build machines, I decided to abandon Launchpad and host APT repository on my server like I did so with
the repository for Debian. A side benefit is that packages won't get stuck in Launchpad build queue. In addition,
RPM packages for Fedora are also hosted on this server, all in one place.

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

Nuvola Player 3 currently ships with five services: **Google Play Music** (Jiří Janoušek), **Grooveshark** (Jiří Janoušek),
**Deezer** (Jiří Janoušek), **Jango** (Stefano Bagnatica) and **This is My Jam** (Jan Vlnas). Six more services are in preparation
and will be added to the repository when finished: **8tracks** (Jiří Janoušek), **Rdio** (Aaron Cripps),
**Bandcamp** (Jiří Janoušek), **Spotify** (Michael Nye), **KEXP Live Stream** (Michael Nye)
and **Synology Audio Station** (Daniel Schep).

Unfortunately, five streaming services available in Nuvola Player 2 are currently unmaintained as a previous
maintainer has lost interest in them: **Grooveshark Mobile, Hype Machine, Amazon Cloud Player, Pandora and Logitech
Media Server**. These services might disappear from the Nuvola Player project unless a new maintainer is found.
I could adopt Grooveshark Mobile and Hype Machine scripts, but I'm not so sure about Amazon Cloud Player, Pandora
and Logitech Media Server scripts as I don't live in supported country or don't have required hardware.

Missing Features
================

Since I don't want to postpone release of Nuvola Player 3 again and again, I've decided not to implement some
features available in Nuvola Player 2 for now. As a result, following features are missing in Nuvola Player 3 and might
be added later upon demand from users: Libre.fm scrobbling, lyrics fetching, translations, per-service network
proxy settings, and file downloads. 

Limited Support
===============

Nuvola Player 3 project officially supports and provides packages for [Ubuntu]({filename}./install.md#ubuntu) 14.10-15.04,
[Fedora]({filename}./install.md#fedora) 20-21 and [Debian]({filename}./install.md#debian)
Jessie and Sid. The Nuvola Player developer has tested installation and functionality in clean virtualized instances
of these distributions and can assure reasonable user support in case of problems.

However, Nuvola Player should also work on [other modern Linux distributions]({filename}./install.md#other-linux), but user experience might
not be optimal (e.g. inconsistent look and behavior) and quality of user support depends on complexity of an issue.

Project Funding
===============

My work on Nuvola Player is [funded by Nuvola Patrons](https://tiliado.eu/nuvolaplayer/funding/). My dream is to work
as an independent developer on open source software for all people around the world, software for you. 
If you like Nuvola Player, or even use it every day, you can
[show your gratitude by supporting the project](https://tiliado.eu/nuvolaplayer/funding/).

Thank you and happy listening!

Jiří Janoušek


[TOC]
