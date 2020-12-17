## Test project for [BugFinder](https://github.com/JetBrains-Research/bug-finder) evaluation

### Prerequisites

 - Download the archive with the plugin [here](https://drive.google.com/file/d/1-un9CRMFXEEXJEvdXZk-Sui0V_EsjuCf/view?usp=sharing)
 - Update your PyCharm to **2020.3** and open it
 - If some current project has opened, you can close it via **File - Close Project**
 - Now you should see the PyCharm welcome screen. Click the button **Get from VCS**:

<img width="550px" src="https://i.ibb.co/B6rbjp0/c-WLRf-Rrq0a-Za-HIf9s-Vi07-wfl1-Y4-X5-VG6-QBusv-YVep-Wcik-S-hg-Ox44j0nf-MSMegfa-A7aohpo-Onw-BGkq-QXP.png" alt="c-WLRf-Rrq0a-Za-HIf9s-Vi07-wfl1-Y4-X5-VG6-QBusv-YVep-Wcik-S-hg-Ox44j0nf-MSMegfa-A7aohpo-Onw-BGkq-QXP" border="0">

 - Insert URL: `https://github.com/SmirnovOleg/bug-finder-test`, specify the location directory, and click **Clone**:

<img width="550px" src="https://i.ibb.co/yY4CKK9/W7r-Cz-Udp19-NCwc-QYKfv-Z8-XDMf7-Dq-Pyei-Ui-A9-koh-Vruf-JVNn-FC-X96-ZHQf-Jxng5c0-VTcym-Raj-PLo-WZb-A.png" alt="W7r-Cz-Udp19-NCwc-QYKfv-Z8-XDMf7-Dq-Pyei-Ui-A9-koh-Vruf-JVNn-FC-X96-ZHQf-Jxng5c0-VTcym-Raj-PLo-WZb-A" border="0">

   - Or you can download a ZIP archive with the test-project [here](https://drive.google.com/file/d/1Nogxc2WHLMTbxWiT7tZnq3Kd5cGHBQKx/view?usp=sharing), unpack it by yourself and open it as a general project in PyCharm.


### Plugin installation

 - In the opened PyCharm window with the project, click **File - Settings - Plugins**, 
   and then **Install Plugin from Disk…**:
   
<img src="https://i.ibb.co/tq0Dywx/HLd0-Fr-KYz-ZCX0iem-JEQU3z-PF8-Ua7-WHOso67-EKlgcs-Guz-DUk-FEVciko-Ejbl-Zx-S6-Cuh-Hv-Dc-CTg-TSD7-Tnf.png" alt="HLd0-Fr-KYz-ZCX0iem-JEQU3z-PF8-Ua7-WHOso67-EKlgcs-Guz-DUk-FEVciko-Ejbl-Zx-S6-Cuh-Hv-Dc-CTg-TSD7-Tnf" border="0">
   
 - Choose the path to the downloaded archive, it should be something like that: 
   `/path/to/bug-finder-1.0-SNAPSHOT.zip`

### Evaluation

 - Since the plugin was installed, it should highlight patterns like this one:

<img src="https://i.ibb.co/L5GT2nW/vfl9g-A7-VNzp-ZCN7-Gc-XSSmz-QHRDeb-WMZx-Z1-Yj-F9-L7-Pc-KPk-Fz-Y60-TG6nd-O1o-M4-Rkf-Qx-2gu6-EDp4-S2la.png" alt="vfl9g-A7-VNzp-ZCN7-Gc-XSSmz-QHRDeb-WMZx-Z1-Yj-F9-L7-Pc-KPk-Fz-Y60-TG6nd-O1o-M4-Rkf-Qx-2gu6-EDp4-S2la" border="0">
   
 - You can press **Alt + Enter** to invoke an intention action and apply suggested quick fixes.
   
   - If nothing is highlighted in the test project, try to restart the IDE, 
     check its version (it should be 2020.3), or contact [us](https://jetbrains.slack.com/team/U01DED2LB5M).
     
 - After you finished, please fill in a [short anonymous survey](https://docs.google.com/forms/d/e/1FAIpQLSdX07czHER3OPnIYOJIHh9Oel7HSSVjUvMgJIIEN6HZFkINdA/viewform?usp=sf_link)
   that takes about 3-5 minutes to complete