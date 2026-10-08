# StreamST

串流語音翻譯的研究與實驗紀錄。這裡採用 StreamST 作為整理主題；閱讀各篇論文時，仍需確認作者的實際定義與輸入假設。

- 負責人：待填寫
- 目前進度：已有共用術語筆記；StreamAtt 詳細方法閱讀與實驗待開始
- 研究問題：continuous／unbounded input 下如何管理語音與文字歷史，以及可靠地評估品質與延遲？
- 下一步：閱讀 StreamAtt 的 history selection 與 StreamLAAL 評估方法

## Nemotron 中文 ASR 簡報

[開啟簡報](report.html) · [Quarto 原始碼](report.qmd)

18 張繁體中文投影片，沿用 `../SimulST/` 的 1280 × 720 Reveal.js 版型：米白背景、深藍標題、青綠重點、頁碼與中文講者筆記。內容依序介紹模型、chunk 設定、中文 CER 結果與下一輪實驗規劃。

### 編輯與預覽

安裝 [Quarto CLI](https://quarto.org/docs/get-started/) 後，在 `StreamST/` 執行：

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
quarto preview report.qmd
```

產生可離線開啟的單檔簡報：

```sh
quarto render
```

- `report.qmd`：逐頁內容與 `.notes` 中文講者筆記。
- `_quarto.yml`：Reveal.js 設定；輸出保留在 `report.html`。
- `styles.css`：沿用 SimulST 字型、配色與版面。
- `data/chunk_results.csv`：實驗數據；渲染前自動重建結果表、摘要與 SVG 圖。
- `scripts/fix_slide_preview.py`：避免 Live Server 干擾內嵌的講者視窗程式。
- `assets/experiment-screenshot.png`：完整原始截圖。

方向鍵切換投影片／漸進顯示；`Esc` 開啟總覽；`F` 全螢幕；`S` 講者模式。講者模式建議透過 `quarto preview` 或 Live Server 使用；一般播放可直接開啟 HTML。

此處的 `report.html` 是本機簡報；`../docs/StreamST/index.html` 仍是研究入口。若日後更新 CSV，需同步檢查內文的樣本範圍、數字解讀與講者筆記。此次只有一段中文樣本，沒有實測延遲，也未重新執行 ASR。

## 閱讀入口

- [共用術語與閱讀判斷規則](../notes/terminology.md)
- [共用術語網頁版](https://tc9305.github.io/streaming-speech-research/notes/terminology.html)
- [StreamST 網頁入口](https://tc9305.github.io/streaming-speech-research/StreamST/index.html)
- [StreamAtt，ACL 2024](https://aclanthology.org/2024.acl-long.202/)
- [SimulST／TACL 2025 簡報](https://tc9305.github.io/streaming-speech-research/SimulST/index.html)

## 名稱與研究設定

StreamAtt 2024 在摘要中把 SimulST 描述為處理預切語音，並以 continuous、unbounded streams 定義 StreamST。TACL 2025 則使用較廣的 SimulST 框架，指出預切輸入是多數研究的簡化設定。這是兩篇論文的用語範圍差異，不是整個領域固定的二分法。

完整比較與來源請見共用術語筆記。後續方法閱讀、實驗腳本與結果將從這裡連結，並同步更新 `docs/StreamST/index.html`。
