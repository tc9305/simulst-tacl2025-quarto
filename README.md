# Streaming Speech Research

從 SimulST 出發，延伸探索 StreamST 與 Speech LLM 的共同研究與學習紀錄。各主題保留研究筆記、簡報、實驗與 demo，透過 GitHub Pages 串起閱讀入口。

## 研究入口

| 主題 | 內容 | 進度 |
| --- | --- | --- |
| [SimulST](SimulST/README.md) | Papi et al. (2025) 論文理解與報告簡報 | 已有簡報 |
| [StreamST](StreamST/README.md) | 串流語音翻譯研究與實驗 | 待開始 |
| [SpeechLLM](SpeechLLM/README.md) | Speech LLM 架構研究、實作與 demo | 待開始 |

網站首頁：https://tc9305.github.io/simulst-tacl2025-quarto/

目前 GitHub repo 名稱維持 `simulst-tacl2025-quarto`；若之後改名為 `streaming-speech-research`，請同步更新網站網址與 SimulST 的線上簡報連結。

## 資料夾

```text
README.md       # 研究與協作入口
SimulST/        # 現有 Quarto 簡報來源、圖解與說明
StreamST/       # 串流語音翻譯研究
SpeechLLM/      # Speech LLM 研究、實作與 demo
docs/           # GitHub Pages 發布內容
```

## 預覽與發布

首頁為 `docs/index.html`，各主題入口為 `docs/<主題>/index.html`。可直接用瀏覽器開啟；SimulST 簡報保留 Quarto 與內嵌資源格式。

安裝 Quarto 後，在 repo 根目錄執行：

```sh
cd SimulST
quarto preview index.qmd
quarto render
```

簡報輸出至根目錄 `docs/SimulST/index.html`。修改首頁或主題入口時，直接編輯對應 HTML。

GitHub Pages 設定：Settings → Pages → Deploy from a branch → main → /docs → Save。將來源與更新的 `docs/` 一起 commit / push，即可發布。

## 一起研究

- 各主題 README 記錄研究問題、負責人、目前進度與下一步。
- 用 Issue 記錄論文疑問、實驗想法與待討論事項。
- 透過 branch 與 PR 提交變更，說明新增的理解或實驗結果。
- 維護者可邀請隊友成為 collaborator，共同參與研究。

模型權重、資料集與大型音訊請放在 Git 之外，保留取得方式與必要範例。需要推論服務的 demo 可由主題入口連到另外運行的服務。
