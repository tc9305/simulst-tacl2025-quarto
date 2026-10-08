# StreamST

串流語音翻譯的研究與實驗紀錄。這裡採用 StreamST 作為整理主題；閱讀各篇論文時，仍需確認作者的實際定義與輸入假設。

- 負責人：待填寫
- 目前進度：已有共用術語筆記；StreamAtt 詳細方法閱讀與實驗待開始
- 研究問題：continuous／unbounded input 下如何管理語音與文字歷史，以及可靠地評估品質與延遲？
- 下一步：閱讀 StreamAtt 的 history selection 與 StreamLAAL 評估方法

## 閱讀入口

- [共用術語與閱讀判斷規則](../notes/terminology.md)
- [共用術語網頁版](https://tc9305.github.io/streaming-speech-research/notes/terminology.html)
- [StreamST 網頁入口](https://tc9305.github.io/streaming-speech-research/StreamST/index.html)
- [StreamAtt，ACL 2024](https://aclanthology.org/2024.acl-long.202/)
- [SimulST／TACL 2025 簡報](https://tc9305.github.io/streaming-speech-research/SimulST/index.html)

## 名稱與研究設定

StreamAtt 2024 在摘要中把 SimulST 描述為處理預切語音，並以 continuous、unbounded streams 定義 StreamST。TACL 2025 則使用較廣的 SimulST 框架，指出預切輸入是多數研究的簡化設定。這是兩篇論文的用語範圍差異，不是整個領域固定的二分法。

完整比較與來源請見共用術語筆記。後續方法閱讀、實驗腳本與結果將從這裡連結，並同步更新 `docs/StreamST/index.html`。