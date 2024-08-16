Environment Configuration for Android:

* # Download Java and JAVA_HOME in environment variables
    - Java Development Kit (JDK) Java11 Download link , Java1.8 Download Link 
    - After installing Open CMD – Enter **where java**
    - Open the installed JDK folder and copy the Folder PATH(C:\Program Files\Java\jdk-11) 
    - Set environment variable 
      1. Search for **Environment Variables** then select **Edit the system environment variables** 
      2. Click the **Environment Variables** button. 
      3. Under System Variables, click New. 
      4. In the Variable Name field, enter either: 
         - **JAVA_HOME** if you installed the JDK (Java Development Kit)
           (or)
         - **JRE_HOME** if you installed the JRE (Java Runtime Environment) 
         - In the Variable Value field, enter your JDK or JRE installation path. 
           --> **Add System Variable** Popup
             - **Variable name: JAVA_HOME**
             - **Variable value: C:\Program Files\Java\jdk-1.8**
             - Click OK and Apply Changes 

    ```OR```

    - # Set the JAVA_HOME variable via the command line 
       1. If you would prefer to set the JAVA_HOME (or JRE_HOME) variable via the command line: 
       2. Open the command prompt (make sure you run it as administrator so you can add a system environment variable). 
       3. Set the value of the environment variable to your JDK (or JRE) installation path as follows: 
          - ```setx /m JAVA_HOME "C:\Program Files\Java\jdk11.0.17.8"```
          - Restart Command Prompt to reload the environment variables then use the following command to check that it's been added correctly.  
          - ```echo %JAVA_HOME%```
          - You should see the path to your JDK (or JRE) installation.
* # Download and install Android Studio 
   - Install Android Studio ([Steps to Setup Android Studio](https://developer.android.com/studio/install#windows)) 
   - Keep all the settings as default including SDK 
   - Copy the SDK folder path from the system variable ```C:\Users\YourUserName\AppData\Local\Android\SDK```
   - Right-click on **This PC -> Properties** 
   - On the left pane select **Advanced System Settings**
   - On the new window select 
        --> Advanced tab 
   - Click on the **Environment Variables** button 
   - On the first top section click on the **New** button 
   - set variable name -> ANDROID_HOME 
   - set variable value 
        --> the custom location of the Android SDK ```C:\Users\YourUserName\AppData\Local\Android\SDK``` 
   - Now click on the newly created variable name and in the box below select **Path** and click on the Edit button 
   - Now click on New and paste the location of the **platform-tools** 
   - Again click on New and paste the location of the **tools**  
   - Again click on New and paste the location of the **tools\bin** 
   - Again click on New and paste the location of the **build-tools**
   - Again click on New and paste the location of the **platforms** 
   - Click OK and Apply Changes as prompted
* # Open Android Studio and Configuration virtual device/Emulator/Real device:-
   - Open the path in My computer ```C:\Program Files\Android\Android Studio\bin``` 
   - Double click the studio64 
   - From Tools select **Device Manager** or Search **AVD Manager > +Create Virtual Device > Select the device (ex: pixel 3) > Next > Select the Android version** (Make sure to Download the release first; ex: Pie) and complete the download version > click on **Advance setting** > Give **AVD name** (ex:Demo).> **finish** >  click on launch to open the virtual mobile device.
* # Download node.js:- [Download Link](https://nodejs.org/en/download/prebuilt-installer) 
   - Go to above link > select **Windows** > click **x64** version > click **Download Node.js** button 
   - Set **NODE_HOME** Environmental variables path: After you finish the installation, _go to Program Files > open nodejs > copy the nodejs path(C:\Program Files\nodejs)>GO to environment variable>Create new variable name as ‘NODE_HOME’_ and paste the path as value  
   - # Set npm Environment variables path:  
      -    Go to nodejs>node_modules>npm>bin>copy the path (ex: C:\Program Files\nodejs\node_modules\npm\bin) and paste under path in environment variable.
* # Download Appium Server:-
   - [Download Appium Desktop](https://github.com/appium/appium-desktop/releases) 
   - Download Appium Server from Node using npm: go to cmd> type: **_npm install -g appium_** > hit enter>let extract and finish all the installation will say at the end ‘_added packages from …._ 
   - **Note:** There are 2 parts of Appium as _Client_ and _Server_. 
       - **Client:** We can write our appium des in multiple languages as _Java, JavaScript, C#, Python, Ruby_. So we need specific jar/packages/libraries as per language we are going to use. **Ex:_Appium java client jar (OR) Appium-Python-Client jar_** 
       - **Server:** We also need _Appium Server_ to listen to our code from the client and execute as per request in Server and trigger in mobile devices (virual). 
       - **npm:** npm is command line tool or installer to install Appium. We can download any node module(Ex: Appium Server) only using npm. 
   - **To Uninstall Appium Server:** _npm uninstall –g appium_
* # APK file
    - [Download Apk file](https://windows.apkpure.com/)
* # Download Appium Inspector 
    - [Download link](https://github.com/appium/appium-inspector/releases)
* # Install APK file into Emulator 
   - If you want to use an app that's not available in the Google Play Store on the Android Emulator, or if you want to install a specific APK, you can manually install the APK file by using a drag-and-drop. 
   - To install an APK file on the emulated device, drag an APK file onto the emulator screen. An APK Installer dialog appears. When the installation completes, you can view the app in your apps list. 
   - To add a file to the emulated device, drag the file onto the emulator screen. The file is placed in the /sdcard/Download/ directory. You can view the file from Android Studio using the [Device Explorer](https://developer.android.com/studio/debug/device-file-explorer) or find it from the device using the _Downloads or Files_ app, depending on the device version. 
   - Verify the emulator device is connected 
       - _Open Command Prompt > enter adb devices_ > It shown List of devices attached and device name
   - After the installation & setup done  open CMD type: **_appium or appium –p port number(4723)_** > hit enter > it will tell you the version number as ‘_Welcome to Appium v2…+ Appium REST http interface Listener started on 0.0.0.0:4723 (port number)._
* # Connecting with real android device 
    - **Note:** On some devices, the Developer options screen might be located or named differently.
    - Click the  link and follow those steps [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options#enable)
    - Download Vysor
    - Double click the Vysor-win-5.0.7.exe file and if device is connected your device name is visible 
    - Open Command Prompt > enter adb devices > It shown List of devices attached and device name 
    - Create a Python project 
    - File > Settings > Search Python Interpreter > click + icon > Search Appium-Python-Client and select > click Install Package button > close > Apply and OK
* # Another commands:-
  * 
  * Get appActivity in command line 

Windows--> adb shell dumpsys package <packageName> | findstr /i activity 

Unix/Linux --> adb shell dumpsys package <packageName> | grep -i activity 

Get appPackage and appActivity in command line 

Windows  

Step1: search cmd --> click run as administration 

Step2: enter adb devices 

Step3: adb shell 

Step4: dumpsys window windows | grep –E 'mTopActivityComponent' 

 
