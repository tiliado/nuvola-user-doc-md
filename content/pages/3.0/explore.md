Title: Explore Nuvola Player 3.0 Beta
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.0 will be the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.



Goal of Nuvola Player is to provide better user experience and desktop integration than common web
browsers can offer.

Unity {: #explore-unity}
=====

## First Launch ##

Let's launch Nuvola Player from Unity Dash. As you can see, you have all supported streaming services in one place,
no need to look for them in your browser's bookmarks or to remember and type in address of a service.

 Gallery
+[Click Ubuntu button in the top left corner to open Unity Dash.](images/3.0/unity/unity_open_dash.png|256x192)
+[Launch Nuvola Player 3.](images/3.0/unity/unity_dash_nuvola.png|256x192)
+[Just in case you wonder which version you have installed.](images/3.0/unity/unity_nuvola_selector_about.png|256x192)
+[Nuvola Player 3 services selector window. Launch any streaming service.](images/3.0/unity/unity_nuvola_selector_launch_deezer.png|256x192)
+[Who is the maintainer of this integration script?](images/3.0/unity/unity_deezer_gear_menu_about.png|256x192)
+[Deezer script is maintained by the main Nuvola Player developer, but other integration scripts can be maintained by independent developers who are properly acknowledged.](images/3.0/unity/unity_deezer_about_dialog.png|256x192)

## Create/Remove Application Launchers

Nuvola Player automatically creates an application launcher when a particular streaming service is
launched. It also allows you to create all launchers at once 
(*Gear Menu → Create application launchers*) or to remove unnecessary launchers
(*Gear Menu → Remove application launchers*). However, the launcher of a currently running streaming
service cannot be removed.

 Gallery
+[Gear Menu → Create application launchers](images/3.0/app_launchers/unity_create_app_launchers.png|256x192)
+[Application launchers have been created](images/3.0/app_launchers/unity_app_launchers_created.png|256x192)
+[Gear Menu → Remove application launchers](images/3.0/app_launchers/unity_delete_app_launchers.png|256x192)
+[Application launchers have been deleted](images/3.0/app_launchers/unity_app_launchers_deleted.png|256x192)

!!! info "Preserve your custom launchers"
    Nuvola Player keeps launchers updated every time a particular streaming service is launched. If you
    want to modify the launchers on your own and prevent Nuvola Player from overwriting your changes,
    mark the launcher as read-only in a file browser or from a terminal. The launchers are located in
    a directory `~/.local/share/applications` where `~` represents your home directory.

## Unity Dash ##

Nuvola Player neatly integrates with Unity Dash. Once a particular music streaming service is launched for the first time,
a desktop launcher is created in the background. You can then get to your favorite music faster, just start typing its name
in Unity Dash screen. Can do this your web browser?

 Gallery
+[Click Ubuntu button in the top left corner to open Unity Dash.](images/3.0/unity/unity_open_dash.png|256x192)
+[First, you can launch only the Nuvola Player 3 services selector.](images/3.0/unity/unity_dash_nuvola.png|256x192)
+[However, after the first launch of a particular service integration script, you can launch it again directly from the dash.](images/3.0/unity/unity_dash_deezer.png|256x192)

## Pin to Unity Launcher ##

For even faster access to your music, you can pin our favorite music streaming services to Unity Launcher. One click
to launch it again!

 Gallery
+[Launch your favorite service from Nuvola Player 3 services selector window. ](images/3.0/unity/unity_nuvola_selector_launch_deezer.png|256x192)
+[Right-click Grooveshark badge in the Unity Launcher and select Lock to Launcher.](images/3.0/unity/unity_deezer_lock_to_launcher.png|256x192)
+[You can, of course, pin all services ;-)](images/3.0/unity/unity_launcher_multiple_pinned.png|256x192)

## Be Quick with Quick List ##

Nuvola Player integrates with Unity Launcher quick list and adds playback actions. In addition, some screaming services
provide other actions like star rating.

 Gallery
+[All integration scripts provide basic playback actions: Play/pause, previous song and next song.](images/3.0/unity/unity_deezer_quick_list.png|256x192)
+[Some integration scripts provide extra actions such as thumbs up/down in Google Play Music.](images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png|256x192)
+[Rating done. This feature is useful when the Google Play Window is hidden or covered by other windows.](images/3.0/unity/unity_google_play_music_launcher_thumbs_up_done.png|256x192)

## Became Keyboard Master ##

Nuvola Player allows you to change keyboard shortcuts or to add your own. Another killer feature is ability to handle
special multimedia keys.

 Gallery
+[Click gear icon and select Preferences from the menu](images/3.0/unity/unity_gear_menu_preferences.png|256x192)
+[You can define both in-app and global keyboard shortcuts.](images/3.0/unity/unity_keyboard_shortcuts.png|256x192)
+[Moreover, Nuvola Player automatically handles multimedia keys on your keyboard.](images/3.0/unity/unity_media_keys.png|256x192)

## Head-Up Display ##

Unity's unique feature, Head-up display, is also supported. Just press Alt key and then start typing an action.

 Gallery
+[Pres Alt key to show Unity Head-Up display](images/3.0/unity/unity_hud_type_command.png|256x192)
+[Type any command](images/3.0/unity/unity_hud_thumbs_up.png|256x192)

## Play in Background with Notifications ##

With Nuvola Player, you will never accidentally close your web browser while music is playing. If you close
Nuvola Player window, it keeps playing in background and you will get notifications on track changes.
Simple and extremely useful.

 Gallery
+[Click gear icon and select Preferences from the menu](images/3.0/unity/unity_gear_menu_preferences.png|256x192)
+[Enable background playback](images/3.0/unity/unity_preferences.png|256x192)
+[Now you don't have to worry about closing the window accidentally. Playback continues in background.](images/3.0/unity/unity_deezer_close.png|256x192)
+[You'll get notifications on track change.](images/3.0/unity/unity_track_change_notification.png|256x192)

## Unity Sound Indicator ##


I hope you are not surprised that Nuvola Player also integrates with Unity sound indicator. You can control playback
or show the main window if hidden.

 Gallery
+[Close the window while music is playing. Playback continues in background.](images/3.0/unity/unity_deezer_close.png|256x192)
+[You can control playback from the Unity Sound Indicator](images/3.0/unity/unity_deezer_sound_menu.png|256x192)
+[You can also display the main window from the Unity Sound Indicator](images/3.0/unity/unity_deezer_open_from_sound_menu.png|256x192)

## Other features ##

To enable, disable or configure **other built-in features**, see [Common Features section bellow](#explore-common).


GNOME {: #explore-gnome}
=====

## First Launch ##

Let's launch Nuvola Player from GNOME Activities screen. As you can see, you have all supported streaming services
in one place, no need to look for them in your browser's bookmarks or to remember and type in address of a service.

 Gallery
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/fedora_open_activities.png|256x192)
+[Launch Nuvola Player 3.](images/3.0/gnome/gnome_activities_nuvola.png|256x192)
+[Just in case you wonder which version you have installed.](images/3.0/gnome/gnome_nuvola_appmenu_about.png|256x192)
+[Just in case you wonder which version you have installed.](images/3.0/gnome/gnome_nuvola_about_dialog.png|256x192)
+[Nuvola Player 3 services selector window. Launch Grooveshark, for example.](images/3.0/gnome/gnome_selector_launch_grooveshark.png|256x192)
+[Who is the maintainer of this integration script?](images/3.0/gnome/gnome_grooveshark_appmenu_about.png|256x192)
+[Grooveshark script is maintained by the main Nuvola Player developer, but other integration scripts can be maintained by independent developers who are properly acknowledged.](images/3.0/gnome/gnome_grooveshark_about_dialog.png|256x192)


## Create/Remove Application Launchers

Nuvola Player automatically creates an application launcher when a particular streaming service is
launched. It also allows you to create all launchers at once 
(*App Menu → Create application launchers*) or to remove unnecessary launchers
(*App Menu → Remove application launchers*). However, the launcher of a currently running streaming
service cannot be removed.

 Gallery
+[App Menu → Create application launchers](images/3.0/app_launchers/gnome_create_app_launchers.png|256x192)
+[Application launchers have been created](images/3.0/app_launchers/gnome_app_launchers_created.png|256x192)
+[App Menu → Remove application launchers](images/3.0/app_launchers/gnome_delete_app_launchers.png|256x192)
+[Application launchers have been deleted](images/3.0/app_launchers/gnome_app_launchers_deleted.png|256x192)

!!! info "Preserve your custom launchers"
    Nuvola Player keeps launchers updated every time a particular streaming service is launched. If you
    want to modify the launchers on your own and prevent Nuvola Player from overwriting your changes,
    mark the launcher as read-only in a file browser or from a terminal. The launchers are located in
    a directory `~/.local/share/applications` where `~` represents your home directory.

## GNOME Dash ##

Nuvola Player neatly integrates with list of applications in GNOME Activities screen. Once a particular music
streaming service is launched for the first time, a desktop launcher is created in the background. You can then get
to your favorite music faster, just start typing its name in GNOME Activities screen. Can do this your web browser?

 Gallery
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/fedora_open_activities.png|256x192)
+[First, you can launch only the Nuvola Player 3 services selector.](images/3.0/gnome/gnome_activities_nuvola.png|256x192)
+[However, after the first launch of a particular service integration script, you can launch it again directly from the dash.](images/3.0/gnome/gnome_activities_deezer.png|256x192)

## Add to Favorites ##

For even faster access to your music, you can add our favourite music streaming services to dock with favourite
applications in GNOME Activities screen. One click to launch it again!

 Gallery
+[Launch your favorite service from Nuvola Player 3 services selector window. Grooveshark, for example.](images/3.0/gnome/gnome_selector_launch_grooveshark.png|256x192)
+[Right-click Grooveshark badge in the GNOME Dash and select Add to favorites.](images/3.0/gnome/gnome_add_to_favorites.png|256x192)
+[You can, of course, pin all services ;-)](images/3.0/gnome/gnome_many_favorites.png|256x192)

## Became Keyboard Master ##

Nuvola Player allows you to change keyboard shortcuts or to add your own. Another killer feature is ability to handle
special multimedia keys.

 Gallery
+[Click application icon and select Preferences from the menu](images/3.0/gnome/gnome_grooveshark_appmenu_preferences.png|256x192)
+[Select tab Keyboard shortcuts and then you can define both in-app and global keyboard shortcuts.](images/3.0/gnome/gnome_grooveshark_keyboard_shortcuts.png|256x192)
+[Moreover, Nuvola Player automatically handles multimedia keys on your keyboard.](images/3.0/new/gnome_media_keys.png|256x192)

## Play in Background with Notifications ##

With Nuvola Player, you will never accidentally close your web browser while music is playing. If you close
Nuvola Player window, it keeps playing in background and you will get notifications on track changes.
Simple and extremely useful.

 Gallery
+[Enable background playback if you want to.](images/3.0/gnome/gnome_grooveshark_preferences.png|256x192)
+[Now you don't have to worry about closing the window accidentally. Playback continues in background.](images/3.0/gnome/gnome_grooveshark_close.png|256x192)
+[You'll get notifications on track change.](images/3.0/gnome/gnome_track_change_notification.png|256x192)

## Notifications with Playback Controls ##

I hope you are not surprised that Nuvola Player also supports rich notifications with playback actions.
You can than control playback even from a lock screen. Note that rich notifications are **no longer
supported in GNOME 3.18**.

 Gallery
+[Hover mouse over small notification and you will get expanded notification with playback controls.](images/3.0/gnome/gnome_notification_expanded.png|256x192)
+[You can also display notification from the GNOME messaging area (key Super+M).](images/3.0/gnome/gnome_notification_messaging_area.png|256x192)
+[How about playback controls on lock screen?](images/3.0/gnome/gnome_lock_screen_controls.png|256x192)

## Media Player Indicator extension ##

Nuvola Player integrates with [Media Player Indicator](https://extensions.gnome.org/extension/55/media-player-indicator/)
GNOME Shell extension. You can control playback or show the main window if hidden.

 Gallery
+[Search for Media Player Indicator in GNOME Extensions website.](images/3.0/gnome/gnome_mpris_extension_web_page.png|256x192)
+[Turn the extension on.](images/3.0/gnome/gnome_mpris_extension_turn_on.png|256x192)
+[Confirm installation.](images/3.0/gnome/gnome_mpris_extension_install.png|256x192)
+[Close the window while music is playing. Playback continues in background.](images/3.0/gnome/gnome_grooveshark_close.png|256x192)
+[You can control playback from the Media Player Indicator.](images/3.0/gnome/gnome_mpris_extension_grooveshark_playing.png|256x192)
+[You can also display the hidden main window from the Media Player Indicator](images/3.0/gnome/gnome_mpris_extension_grooveshark_open.png|256x192)

## Dark or Light Theme? ##

Nuvola Player allows you to set a dark theme. Some streaming services look better that way.

 Gallery
+[Click application icon and select Preferences from the menu](images/3.0/gnome/gnome_grooveshark_appmenu_preferences.png|256x192)
+[Check &quot;Prefer dark theme&quit; if you want to.](images/3.0/gnome/gnome_grooveshark_preferences.png|256x192)
+[Grooveshark looks better with dark window decorations.](images/3.0/gnome/gnome_grooveshark_dark.png|256x192)

## Other features ##

To enable, disable or configure **other built-in features**, see [Common Features section bellow](#explore-common).
 
Terminal & Scripts {: #explore-terminal}
==================

## Command-line Controller ##

Nuvola Player 3 can be also controlled from command line via `nuvolaplayer3ctl`.

 Gallery
+[Nuvola Player comes with command-line controller for your scripts](images/3.0/unity/unity_nuvolactl_help.png|256x192)
+[Get track info, pause playback, ...](images/3.0/unity/unity_nuvolactl_track_info.png|256x192)
+[How about controlling three Nuvola Player instances?](images/3.0/unity/unity_nuvolactl_multiple_apps.png|256x192)

Common Features {: #explore-common}
===============

These featured are not dependent on a particular desktop environment.

## Enable, disable or configure built-in features ##

Nuvola Player allows you enable, disable or configure **many built-in features**:

  * In **Unity**, click *Gear Menu → Preferences*, then switch to tab *Components*.
  * In **GNOME**, click *App Menu → Preferences*, then switch to tab *Components*.

 Gallery
+[Gear Menu → Preferences](images/3.0/unity/unity_gear_menu_preferences.png|256x192)
+[Switch to tab Components](images/3.0/components/unity_webapp_components.png|256x192)
+[App Menu → Preferences](images/3.0/gnome/gnome_grooveshark_appmenu_preferences.png|256x192)
+[Switch to tab Components](images/3.0/components/gnome_webapp_components.png|256x192)

## Last.fm Scrobbling ##

Nuvola Player allows you to scrobble your music taste to [Last.fm](http://www.last.fm) audio scrobbler and music recommendation service.

  * In **Unity**, click *Gear Menu → Preferences*, then switch to tab *Components*, enable *Audio
    Scrobbler Services* and finally connect your Last.fm account.
  * In **GNOME**, click *App Menu → Preferences*, then switch to tab *Components*, enable *Audio
    Scrobbler Services* and finally connect your Last.fm account.

 Gallery
+[Click Configure button at the Last.fm component](images/3.0/lastfm/unity_webapp_components_lasfm.png|256x192)
+[Click Connect button](images/3.0/lastfm/unity_lastfm_authorize.png|256x192)
+[Grant access to Nuvola Player on the Last.fm page that has been opened](images/3.0/lastfm/unity_lastfm_site_authorize.png|256x192)
+[Finish authorization in Nuvola Player](images/3.0/lastfm/unity_lastfm_finish_authorization.png|256x192)
+[Done! Your music taste will be scrobbled.](images/3.0/lastfm/unity_lastfm_authorized.png|256x192)

## Lyrics Fetching ##

Nuvola Player can fetch lyrics from AZLyrics.

  * In **Unity**, click *Gear Menu → Preferences*, switch to tab *Components*, enable *Lyrics*. Then
    click *Gear Menu → Show sidebar* and select *Lyrics* if necessary.
  * In **GNOME**, click *App Menu → Preferences*, switch to tab *Components*, enable *Lyrics*. Then
    click *Gear Menu → Show sidebar* and select *Lyrics* if necessary.

 Gallery
+[Enable Lyrics component](images/3.0/lyrics/unity_webapp_components_lyrics.png|256x192)
+[Enable sidebar](images/3.0/lyrics/unity_gear_show_sidebar.png|256x192)
+[Lyrics is automatically fetched](images/3.0/lyrics/unity_webapp_lyrics.png|256x192)

## Per-Application Network Proxy ##

Each application can have its own network proxy settings.

  * In **Unity**, click *Gear Menu → Preferences* and switch to tab *Network*.
  * In **GNOME**, click *App Menu → Preferences* and switch to tab *Network*.

 Gallery
+[Switch to tab Network](images/3.0/components/unity_webapp_network_proxy.png|256x192)

## Old-style Tray Icons ##

Some desktop environments (e.g. XFCE, LXDE, partially GNOME) still support old-style tray icons.

  * In **GNOME**, click *App Menu → Preferences*, switch to tab *Components* and enable *Tray Icon*.
  * In **other environments**, click *Gear Menu → Preferences*, switch to tab *Components* and
    enable *Tray Icon*. Note that old-style tray icons are **not supported in Ubuntu's Unity**. 

 Gallery
+[Enable tray icon to use it to control playback.](images/3.0/components/gnome_webapp_trayicon.png|256x192)

[TOC]
