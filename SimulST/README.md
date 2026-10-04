# SimulST 論文導讀：Quarto + SVG / HTML

以 Papi et al. (2025), **How “Real” is Your Real-Time Simultaneous Speech-to-Text Translation System?** 為主題的 16 張繁體中文簡報。

- [論文](https://aclanthology.org/2025.tacl-1.14/) · [PDF](https://aclanthology.org/2025.tacl-1.14.pdf)
- [線上簡報](https://tc9305.github.io/streaming-speech-research/SimulST/)

## 修改與預覽

安裝 [Quarto](https://quarto.org/docs/get-started/) 後，在 `SimulST/` 資料夾執行：

```sh
quarto preview index.qmd
quarto render
```

`index.qmd` 是投影片內容；`styles.css` 管理視覺樣式；`assets/*.svg` 是可編輯的圖解；`assets/demo.html` 是 chunk 累積的教學互動。輸出在 `../docs/SimulST/index.html`，採用 embed-resources，可下載後直接在瀏覽器開啟。

## 報告操作

- 左右方向鍵：上一頁／下一頁與漸進顯示。
- `Esc`：總覽；`F`：全螢幕；`S`：講者模式（含中文講稿）。
- 第 9 張：用按鈕逐次加入 500 ms chunk；可重置。
- 第 12 張：方向鍵比較追加式輸出與可修訂輸出。

## GitHub Pages

本 repository 從 `main` 分支的 `/docs` 資料夾發布。第一次啟用：Settings → Pages → Deploy from a branch → main → /docs → Save。

每次修改後先 `quarto render`，再把來源與 `../docs/SimulST/index.html` 一起 commit / push；GitHub Pages 會發布更新。`.nojekyll` 讓 GitHub 直接提供 Quarto 產出的檔案。發布的簡報是靜態頁面，不需伺服器，也不呼叫翻譯 API。

## 內容與來源

每張投影片註明原文節次與頁碼，speaker notes 包含詳細解說與容易混淆的術語。六步流程與術語以本文為準；圖中音訊長度、候選句子與 trimming 範圍都是教學示例，沒有執行實際 ST 模型。

Survey 統計描述本文的 110 篇調查範圍，不代表目前所有 SimulST 研究。圖解為重新繪製，非原文實驗數據以外的新結果。原文採用 CC BY 4.0，來源與作者列於簡報。

## 檔案

```text
index.qmd          # 16 張簡報與中文講者筆記
_quarto.yml        # Reveal.js、輸出與內嵌資源設定
styles.css         # 字型、配色與版面
assets/            # SVG 教學圖與 HTML 互動
../docs/SimulST/index.html    # 已產生、可離線開啟的簡報
../docs/.nojekyll     # Pages 靜態發布
```
