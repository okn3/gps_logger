## API Reference

* api/get/gps
GPSデータの取得

* api/set/gps
GPSデータの登録

* web/show_recent
最近のスポット表示

* web/show_route
今までのルート表示

## 準備

### 素材

* raspberry pi2
* GPSロガー(BU-353S4)
* 0sim or DMMSIM
* L02-C
* androidスマホ

### 構成

* pi : データ送信
* AWS：受け取り、保存
     * WAF:Django/flask
* android : データ可視化、通知

### 機能

[pi]
* GPSデータの送信

[サーバ]
* データの受け取り
* DB書き込み
* データ整理、処理
* ツイート、API連携

[android]
* 地図表示
* ジオフェンス通知
* 通知処理

------------------------------------------------
## task

### 開発の手順

準備
- [ ] ラズパイのSIM接続
- [x] GPSデータ取得確認
- [ ] バイクの電力で動作するか？

実装
- [x] AWS設定(mod_wsgi-)
- [x] 受け取りプログラム
- [x] piから送信するプログラム(Requestsで実装)
- [x] DB受け取り確認
- [x] ウェブでデータ確認

- [ ] android通知用プログラム（サーバ）
- [ ] androidで表示（ネイティブ）

------------------------------------------------

## 参考

-  sim+L02c+raspiの設定について

http://matoken.org/blog/blog/2015/12/29/try-0sim-of-dejimonostation-magazine-in-february-2016-degree-in-raspberry-pi/

-  GPSデータの取得方法
- http://make.bcde.jp/raspberry-pi/gps%E3%81%AE%E6%8E%A5%E7%B6%9A/

- GPSログデータ読み方http://www.gpsdgps.com/qa.htm

-  Google Map API使い方

http://www.ajaxtower.jp/googlemaps/

## 勉強
MongoDBのデータ構造な簡単な操作など - Qiita http://qiita.com/yuji0602/items/c55e2cb75376fd565b4e

pythonでHTTP通信+ベーシック認証
　[Python] HTTP通信でGetやPostを行う - YoheiM .NET http://www.yoheim.net/blog.php?q=20160204

## その他

markdown+evernote
 chromeアプリ　marxico
