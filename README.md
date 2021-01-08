## Test project for Revizor evaluation

### Prerequisites

 - Download the archive with the plugin
 - Update your PyCharm to **2020.3** and open it
 - Open the `test-project` directory as a PyCharm Project via **File - Open - ...**

### Plugin installation

 - In the opened PyCharm window with the project, click **File - Settings - Plugins**, 
   and then **Install Plugin from Disk…**:
   
<img src="https://i.ibb.co/tq0Dywx/HLd0-Fr-KYz-ZCX0iem-JEQU3z-PF8-Ua7-WHOso67-EKlgcs-Guz-DUk-FEVciko-Ejbl-Zx-S6-Cuh-Hv-Dc-CTg-TSD7-Tnf.png" alt="HLd0-Fr-KYz-ZCX0iem-JEQU3z-PF8-Ua7-WHOso67-EKlgcs-Guz-DUk-FEVciko-Ejbl-Zx-S6-Cuh-Hv-Dc-CTg-TSD7-Tnf" border="0">
   
 - Choose the path to the downloaded plugin's archive, it should be something like that: 
   `/path/to/revizor-1.0-SNAPSHOT.zip`

### Evaluation

 - Since the plugin was installed, it should highlight patterns like this one:

<img src="https://i.ibb.co/FXCCpYm/11.png" alt="11" border="0">
 
 - You can press **Alt + Enter** to invoke an intention action and apply suggested quick fixes
   
   - If nothing is highlighted in the test project, try to restart the IDE, or 
     check its version (it should be 2020.3)