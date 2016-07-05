Title: Install Nuvola Player 3.0 on Debian
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.0 is the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.

!!! info "Supported Releases"

    The Nuvola Player 3 project officially supports and provides packages for
    Debian Jessie, Stretch and Sid.

Choose Installation Method {: #install}
==========================

There are three ways how to install Nuvola Player on your system. Choose the one which suits you best.

  1. [All-in-one Nuvola Player Bundle](#bundle): A single package that bundles the core application
     as well as integration scripts of streaming services. Upon installation, all components are
     updated independently. **This method is recommended to less experienced users.**
  2. [User-friendly graphical installation](#installer): Users who are not friends with a terminal
     can take advantage of an easy-to-use graphical installer.
     **This method is recommended to less experienced users if installation of the Nuvola Player Bundle fails.**

  3. [Manual installation from terminal](./manual-installation.html):
     Power users who are excellent in command-line kung-fu can just add
     [the Nuvola Player Repository](https://tiliado.eu/nuvolaplayer/repository/) manually and install
     Nuvola Player using common package management tools of your linux distribution. Then skip to the
     section [Check format support](#format-support).
     **This method is not recommended to less experienced users. Any mistake can break your system.**

All-in-one Nuvola Player Bundle {: #bundle}
===============================

 1. Download [All-in-one Nuvola Player Bundle](https://github.com/tiliado/nuvolaplayer/releases/tag/3.0.3).
    Note: Choose correct distribution and architecture (i386 for 32-bit processors and amd64 for 64-bit ones).
 2. Open the bundle package with GDebi package installation tool and install the package.
    If the installation is not successful, try the [User-Friendly Graphical Installation](#installer) procedure
    as it is more robust and can solve conflicts to a certain degree.
 3. [Check format support status](#format-support).

 Gallery
+[Download All-in-one Nuvola Player Bundle](images/3.0/installation/debian/firefox_download_bundle.png|256x192)
+[Open the directory where the bundle has been downloaded](images/3.0/installation/debian/firefox_open_bundle_folder.png|256x192)
+[Open the bundle with GDebi package installation tool](images/3.0/installation/debian/bundle_open_with_gdebi.png|256x192)
+[Install the bundle](images/3.0/installation/debian/gdebi_install_bundle.png|256x192)
+[Enter your password to confirm installation.](images/3.0/installation/debian/gdebi_install_bundle_auth.png|256x192)
+[Close the GDebi package installation tool.](images/3.0/installation/debian/gdebi_bundle_close.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player 3.](images/3.0/gnome/debian_activities_nuvola.png|256x192)
+[Nuvola Player 3 services selector window.](images/3.0/gnome/debian_selector_launch_deezer.png|256x192)

User-Friendly Graphical Installation {: #installer}
====================================

!!! info "Use up-to-date installer"
    
    It is recommended to always download an up-to-date version of the Tiliado Repository Installer.

Install Tiliado Repository Installer 
------------------------------------

 1. Download Tiliado Repository Installer for your
    distribution release and open it with Ubuntu Software Center.
       * [Debian 8 Jessie](https://tiliado.eu/repository-installer/download/jessie/) 
       * [Debian 9 Stretch](https://tiliado.eu/repository-installer/download/stretch/) 
       * [Debian Sid](https://tiliado.eu/repository-installer/download/sid/) 
 2. Open the installer package with GDebi package installation tool and install the package.

 Gallery
+[Download Tiliado Repository Installer](images/3.0/installation/debian/firefox_download_installer.png|256x192)
+[Open the directory where the isntaller has been downloaded](images/3.0/installation/debian/firefox_open_folder.png|256x192)
+[Open the installer with GDebi package installation tool](images/3.0/installation/debian/open_with_gdebi.png|256x192)
+[Install the installer](images/3.0/installation/debian/gdebi_install.png|256x192)
+[Enter your password to confirm installation.](images/3.0/installation/debian/gdebi_install_auth.png|256x192)
+[Close the GDebi package installation tool.](images/3.0/installation/debian/gdebi_close.png|256x192)

Add Nuvola Player Repository
----------------------------

  1. Click **Activities button** in the top left corner to open GNOME Overview.
  2. Launch **Tiliado Repositories** installer.
  3. Use anonymous access or Enter login credentials to your Tiliado account.
  4. Select Nuvola Player repository.
  5. Select repository components you want to install Nuvola Player from.
  6. Select which packages you want to install from the repository.
  7. Review the summary and click **Install** button.
  8. Enter your password to confirm installation.
  9. If installation is successful, click Quit button. Otherwise copy the installation log and
     [contact support](https://github.com/tiliado/tiliado-repositories/issues/new).
 10. Click **Activities button** in the top left corner to open GNOME Overview.
 11. Launch Nuvola Player 3.
 12. You should see Nuvola Player 3 services selector window.

 Gallery
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/debian_open_activities.png|256x192)
+[Launch Tiliado Repositories installer.](images/3.0/installation/debian/activities_tiliado_installer.png|256x192)
+[Use anonymous access or enter login credentials to your Tiliado account.](images/3.0/installation/debian/installer_anonymous.png|256x192)
+[Select Nuvola Player repository.](images/3.0/installation/debian/installer_repositories.png|256x192)
+[Select repository components you want to install Nuvola Player from.](images/3.0/installation/debian/tiliado_installer_components_stable.png|256x192)
+[Select which packages you want to install from the repository.](images/3.0/installation/debian/installer_packages.png|256x192)
+[Review the summary and click Install button.](images/3.0/installation/debian/installer_summary.png|256x192)
+[Enter your password to confirm installation.](images/3.0/installation/debian/installer_install_auth.png|256x192)
+[If installation is successful, click Quit button.](images/3.0/installation/debian/installer_done_quit.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player 3.](images/3.0/gnome/debian_activities_nuvola.png|256x192)
+[Nuvola Player 3 services selector window.](images/3.0/gnome/debian_selector_launch_deezer.png|256x192)

Check Format Support {: #format-support}
====================

!!! info
    
    **Nuvola Player 3 packages for Debian** have both Flash plugin and GStreamer MP3 audio decoder as
    dependencies, so these plugins should work out of the box without any hassles.

 1. Click **Activities button** in the top left corner to open GNOME Overview.
 2. Launch Nuvola Player 3.
 3. You should see Nuvola Player 3 services selector window. Launch any streaming service.
 4. Open App menu and select Format Support.
 5. Tab Web Plugins shows information about available Flash Player plugins.
 6. Tab MP3 format shows information whether GStreamer MP3 Audio encoder has been found. You can
    click button Check again to run a MP3 support test.

 Gallery
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/debian_open_activities.png|256x192)
+[Launch Nuvola Player 3.](images/3.0/gnome/debian_activities_nuvola.png|256x192)
+[Nuvola Player 3 services selector window.](images/3.0/gnome/debian_selector_launch_deezer.png|256x192)
+[Open App menu and select Format Support.](images/3.0/installation/debian/nuvola_appmenu_format_support.png|256x192)
+[Tab Web Plugins shows information about available Flash Player plugins.](images/3.0/installation/debian/format_support_flash.png|256x192)
+[Tab MP3 format shows information whether GStreamer MP3 Audio encoder has been found. You can click button Check again to run a MP3 support test.](images/3.0/installation/debian/format_support_mp3_ok.png|256x192) 
+[A sound is playing during the test.](images/3.0/installation/debian/format_support_mp3_check.png|256x192)
+[Test has been successful.](images/3.0/installation/debian/format_support_mp3_check_success.png|256x192)


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
