Title: Install Nuvola Player 3.0 on Fedora
Image: images/3.0/unity/unity_google_play_music_launcher_thumbs_up.png
Description: Nuvola Player 3.0 is the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.

!!! info "Supported Releases"

    The Nuvola Player 3 project officially supports and provides packages for
    Fedora 25-26.

Choose Installation Method {: #install}
==========================

There are two ways how to install Nuvola Player on your system. Choose the one which suits you best.

1.  [User-friendly graphical installation](#installer): Users who are not friends with a terminal
    can take advantage of an easy-to-use graphical installer.
    **This method is recommended to less experienced users.**

2.  [Manual installation from terminal](./manual-installation.html): Power users who are excellent in command-line kung-fu can just add
    [the Nuvola Player Repository](https://tiliado.eu/nuvolaplayer/repository/) manually and install
    Nuvola Player using common package management tools of your linux distribution. Then skip to the
    section [Check format support](#format-support).
    **This method is not recommended to less experienced users. Any mistake can break your system.**


User-Friendly Graphical Installation {: #installer}
====================================

!!! info "Use up-to-date installer"
    
    It is recommended to always download an up-to-date version of the Tiliado Repository Installer.

Install Tiliado Repository Installer
------------------------------------

 1. Download Tiliado Repository Installer for your
    distribution release and open it with Software Install tool.
    * [Fedora 25](https://tiliado.eu/repository-installer/download/fc25/)
    * [Fedora 26](https://tiliado.eu/repository-installer/download/fc26/)
 2. When the Software Install tool is launched, click **Install** button.
 3. Enter your password to confirm installation.

!!! warning "Installation via Software Install tool may fail behind HTTP proxy server"
    
    Software Install tool is not reliable behind HTTP proxy server and installation may fail. In
    that case, please install the Tiliado Repository Installer from command line under root/superuser
    account.
    
        su
        dnf install /path/to/location/of/tiliado-repositories*.rpm
    

 Gallery
+[Download Tiliado Repository Installer for your distribution release and open it with Software Install tool.](images/3.0/gnome/gnome_firefox_download_rpm.png|256x192)
+[When the Software Install tool is launched, click Install button.](images/3.0/gnome/gnome_install_installer.png|256x192)
+[Enter your password to confirm installation.](images/3.0/gnome/gnome_install_installer_auth.png|256x192)

Add Nuvola Player Repository
----------------------------

  1. Click **Activities button** in the top left corner to open GNOME Overview.
  2. Launch **Tiliado Repositories** installer.
  3. Use anonymous access or enter login credentials to your Tiliado account.
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
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/fedora_open_activities.png|256x192)
+[Launch Tiliado Repositories installer.](images/3.0/gnome/fedora_activities_tiliado_installer.png|256x192)
+[Use anonymous access or enter login credentials to your Tiliado account.](images/3.0/gnome/gnome_installer_anonymous.png|256x192)
+[Select Nuvola Player repository.](images/3.0/gnome/gnome_installer_repositories.png|256x192)
+[Select repository components you want to install Nuvola Player from.](images/3.0/installation/fedora_tiliado_installer_components_stable.png|256x192)
+[Select which packages you want to install from the repository.](images/3.0/gnome/gnome_installer_packages.png|256x192)
+[Review the summary and click Install button.](images/3.0/gnome/gnome_installer_summary.png|256x192)
+[Enter your password to confirm installation.](images/3.0/gnome/gnome_installer_install_auth.png|256x192)
+[If installation is successful, click Quit button. Otherwise copy the installation log and contact support.](images/3.0/gnome/gnome_installer_finished.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview.](images/3.0/gnome/fedora_open_activities.png|256x192)
+[Launch Nuvola Player 3.](images/3.0/gnome/gnome_activities_nuvola.png|256x192)
+[You should see Nuvola Player 3 services selector window.](images/3.0/gnome/gnome_selector_launch_grooveshark.png|256x192)

Format Support {: #format-support}
==============

Nuvola Player requires some plugins that are not available in the official Fedora repositories.

Install Flash Plugin {: #flash}
--------------------

!!! info
    
    Fedora repository doesn't contain a [Flash plugin](http://fedoraproject.org/wiki/Flash) package,
    so it **cannot be installed automatically with Nuvola Player 3** package and it's necessary to
    [install it manually](https://ask.fedoraproject.org/en/question/10217/how-to-install-adobe-flash-on-fedora/).

  1. Open [Adobe Flash Installation web page](http://get.adobe.com/flashplayer/) in your web browser.
  2. Select variant "YUM for Linux (YUM)" and click Download button.
  3. Open downloaded package with Software Install Flash tool.
  4. Install the downloaded package to add Adobe Flash repository.
  5. Click **Activities button** in the top left corner to open GNOME Overview and launch Terminal.
  6. Run command ``su`` or ``sudo -i`` to get superuser rights.
  7. Run command ``rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux`` to import PGP key.
  8. Run command ``dnf -y install flash-plugin`` to install Flash plugin.
  9. Close both terminal and Nuvola Player.
  10. Click **Activities button** in the top left corner to open GNOME Overview and launch Nuvola Player again.
  11. Open Format support dialog and check whether Flash plugin is recognized.

 Gallery
+[Flash plugin is not available in a clean Fedora installation.](images/3.0/gnome/fedora_grooveshark_flash_button.png|256x192)
+[Flash plugin is not available in a clean Fedora installation.](images/3.0/gnome/fedora_grooveshark_format_support_flash.png|256x192)
+[Select variant &quot;YUM for Linux (YUM)&quot;.](images/3.0/gnome/fedora_flash_install_select_yum.png|256x192)
+[Click Download button.](images/3.0/gnome/fedora_flash_install_download_button.png|256x192)
+[Open downloaded package with Software Install tool.](images/3.0/gnome/fedora_flash_install_download_rpm.png|256x192)
+[Install the downloaded package to add Adobe Flash repository.](images/3.0/gnome/fedora_flash_install_rpm.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Terminal.](images/3.0/gnome/fedora_activities_terminal.png|256x192)
+[Installation of Flash plugin in terminal.](images/3.0/gnome/fedora_flash_install_terminal_1.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player again.](images/3.0/gnome/gnome_activities_deezer.png|256x192)
+[Open Format support dialog.](images/3.0/gnome/fedora_grooveshark_flash_installed_format_support.png|256x192)
+[Check whether Flash plugin is recognized.](images/3.0/gnome/fedora_grooveshark_format_support_flash_ok.png|256x192)

Install GStreamer MP3 Audio Decoder {: #mp3}
-----------------------------------

### Fedora 25+

!!! info
    
    Fedora repository contain a GStreamer MP3 Audio Decoder package since Fedora 25,
    install package [gstreamer1-plugin-mpg123](https://admin.fedoraproject.org/pkgdb/package/rpms/gstreamer1-plugin-mpg123/).

### Fedora 24

!!! info
    
    Fedora 24 repository doesn't contain a GStreamer MP3 Audio Decoder package,
    so it **cannot be installed automatically with Nuvola Player 3** package and it's necessary to
    [install it manually](https://ask.fedoraproject.org/en/question/42073/how-i-can-install-audio-codecs-like-mp3/).


 1. Click **Activities button** in the top left corner to open GNOME Overview and launch Terminal.
 2. Run command ``su`` or ``sudo -i`` to get superuser rights.
 3. Run following command to add a RPM Fusion repository.
     
        :::text
        dnf install --nogpgcheck \
        http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
        http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    
  4. Run following command to install GStreamer MP3 Audio Decoder from the RPM Fusion repository.
    
        :::text
        dnf install gstreamer1-{libav,plugins-{good,ugly,bad-free}}

  9. Close both terminal and Nuvola Player.
 10. Click **Activities button** in the top left corner to open GNOME Overview and launch Nuvola Player again.
 11. Open Format support dialog and check whether GStreamer MP3 Audio Decoder is recognized.

 Gallery
+[GStreamer MP3 Audio Decoder is not available in a clean Fedora installation.](images/3.0/gnome/fedora_format_support_mp3_button.png|256x192)
+[GStreamer MP3 Audio Decoder is not available in a clean Fedora installation.](images/3.0/gnome/fedora_format_support_mp3_unsupported_check_again.png|256x192)
+[GStreamer MP3 Audio Decoder is not available in a clean Fedora installation.](images/3.0/gnome/fedora_format_support_mp3_unsupported_check_failed.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Terminal.](images/3.0/gnome/fedora_activities_terminal.png|256x192)
+[Installation of GStreamer MP3 Audio Decoder in terminal (1/4).](images/3.0/gnome/fedora_mp3_install_terminal_1.png|256x192)
+[Installation of GStreamer MP3 Audio Decoder in terminal (2/4).](images/3.0/gnome/fedora_mp3_install_terminal_2.png|256x192)
+[Installation of GStreamer MP3 Audio Decoder in terminal (3/4).](images/3.0/gnome/fedora_mp3_install_terminal_3.png|256x192)
+[Installation of GStreamer MP3 Audio Decoder in terminal (4/4).](images/3.0/gnome/fedora_mp3_install_terminal_4.png|256x192)
+[Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player again.](images/3.0/gnome/gnome_activities_deezer.png|256x192)
+[Open Format support dialog.](images/3.0/gnome/gnome_grooveshark_appmenu_format_support.png|256x192)
+[Check whether GStreamer MP3 Audio Decoder is recognized.](images/3.0/gnome/gnome_format_support_mp3_ok_check_again.png|256x192)
+[A sound is playing during the test.](images/3.0/gnome/fedora_format_support_mp3_checking.png|256x192)

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
