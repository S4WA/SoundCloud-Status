# Soundcloud Status
![image1](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_1.png?raw=true)  
![image2](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_2.png?raw=true)  

# 環境
 - Python 3.7.4
   - [pypresence](https://github.com/qwertyquerty/pypresence)
   - [urllib3](https://github.com/urllib3/urllib3)
 - Browser
   - [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
     - [Script](https://github.com/S4WA/soundcloud-status/raw/master/chrome/contents.user.js)

※ Windowsでしか動作確認してません

# インストール
1. [スクリプト](https://github.com/S4WA/soundcloud-status/raw/master/chrome/contents.user.js)をTampermonkeyに追加
2. ``server\start.bat`` を実行
3. SoundCloudを開く

# OBS
![image3](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_3.png?raw=true)  
``soundcloud-status\server``にある  
- ``artwork.jpg``  
- ``export.txt``  
をOBSのソースに追加する  
![image4](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_4.png?raw=true)  

※ フォーマットとかの設定は[``server\config.ini``](https://github.com/S4WA/soundcloud-status/blob/master/server/config.ini)で変えれる

# 仕組み
1. ブラウザからテキストを取る
2. テキストをPythonのローカルサーバー(localhost:8000)にPOSTで送る
3. POSTされたテキストをRich Presenceで使う