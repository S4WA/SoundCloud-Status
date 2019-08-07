# Soundcloud Status
![image1](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_1.png?raw=true)  
![image2](https://github.com/S4WA/files/blob/master/soundcloud-status/Screenshot_2.png?raw=true)  

# 環境
 - Python 3.7.4
   - [pypresence](https://github.com/qwertyquerty/pypresence)
 - Browser
   - [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
     - [Script](https://github.com/S4WA/soundcloud-status/raw/master/chrome/contents.user.js)

# インストール
1. [スクリプト](https://github.com/S4WA/soundcloud-status/raw/master/chrome/contents.user.js)をTampermonkeyに追加
2. ``server/start.bat`` を実行
3. SoundCloudを開く

# 仕組み
1. ブラウザからテキストを取る
2. テキストをPythonのローカルサーバーにPOSTで送る
3. POSTされたテキストをRich Presenceで使う