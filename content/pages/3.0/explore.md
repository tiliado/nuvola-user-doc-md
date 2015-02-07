Title: Explore Nuvola Player 3.0 Beta
Image: images/3.0/unity/orig/unity_google_play_music_launcher_star_rating.png
Description: Nuvola Player 3.0 will be the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.


Install
=======

<table class="badges">
<tr>
<td><a title="Install Nuvola Player" href="./install.html"><img src="../images/nuvola-logos/install_vertical_2.png" height="108" /></a></td>
<td><a title="Install Nuvola Player in Ubuntu" href="./install.html#ubuntu"><img src="../images/dist-logos/ubuntu_vertical.png" height="108" /></a></td>
<td><a title="Install Nuvola Player in Fedora" href="./install.html#fedora"><img src="../images/dist-logos/fedora_vertical.png" height="108" /></a></td>
<!--<td><a title="Install Nuvola Player in Debian" href="./install.html#debian"><img src="../images/dist-logos/debian_vertical.png" height="108" /></a></td>-->
</tr>
</table>

What's New {: #news}
==========

**Have you upgraded from Nuvola Player 2?** Take a look at following changes!

New Codebase
------------

**Nuvola Player 3 is a new code-base written from scratch**:

 * Ported to the **second generation of the WebKit2Gtk+** web rendering library that doesn't suffer from
   Flash plugin compatibility issues (see section bellow).
 * Removed calls of deprecated functions.
 * Dropped a heavy bag of backward compatibility with old distributions that limits potential of the application.
 * Use of **modern widgets and technologies** (e.g. header bar and client side decorations in GNOME).
 * New more **powerful and flexible JavaScript API** for service integration scripts.
 * The runtime is more generic than Nuvola Player 2, so the fourth generation will be probably
   called **Nuvola Apps 4** (competitor of Unity web Apps?) and used not only for music streaming services. 

Tiliado Repository
------------------

While Nuvola Player 2 packages are hosted at Launchpad PPA, Nuvola Player 3 packages are maintained
in a custom repository.

 * **Debian** and **Ubuntu packages** are now in one place. Moreover, there are packages for **Fedora**.
 * It is possible to continue **support of releases abandoned by Canonical** after the short nine-month
   support window and their removal from Launchpad PPA build machines. 
 * Tiliado Repository Installer makes installation of Nuvola Player easier and without a terminal.
 * Packages won't get stuck in a Launchpad build queue.

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
---------------------

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

Other changes
-------------

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

User Experience {: #user-experience}
===============

**Goal of Nuvola Player is to provide better user experience and desktop integration than common web
browsers can offer.**

Unity {: #explore-unity}
-----

### First Launch ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Ubuntu button in the top left corner to open Unity Dash." href="../images/3.0/unity/orig/unity_open_dash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_open_dash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Nuvola Player 3." href="../images/3.0/unity/orig/unity_dash_nuvola.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Just in case you wonder which version you have installed." href="../images/3.0/unity/orig/unity_nuvola_selector_about.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvola_selector_about.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Nuvola Player 3 services selector window. Launch Grooveshark, for example." href="../images/3.0/unity/orig/unity_nuvola_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvola_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Who is the maintainer of this integration script?" href="../images/3.0/unity/orig/unity_grooveshark_appmenu_about.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_appmenu_about.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Grooveshark script is maintained by the main Nuvola Player developer, but other integration scripts can be maintained by independent developers who are properly acknowledged." href="../images/3.0/unity/orig/unity_grooveshark_about_dialog.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_about_dialog.png" width="256" height="192" /></a></li>
</ul>
</div>

### Unity Dash ###
<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Ubuntu button in the top left corner to open Unity Dash." href="../images/3.0/unity/orig/unity_open_dash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_open_dash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="First, you can launch only the Nuvola Player 3 services selector." href="../images/3.0/unity/orig/unity_dash_nuvola.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="However, after the first launch of a particular service integration script, you can launch it again directly from the dash." href="../images/3.0/unity/orig/unity_dash_grooveshark.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_grooveshark.png" width="256" height="192" /></a></li>
</ul>
</div>

### Pin to Unity Launcher ###

For a quick access to your favorite streaming services, you can pin them on Unity Launcher.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Launch your favorite service from Nuvola Player 3 services selector window. Grooveshark, for example." href="../images/3.0/unity/orig/unity_nuvola_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvola_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Right-click Grooveshark badge in the Unity Launcher and select Lock to Launcher." href="../images/3.0/unity/orig/unity_grooveshark_lock_to_launcher.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_lock_to_launcher.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can, of course, pin all services ;-)" href="../images/3.0/unity/orig/unity_launcher_multiple_pinned.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_launcher_multiple_pinned.png" width="256" height="192" /></a></li>
</ul>
</div>

### Be Quick with Quick List ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="All integration scripts provide basic playback actions: Play/pause, previous song and next song." href="../images/3.0/new/orig/unity_grooveshark_quicklist.png" class="thumbnail"><img src="../images/3.0/new/small/unity_grooveshark_quicklist.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Some integration scripts provide extra actions such as star rating in Google Play Music." href="../images/3.0/unity/orig/unity_google_play_music_launcher_star_rating.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Rating done. This feature is useful when the Google Play Window is hidden or covered by other windows." href="../images/3.0/unity/orig/unity_google_play_music_launcher_star_rating_done.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating_done.png" width="256" height="192" /></a></li>
</ul>
</div>

### Became Keyboard Master ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click gear icon and select Keyboard shortcuts from the menu" href="../images/3.0/new/orig/unity_grooveshark_appmenu_keyboard_shortcuts.png" class="thumbnail"><img src="../images/3.0/new/small/unity_grooveshark_appmenu_keyboard_shortcuts.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can define both in-app and global keyboard shortcuts." href="../images/3.0/unity/orig/unity_grooveshark_keyboard_shortcuts.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_keyboard_shortcuts.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Moreover, Nuvola Player automatically handles multimedia keys on your keyboard." href="../images/3.0/unity/orig/unity_media_keys.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_media_keys.png" width="256" height="192" /></a></li>
</ul>
</div>

### Head-Up Display ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Pres Alt key to show Unity Head-Up display" href="../images/3.0/unity/orig/unity_grooveshark_hud.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_hud.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Type any command" href="../images/3.0/unity/orig/unity_grooveshark_hud_toggle_play.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_hud_toggle_play.png" width="256" height="192" /></a></li>
</ul>
</div>

### Play in Background with Notifications ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click gear icon and select Preferences from the menu" href="../images/3.0/new/orig/unity_grooveshark_appmenu_preferences.png" class="thumbnail"><img src="../images/3.0/new/small/unity_grooveshark_appmenu_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Enable background playback" href="../images/3.0/new/orig/unity_grooveshark_preferences.png" class="thumbnail"><img src="../images/3.0/new/small/unity_grooveshark_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Now you don't have to worry about closing the window accidentally. Playback continues in background." href="../images/3.0/unity/orig/unity_grooveshark_close.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_close.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You'll get notifications on track change." href="../images/3.0/unity/orig/unity_grooveshark_notification.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_notification.png" width="256" height="192" /></a></li>
</ul>
</div>

### Unity Sound Indicator ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Close the window while music is playing. Playback continues in background." href="../images/3.0/unity/orig/unity_grooveshark_close.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_close.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can control playback from the Unity Sound Indicator" href="../images/3.0/unity/orig/unity_grooveshark_sound_menu.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_sound_menu.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can also display the main window from the Unity Sound Indicator" href="../images/3.0/unity/orig/unity_grooveshark_open_from_sound_menu.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_open_from_sound_menu.png" width="256" height="192" /></a></li>
</ul>
</div>



GNOME {: #explore-gnome}
-----


### First Launch ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview." href="../images/3.0/gnome/orig/fedora_flash_install_done_activities.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_done_activities.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Nuvola Player 3." href="../images/3.0/gnome/orig/gnome_activities_nuvola.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_activities_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Just in case you wonder which version you have installed." href="../images/3.0/new/orig/gnome_nuvola_appmenu_about.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_nuvola_appmenu_about.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Just in case you wonder which version you have installed." href="../images/3.0/new/orig/gnome_nuvola_about_dialog.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_nuvola_about_dialog.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Nuvola Player 3 services selector window. Launch Grooveshark, for example." href="../images/3.0/gnome/orig/gnome_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Who is the maintainer of this integration script?" href="../images/3.0/new/orig/gnome_grooveshark_appmenu_about.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_appmenu_about.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Grooveshark script is maintained by the main Nuvola Player developer, but other integration scripts can be maintained by independent developers who are properly acknowledged." href="../images/3.0/gnome/orig/gnome_grooveshark_about_dialog.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_about_dialog.png" width="256" height="192" /></a></li>
</ul>
</div>

### GNOME Dash ###
<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview." href="../images/3.0/gnome/orig/fedora_flash_install_done_activities.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_done_activities.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="First, you can launch only the Nuvola Player 3 services selector." href="../images/3.0/gnome/orig/gnome_activities_nuvola.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_activities_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="However, after the first launch of a particular service integration script, you can launch it again directly from the dash." href="../images/3.0/gnome/orig/fedora_flash_install_relaunch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_relaunch_grooveshark.png" width="256" height="192" /></a></li>
</ul>
</div>

### Dark or Light Theme? ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click application icon and select Preferences from the menu" href="../images/3.0/gnome/orig/gnome_grooveshark_appmenu_preferences.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_appmenu_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="check &quot;Prefer dark theme&quit; if you want to." href="../images/3.0/gnome/orig/gnome_grooveshark_preferences.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Grooveshark looks better with dark window decorations." href="../images/3.0/new/orig/gnome_grooveshark_dark.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_dark.png" width="256" height="192" /></a></li>
</ul>
</div>

### Add to Favorites ###

For a quick access to your favorite streaming services, you can pin them on Unity Launcher.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Launch your favorite service from Nuvola Player 3 services selector window. Grooveshark, for example." href="../images/3.0/gnome/orig/gnome_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Right-click Grooveshark badge in the GNOME Dash and select Add to favorites." href="../images/3.0/new/orig/gnome_grooveshark_add_to_favorites.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_add_to_favorites.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can, of course, pin all services ;-)" href="../images/3.0/new/orig/gnome_many_favorites.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_many_favorites.png" width="256" height="192" /></a></li>
</ul>
</div>

### Became Keyboard Master ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click application icon and select Keyboard shortcuts from the menu" href="../images/3.0/gnome/orig/gnome_grooveshark_appmenu_keyboard_shortcuts.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_appmenu_keyboard_shortcuts.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can define both in-app and global keyboard shortcuts." href="../images/3.0/gnome/orig/gnome_grooveshark_keyboard_shortcuts.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_keyboard_shortcuts.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Moreover, Nuvola Player automatically handles multimedia keys on your keyboard." href="../images/3.0/new/orig/gnome_media_keys.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_media_keys.png" width="256" height="192" /></a></li>
</ul>
</div>



### Play in Background with Notifications ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Enable background playback if you want to." href="../images/3.0/gnome/orig/gnome_grooveshark_preferences.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a  title="Now you don't have to worry about closing the window accidentally. Playback continues in background." href="../images/3.0/new/orig/gnome_grooveshark_close.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_close.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You'll get notifications on track change." href="../images/3.0/gnome/orig/gnome_notification_small.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_notification_small.png" width="256" height="192" /></a></li>
</ul>
</div>

### Notifications with Playback Controls###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Hover mouse over small notification and you will get expanded notification with playback controls." href="../images/3.0/gnome/orig/gnome_notification_expanded.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_notification_expanded.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can also display notification from the GNOME messaging area (key Super+M)." href="../images/3.0/gnome/orig/gnome_notification_messaging_area.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_notification_messaging_area.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="How about playback controls on lock screen?" href="../images/3.0/gnome/orig/gnome_lock_screen_controls.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_lock_screen_controls.png" width="256" height="192" /></a></li>
</ul>
</div>

### Extension of the Day: Media Player Indicator ###

Take a look at [Media Player Indicator](https://extensions.gnome.org/extension/55/media-player-indicator/)
GNOME Shell extension.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Search for Media Player Indicator in GNOME Extensions website." href="../images/3.0/gnome/orig/gnome_mpris_extension_web_page.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_web_page.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Turn the extension on." href="../images/3.0/gnome/orig/gnome_mpris_extension_turn_on.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_turn_on.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Confirm installation." href="../images/3.0/gnome/orig/gnome_mpris_extension_install.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_install.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Reload the web page." href="../images/3.0/gnome/orig/gnome_mpris_extension_reload.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_reload.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Open preferences." href="../images/3.0/gnome/orig/gnome_mpris_extension_open_preferences.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_open_preferences.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Change position of the indicator, if you want to." href="../images/3.0/gnome/orig/gnome_mpris_extension_preferences_right.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_mpris_extension_preferences_right.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Close the window while music is playing. Playback continues in background." href="../images/3.0/new/orig/gnome_grooveshark_close.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_close.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can control playback from the Media Player Indicator." href="../images/3.0/new/orig/gnome_grooveshark_mpris_pause.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_mpris_pause.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You can also display the hidden main window from the Media Player Indicator" href="../images/3.0/new/orig/gnome_grooveshark_mpris_raise.png" class="thumbnail"><img src="../images/3.0/new/small/gnome_grooveshark_mpris_raise.png" width="256" height="192" /></a></li>
</ul>
</div>


Terminal & Scripts {: #explore-terminal}
------------------

### Command-line Controller ###

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Nuvola Player comes with command-line controller for your scripts" href="../images/3.0/unity/orig/unity_nuvolactl_help.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvolactl_help.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Get track info, pause playback, ..." href="../images/3.0/unity/orig/unity_nuvolactl_track_info.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvolactl_track_info.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="How about controlling three Nuvola Player instances?" href="../images/3.0/unity/orig/unity_nuvolactl_multiple_apps.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvolactl_multiple_apps.png" width="256" height="192" /></a></li>
</ul>
</div>


<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
</ul>
</div>

[TOC]
