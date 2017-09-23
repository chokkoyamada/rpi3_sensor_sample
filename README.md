# Raspberry Pi 3 人感センサーと通知のサンプル

５秒毎にセンサーで検知を行い、検出するとLEDを光らせるとともにIFTTTへ通知（LINEに通知する設定をしている）を行います。

![img_7189](https://user-images.githubusercontent.com/843192/30771232-5a3f3c50-a07d-11e7-9f48-76bca10c10de.JPG)



## 事前準備

```
sudo apt-get update
sudo apt-get install python-rpi.gpio
```
## 実行

```
sudo python sensor.py
```

python 2.7で動作確認しています。
