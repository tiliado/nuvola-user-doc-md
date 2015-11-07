Title: Install Nuvola Player 3.0 Beta
Image: images/3.0/unity/orig/unity_google_play_music_launcher_star_rating.png
Description: Nuvola Player 3.0 will be the first release of the third generation of a runtime for
    web-based music streaming services that provides more native user experience and integration with Linux
    desktop environments than usual web browsers can offer. Nuvola Players handles multimedia keys,
    shows desktop notifications, integrates with various sound indicators, media player applets,
    GNOME lock screen and launchers and more.

Nuvola Player 3 project officially supports and provides packages for [Ubuntu](#ubuntu) 14.10-15.04,
([15.10 in progress](https://github.com/tiliado/nuvolaplayer/issues/166)), [Fedora](#fedora) 22
([23 in progress](https://github.com/tiliado/nuvolaplayer/issues/167)) and [Debian](#debian)
Jessie, Stretch and Sid. The Nuvola Player developer has tested installation and functionality in
clean virtualized instances of these distributions and can assure reasonable user support in case
of problems.

However, Nuvola Player should also work on [other modern Linux distributions](#other-linux), but
user experience might not be optimal (e.g. inconsistent look and behaviour) and quality of user
support depends on complexity of an issue.


Ubuntu {: #ubuntu}
======

Graphical Installer or Terminal Kung-fu
---------------------------------------

There are two ways how to install Nuvola Player:

 1. **Power users** who are excellent in command-line kung-fu can just add
    [the Nuvola Player Repository](https://tiliado.eu/nuvolaplayer/repository/) manually and install
    Nuvola Player using common package management tools of your linux distribution. Then skip to the
    section [Check format support](#ubuntu-format-support).

 2. Users who are **not friends with a terminal** can take advantage of an easy-to-use graphical
    installer and follow instructions in the next section.

Install Tiliado Repository Installer
------------------------------------

 1. Download Tiliado Repository Installer for your
    distribution release and open it with Ubuntu Software Center.
     * [Ubuntu 14.04 LTS Trusty Tahr](https://tiliado.eu/repository-installer/download/trusty/) 
     * [Ubuntu 14.10 Utopic Unicorn](https://tiliado.eu/repository-installer/download/utopic/) 
     * [Ubuntu 15.04 Vivid Vervet](https://tiliado.eu/repository-installer/download/vivid/)
     * [Ubuntu 15.10 Wily Werewolf](https://tiliado.eu/repository-installer/download/wily/)
 2. Wait a bit as Ubuntu Software Center is a pretty slow beast. Then click **Install** button.
 3. Enter your password to confirm installation.


<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Download Tiliado Repository Installer and open it with Ubuntu Software Center" href="../images/3.0/unity/orig/unity_firefox_download_installer.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_firefox_download_installer.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Wait a bit as Ubuntu Software Center is a pretty slow beast. Then click Install button." href="../images/3.0/unity/orig/unity_install_installer.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_install_installer.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Enter your password to confirm installation." href="../images/3.0/unity/orig/unity_install_installer_auth.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_install_installer_auth.png" width="256" height="192" /></a></li>
</ul>
</div>

Add Nuvola Player Repository
----------------------------

!!! danger "Warning"
    
    Make sure you have installed **Tiliado Repository Installer version 0.3.2** or newer. If unsure,
    [download the latest version](https://tiliado.eu/nuvolaplayer/repository/).

  1. Click **Ubuntu button** in the top left corner to open Unity Dash.
  2. Launch **Tiliado Repositories** installer.
  3. Use anonymous access or Enter login credentials to your Tiliado account.
  4. Select Nuvola Player repository.
  5. Select repository components you want to install Nuvola Player from.
  6. Select which packages you want to install from the repository.
  7. Review the summary and click **Install** button.
  8. Enter your password to confirm installation.
  9. If installation is successful, click Quit button. Otherwise copy the installation log and
     [contact support](https://groups.google.com/d/forum/nuvola-player-users).
 10. Click **Ubuntu button** in the top left corner to open Unity Dash.
 11. Launch Nuvola Player 3.
 12. You should see Nuvola Player 3 services selector window.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Ubuntu button in the top left corner to open Unity Dash." href="../images/3.0/unity/orig/unity_installer_installed_open_dash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_installed_open_dash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Tiliado Repositories installer." href="../images/3.0/unity/orig/unity_dash_tiliado_installer.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_tiliado_installer.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Use anonymous access or enter login credentials to your Tiliado account." href="../images/3.0/unity/orig/unity_installer_anonymous.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_anonymous.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select Nuvola Player repository." href="../images/3.0/unity/orig/unity_installer_repositories.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_repositories.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select repository components you want to install Nuvola Player from." href="../images/3.0/unity/orig/unity_installer_components_stable_beta.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_components_stable_beta.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select which packages you want to install from the repository." href="../images/3.0/unity/orig/unity_installer_packages.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_packages.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Review the summary and click Install button." href="../images/3.0/unity/orig/unity_installer_summary.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_summary.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Enter your password to confirm installation." href="../images/3.0/unity/orig/unity_installer_install_auth.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_install_auth.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="If installation is successful, click Quit button." href="../images/3.0/unity/orig/unity_installer_done_quit.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_installer_done_quit.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Ubuntu button in the top left corner to open Unity Dash." href="../images/3.0/unity/orig/unity_open_dash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_open_dash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Nuvola Player 3." href="../images/3.0/unity/orig/unity_dash_nuvola.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Nuvola Player 3 services selector window." href="../images/3.0/unity/orig/unity_nuvola_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvola_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
</ul>
</div>

Check Format Support {: #ubuntu-format-support}
--------------------

!!! info
    
    **Nuvola Player 3 packages for Ubuntu** have both Flash plugin and GStreamer MP3 audio decoder as
    dependencies, so these plugins should work out of the box without any hassles.

 1. Click **Ubuntu button** in the top left corner to open Unity Dash.
 2. Launch Nuvola Player 3.
 3. You should see Nuvola Player 3 services selector window. Launch Grooveshark, for example.
 4. Open Gear menu and select Format Support.
 5. Tab Web Plugins shows information about available Flash Player plugins.
 6. Tab MP3 format shows information whether GStreamer MP3 Audio encoder has been found. You can
    click button Check again to run a MP3 support test.
 
<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Ubuntu button in the top left corner to open Unity Dash." href="../images/3.0/unity/orig/unity_open_dash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_open_dash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Nuvola Player 3." href="../images/3.0/unity/orig/unity_dash_nuvola.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_dash_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Nuvola Player 3 services selector window. Launch Grooveshar, for example." href="../images/3.0/unity/orig/unity_nuvola_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_nuvola_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Open Gear menu and select Format Support." href="../images/3.0/new/orig/unity_grooveshark_appmenu_format_support.png" class="thumbnail"><img src="../images/3.0/new/small/unity_grooveshark_appmenu_format_support.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Tab Web Plugins shows information about available Flash Player plugins." href="../images/3.0/unity/orig/unity_grooveshark_format_support_flash.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_format_support_flash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Tab MP3 format shows information whether GStreamer MP3 Audio encoder has been found. You can click button Check again to run a MP3 support test."href="../images/3.0/unity/orig/unity_grooveshark_format_support_mp3_ok.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_format_support_mp3_ok.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="A sound is playing during the test." href="../images/3.0/unity/orig/unity_grooveshark_format_support_mp3_check.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_format_support_mp3_check.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Test has been successful." href="../images/3.0/unity/orig/unity_grooveshark_format_support_mp3_check_success.png" class="thumbnail"><img src="../images/3.0/unity/small/unity_grooveshark_format_support_mp3_check_success.png" width="256" height="192" /></a></li>
</ul>
</div>

Explore Features
----------------

<div class="row">
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-unity"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-unity">Unity</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-gnome"><img src="../images/3.0/new/small/gnome_grooveshark_add_to_favorites.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-gnome">GNOME</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-terminal"><img src="../images/3.0/unity/small/unity_nuvolactl_multiple_apps.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-terminal">Terminal & scripts</a>
      </div>
    </div>
  </div>
</div>


Fedora {: #fedora}
======

Graphical Installer or Terminal Kung-fu
---------------------------------------

There are two ways how to install Nuvola Player:

 1. **Power users** who are excellent in command-line kung-fu can just add
    [the Nuvola Player Repository](https://tiliado.eu/nuvolaplayer/repository/) manually and install
    Nuvola Player using common package management tools of your linux distribution. Then skip to the
    section [Install Flash Plugin](#fedora-flash).

 2. Users who are **not friends with a terminal** can take advantage of an easy-to-use graphical
    installer and follow instructions in the next section.

Install Tiliado Repository Installer
------------------------------------

 1. Download Tiliado Repository Installer for your
    distribution release and open it with Software Install tool.
    * [Fefora 22](https://tiliado.eu/repository-installer/download/fc22/)
    * In progress: [Fedora 23](https://tiliado.eu/repository-installer/download/fc23/) - be careful
      as [not all issues have been solved yet](https://github.com/tiliado/nuvolaplayer/issues/167)
 2. When the Software Install tool is launched, click **Install** button.
 3. Enter your password to confirm installation.

<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Download Tiliado Repository Installer for your distribution release and open it with Software Install tool." href="../images/3.0/gnome/orig/gnome_firefox_download_rpm.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_firefox_download_rpm.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="When the Software Install tool is launched, click Install button." href="../images/3.0/gnome/orig/gnome_install_installer.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_install_installer.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Enter your password to confirm installation." href="../images/3.0/gnome/orig/gnome_install_installer_auth.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_install_installer_auth.png" width="256" height="192" /></a></li>

</ul>
</div>

Add Nuvola Player Repository
----------------------------

!!! danger "Warning"
    
    Make sure you have installed **Tiliado Repository Installer version 0.3.2** or newer. If unsure,
    [download the latest version](https://tiliado.eu/nuvolaplayer/repository/).

  1. Click **Activities button** in the top left corner to open GNOME Overview.
  2. Launch **Tiliado Repositories** installer.
  3. Use anonymous access or enter login credentials to your Tiliado account.
  4. Select Nuvola Player repository.
  5. Select repository components you want to install Nuvola Player from.
  6. Select which packages you want to install from the repository.
  7. Review the summary and click **Install** button.
  8. Enter your password to confirm installation.
  9. If installation is successful, click Quit button. Otherwise copy the installation log and
     [contact support](https://groups.google.com/d/forum/nuvola-player-users).
 10. Click **Activities button** in the top left corner to open GNOME Overview.
 11. Launch Nuvola Player 3.
 12. You should see Nuvola Player 3 services selector window.


<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview." href="../images/3.0/gnome/orig/gnome_installer_installed_open_activities.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_installed_open_activities.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Tiliado Repositories installer." href="../images/3.0/gnome/orig/gnome_activities_launch_installer.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_activities_launch_installer.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Use anonymous access or enter login credentials to your Tiliado account." href="../images/3.0/gnome/orig/gnome_installer_anonymous.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_anonymous.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select Nuvola Player repository." href="../images/3.0/gnome/orig/gnome_installer_repositories.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_repositories.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select repository components you want to install Nuvola Player from." href="../images/3.0/gnome/orig/gnome_installer_components_stable_beta.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_components_stable_beta.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select which packages you want to install from the repository." href="../images/3.0/gnome/orig/gnome_installer_packages.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_packages.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Review the summary and click Install button." href="../images/3.0/gnome/orig/gnome_installer_summary.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_summary.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Enter your password to confirm installation." href="../images/3.0/gnome/orig/gnome_installer_install_auth.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_install_auth.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="If installation is successful, click Quit button. Otherwise copy the installation log and contact support." href="../images/3.0/gnome/orig/gnome_installer_finished.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_installer_finished.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview." href="../images/3.0/gnome/orig/fedora_flash_install_done_activities.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_done_activities.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Launch Nuvola Player 3." href="../images/3.0/gnome/orig/gnome_activities_nuvola.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_activities_nuvola.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="You should see Nuvola Player 3 services selector window." href="../images/3.0/gnome/orig/gnome_selector_launch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_selector_launch_grooveshark.png" width="256" height="192" /></a></li>
</ul>
</div>

Install Flash Plugin {: #fedora-flash}
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
  8. Run command ``yum -y install flash-plugin`` to install Flash plugin.
  9. Close both terminal and Nuvola Player.
  10. Click **Activities button** in the top left corner to open GNOME Overview and launch Nuvola Player again.
  11. Open Format support dialog and check whether Flash plugin is recognized.


<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="Flash plugin is not available in a clean Fedora installation." href="../images/3.0/gnome/orig/fedora_grooveshark_flash_button.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_grooveshark_flash_button.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Flash plugin is not available in a clean Fedora installation." href="../images/3.0/gnome/orig/fedora_grooveshark_format_support_flash.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_grooveshark_format_support_flash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Install Flash to open Adobe Flash Installation web page in your web browser." href="../images/3.0/new/orig/fedora_grooveshark_install_flash.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_grooveshark_install_flash.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Select variant &quot;YUM for Linux (YUM)&quot;." href="../images/3.0/gnome/orig/fedora_flash_install_select_yum.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_select_yum.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Download button." href="../images/3.0/gnome/orig/fedora_flash_install_download_button.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_download_button.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Open downloaded package with Software Install tool." href="../images/3.0/gnome/orig/fedora_flash_install_download_rpm.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_download_rpm.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Install the downloaded package to add Adobe Flash repository." href="../images/3.0/gnome/orig/fedora_flash_install_rpm.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_rpm.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview and launch Terminal." href="../images/3.0/gnome/orig/fedora_activities_terminal.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_activities_terminal.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Installation of Flash plugin in terminal (1/2)." href="../images/3.0/gnome/orig/fedora_flash_install_terminal_1.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_terminal_1.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Installation of Flash plugin in terminal (2/2)." href="../images/3.0/gnome/orig/fedora_flash_install_terminal_2.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_terminal_2.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Quit Nuvola Player" href="../images/3.0/new/orig/fedora_grooveshark_flash_installed_quit.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_grooveshark_flash_installed_quit.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player again." href="../images/3.0/gnome/orig/fedora_flash_install_relaunch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_relaunch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Open Format support dialog." href="../images/3.0/new/orig/fedora_grooveshark_flash_installed_format_support.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_grooveshark_flash_installed_format_support.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Check whether Flash plugin is recognized." href="../images/3.0/new/orig/fedora_grooveshark_format_support_flash_ok.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_grooveshark_format_support_flash_ok.png" width="256" height="192" /></a></li>
</ul>
</div>

Install GStreamer MP3 Audio Decoder {: #fedora-mp3}
-----------------------------------

!!! info
    
    Fedora repository doesn't contain a GStreamer MP3 Audio Decoder package,
    so it **cannot be installed automatically with Nuvola Player 3** package and it's necessary to
    [install it manually](https://ask.fedoraproject.org/en/question/42073/how-i-can-install-audio-codecs-like-mp3/).


 1. Click **Activities button** in the top left corner to open GNOME Overview and launch Terminal.
 2. Run command ``su`` or ``sudo -i`` to get superuser rights.
 3. Run following command to add a RPM Fusion repository.
     
        :::text
        yum localinstall --nogpgcheck \
        http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm \
        http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm
    
  4. Run following command to install GStreamer MP3 Audio Decoder from the RPM Fusion repository.
    
        :::text
        yum install gstreamer1-{libav,plugins-{good,ugly,bad-free}}

  9. Close both terminal and Nuvola Player.
 10. Click **Activities button** in the top left corner to open GNOME Overview and launch Nuvola Player again.
 11. Open Format support dialog and check whether GStreamer MP3 Audio Decoder is recognized.
  
<div class="cointainer">
<ul class="thumbnails row" data-toggle="lightbox">
<li class="col-md-8"><a title="GStreamer MP3 Audio Decoder is not available in a clean Fedora installation." href="../images/3.0/new/orig/fedora_fromat_support_mp3_button.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_fromat_support_mp3_button.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="GStreamer MP3 Audio Decoder is not available in a clean Fedora installation." href="../images/3.0/new/orig/fedora_format_support_mp3_unsupported_check_again.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_format_support_mp3_unsupported_check_again.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="GStreamer MP3 Audio Decoder is not available in a clean Fedora installation." href="../images/3.0/new/orig/fedora_format_support_mp3_unsupported_check_failed.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_format_support_mp3_unsupported_check_failed.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview and launch Terminal." href="../images/3.0/gnome/orig/fedora_activities_terminal.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_activities_terminal.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Installation of GStreamer MP3 Audio Decoder in terminal (1/3)." href="../images/3.0/gnome/orig/fedora_mp3_install_terminal_1.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_mp3_install_terminal_1.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Installation of GStreamer MP3 Audio Decoder in terminal (2/3)." href="../images/3.0/gnome/orig/fedora_mp3_install_terminal_2.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_mp3_install_terminal_2.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Installation of GStreamer MP3 Audio Decoder in terminal (3/3)." href="../images/3.0/gnome/orig/fedora_mp3_install_terminal_3.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_mp3_install_terminal_3.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Quit Nuvola Player" href="../images/3.0/new/orig/fedora_grooveshark_mp3_installed_quit.png" class="thumbnail"><img src="../images/3.0/new/small/fedora_grooveshark_mp3_installed_quit.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Click Activities button in the top left corner to open GNOME Overview and launch Nuvola Player again." href="../images/3.0/gnome/orig/fedora_flash_install_relaunch_grooveshark.png" class="thumbnail"><img src="../images/3.0/gnome/small/fedora_flash_install_relaunch_grooveshark.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Open Format support dialog." href="../images/3.0/gnome/orig/gnome_grooveshark_appmenu_format_support.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_grooveshark_appmenu_format_support.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="Check whether GStreamer MP3 Audio Decoder is recognized." href="../images/3.0/gnome/orig/gnome_format_support_mp3_ok_check_again.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_format_support_mp3_ok_check_again.png" width="256" height="192" /></a></li>
<li class="col-md-8"><a title="A sound is playing during the test." href="../images/3.0/gnome/orig/gnome_format_support_mp3_checking.png" class="thumbnail"><img src="../images/3.0/gnome/small/gnome_format_support_mp3_checking.png" width="256" height="192" /></a></li>
</ul>
</div>

Explore Features
----------------

<div class="row">
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-gnome"><img src="../images/3.0/new/small/gnome_grooveshark_add_to_favorites.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-gnome">GNOME</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-unity"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-unity">Unity</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-terminal"><img src="../images/3.0/unity/small/unity_nuvolactl_multiple_apps.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-terminal">Terminal & scripts</a>
      </div>
    </div>
  </div>
</div>

Debian {: #debian}
======

Installation instructions for Debian haven't been written yet, but will be made before the stable release.
You can follow [instructions for Ubuntu](#ubuntu) for now. Please report any issues to
[the Nuvola Player Users mailing list](https://groups.google.com/d/forum/nuvola-player-users).
I'll be there to help you ;-)

Graphical Installer or Terminal Kung-fu
---------------------------------------

There are two ways how to install Nuvola Player:

 1. **Power users** who are excellent in command-line kung-fu can just add
    [the Nuvola Player Repository](https://tiliado.eu/nuvolaplayer/repository/) manually and install Nuvola Player
    using common package management tools of your linux distribution.

 2. Users who are **not friends with a terminal** can take advantage of an easy-to-use graphical installer
    and follow instructions in the next section.


Install Tiliado Repository Installer
------------------------------------

Download Tiliado Repository Installer for your distribution release and install it with package installer.

  * [Debian 8 Jessie](https://tiliado.eu/repository-installer/download/jessie/) 
  * [Debian 9 Stretch](https://tiliado.eu/repository-installer/download/stretch/) 
  * [Debian Sid](https://tiliado.eu/repository-installer/download/sid/) 

Add Nuvola Player Repository
----------------------------

!!! danger "Warning"
    
    Make sure you have installed **Tiliado Repository Installer version 0.3.2** or newer. If unsure,
    [download the latest version](https://tiliado.eu/nuvolaplayer/repository/).

  1. Launch **Tiliado Repositories** installer from applications list.
  2. Use anonymous access or Enter login credentials to your Tiliado account.
  3. Select Nuvola Player repository.
  4. Select repository components you want to install Nuvola Player from.
  5. Select which packages you want to install from the repository.
  6. Review the summary and click **Install** button.
  7. Enter your password to confirm installation.
  8. If installation is successful, click Quit button. Otherwise copy the installation log and
     [contact support](https://groups.google.com/d/forum/nuvola-player-users).
  9. Click **Ubuntu button** in the top left corner to open Unity Dash.
 10. Launch Nuvola Player 3 from applications list.
 11. You should see Nuvola Player 3 services selector window.

Explore Features
----------------

<div class="row">
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-gnome"><img src="../images/3.0/new/small/gnome_grooveshark_add_to_favorites.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-gnome">GNOME</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-unity"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-unity">Unity</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-terminal"><img src="../images/3.0/unity/small/unity_nuvolactl_multiple_apps.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-terminal">Terminal & scripts</a>
      </div>
    </div>
  </div>
</div>

Other Distributions {: #other-linux}
===================

Nuvola Player 3 should work also on modern linux distributions which meet minimal requirements listed bellow,
but hasn't been tested here by the developer and support may be limited for that reason.
You can take a look at [a list of unofficial packages](https://github.com/tiliado/nuvolaplayer/wiki/Unofficial)
provided by a community or [build Nuvola Player from source](https://github.com/tiliado/nuvolaplayer).

Dependencies
------------

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

Format Support
--------------

Streaming services use following technologies for audio playback:

* **Adobe Flash** - you will need a NPAPI based Flash plugin (not PAPI) - see [Flash download page](http://get.adobe.com/flashplayer/)
* **HTML5 Audio with MP3 format** - you will need a functional [GStreamer stack](http://gstreamer.freedesktop.org/modules/)
  with a MP3 decoder. I'd recommend to install modules `gst-plugins-base`, `gst-plugins-good`, `gst-plugins-ugly` and `gst-plugins-bad`.

Explore Features
----------------

<div class="row">
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-gnome"><img src="../images/3.0/new/small/gnome_grooveshark_add_to_favorites.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-gnome">GNOME</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-unity"><img src="../images/3.0/unity/small/unity_google_play_music_launcher_star_rating.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-unity">Unity</a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-8">
    <div class="thumbnail">
      <a href="./explore.html#explore-terminal"><img src="../images/3.0/unity/small/unity_nuvolactl_multiple_apps.png" width="256" height="192" /></a>
      <div class="caption">
        <a class="btn btn-primary btn-block" role="button" href="./explore.html#explore-terminal">Terminal & scripts</a>
      </div>
    </div>
  </div>
</div>

[TOC]
