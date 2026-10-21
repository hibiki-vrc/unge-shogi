# 運ゲー将棋 Web試作版

Godot 4.7.2通常版 / Compatibility / Thread Support OFF。
ローカル2人対戦とCPU2スタイルを実装。CPUは試作で、名人相当の強さは未調整。

## 起動

Pythonが利用できるWindowsで、ZIPを展開してStart-preview.cmdをダブルクリック。
http://127.0.0.1:8060/Build.html が開く。遊んでいる間は黒いウィンドウを開いたままにする。
終了時はそのウィンドウを閉じる。file://でBuild.htmlを直接開かない。
他のHTTPサーバーでもこのフォルダー全体を配信できる。ゲーム用外部サーバーは不要。

## 操作

駒→緑の移動先の順にクリック。持ち駒は駒台から選択。
CPU対戦は「次の対局」で「CPU・通常将棋型」または「CPU・確率考慮型」と自分の先後を選び、
「開始」→「実行」。同じseed／新seedでの再戦は現在の対戦設定を保つ。
王手・詰みの制限なし。王の消滅で敗北。全捕獲に30%返り討ち。
隕石予告の後、5×5→3×3→1マスの炎上が進み復旧する。

## 投稿と制限

Build.html/js/wasm/pckとその他Build.*を一緒に保管し、個別リネームしない。
unityroom公式Godot手順の投稿対象はBuild.pck。ソースZIPや検証ページではない。
実際の対応エンジン版・容量上限は投稿画面で確認する。
ローカルブラウザー確認済み。unityroom実プレイヤー、Safari、モバイルは未確認。
公開・アップロードはまだ行っていない。

更新ソースと詳細設計は同時配布のunge-cpu-web-source.zip内README.mdとdocsを参照。
フォントの権利表記はTHIRD_PARTY_NOTICES.md / OFL.txt。
