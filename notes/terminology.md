# SimulST／StreamST：共用術語與閱讀判斷規則

**先確認輸入假設、分段方式、模型架構與輸出策略，再解讀系統名稱。**

這份筆記比較 StreamAtt（ACL 2024）與 Papi et al.（TACL 2025）的用語，作為 SimulST 與 StreamST 研究的共同閱讀入口。文中的一般工程例子與兩篇論文的定義分開標示；資料夾名稱是研究整理方式，不代表兩者是互斥的標準分類。

## 1. 同一個名稱，在不同論文裡可能不同

| 來源 | SimulST 的用法 | StreamST／串流的用法 | 閱讀重點 |
|---|---|---|---|
| StreamAtt，ACL 2024 | 摘要把 SimulST 描述為處理預切語音 | 明確以逐步接收 continuous、unbounded audio streams 定義 StreamST | 這是該文採用的區分方式 |
| Papi et al.，TACL 2025 | 以接收語音與生成譯文並行定義 SimulST；預期應用包含 unbounded speech | 整理 streaming、online、real-time 與 simultaneous 在文獻中的混用 | 用輸入、架構與輸出策略分類，避免只憑名稱推論能力 |

這個差異反映兩篇論文的問題設定與用語範圍。不能將「SimulST 一律 bounded、StreamST 一律 unbounded」當成整個領域的通用定義。

來源：[StreamAtt 摘要與 §1](https://aclanthology.org/2024.acl-long.202/)；[TACL 2025 §1、§3.2、§4](https://aclanthology.org/2025.tacl-1.14.pdf)。

## 2. 名稱描述什麼？

| 名稱 | 本筆記採用的解讀 | 能否單憑名稱判定 unbounded input？ |
|---|---|---|
| Speech-to-text translation（ST） | 本筆記聚焦語音到目標語文字；廣義 speech translation 也可能有語音輸出 | 不能 |
| Offline ST | 取得完整處理單位後翻譯；offline 不表示沒有網路 | 不能 |
| Simultaneous ST（SimulST） | 接收語音與生成部分譯文並行 | 不能；須檢查是否預切輸入 |
| Streaming ST／StreamST | 用法須依論文確認；StreamAtt 明確指 continuous、unbounded streams | 不能跨論文保證相同用法 |
| Real-time ST | 強調低延遲的處理與回應 | 不能；須檢查實際延遲設定與測量 |
| Online ST | 常用來與 offline 對比，也可能與 simultaneous／streaming 混用 | 不能；須檢查作者定義 |

上述 streaming、online 用法整理依 TACL 2025 §4，不是為所有研究制定固定定義。

## 3. 輸入假設：系統實際拿到什麼？

| 概念 | 本文脈絡與判斷方式 | 例子或注意事項 |
|---|---|---|
| Bounded input | TACL 2025 的 bounded setting 主要是翻譯前已切好的短語音段；輸入有有限長度 | 已備妥、具有起訖的句子音檔 |
| Unbounded input | 長串流沒有明確的整體長度資訊，須持續處理；不表示真的無限長 | Live microphone stream |
| Continuous speech／audio stream | 描述連續音訊流；可包含停頓，不代表說話者一直不休息 | 「連續」這個描述本身不足以交代輸入是否預切 |
| Long-form speech | 描述長篇音訊；長度與系統是否知道整體終點要分別檢查 | 一小時完整錄音是一般工程例子；其有限長度不等於已符合本文的短段 bounded 實驗設定 |

長錄音可以在翻譯前預切，也可以模擬逐步到來。判定研究設定時，要看模型收到的資料與可用資訊，不能只看原始檔案長度。

**系統對 unbounded stream 做線上 segmentation 後，內部得到 bounded segments；整體系統仍是在處理 unbounded input。**

來源：TACL 2025 §2.3、§3.1–3.2、Table 1。

## 4. 分段方式要拆成三個問題

| 問題 | 常見選擇 | 要釐清的事 |
|---|---|---|
| 何時分段？ | Pre-segmentation／simultaneous segmentation | 在翻譯開始前預切，還是在線處理時決定邊界？ |
| 誰決定邊界？ | Human／gold 或 automatic | 人手動切分或修正，還是模型、VAD 等自動判定？ |
| 是否需要語音分段？ | 有 segmentation 或 segmentation-free | 是否需要六步流程中的 Step 2？ |

- **Gold pre-segmentation**：翻譯前由人手動切分或修正邊界；資料集可能直接提供這些 bounded segments。
- **Automatic pre-segmentation**：翻譯前自動切好，翻譯階段取得 bounded segments。
- **Simultaneous segmentation**：系統在線處理 unbounded stream，同時自動決定邊界。
- **Segmentation-free**：不需要 Step 2 的語音分段；仍可有 chunks、內部對齊或字幕呈現的分段。

Automatic 可以出現在預切或線上分段中，因此不應把這些名稱當成完全互斥的四個選項。Gold 也不表示系統在線解決了邊界判定。

來源：TACL 2025 §3.1–3.2、Table 1。

## 5. Segment 與 chunk

| 名詞 | 功能 | 邊界與語意 |
|---|---|---|
| Segment | 語音 segmentation 得到的有邊界處理單位 | 有切分邊界，但不保證是完整句子或語意單位 |
| Chunk | 逐次餵入模型的短音訊單位，本文示例通常固定長度 | 餵入邊界不保證與 utterance 或語意邊界一致 |

```text
有 segmentation：
Unbounded stream → [ Segment S1 ][ Segment S2 ] …
                    C1 C2 C3       C4 C5 …

Segmentation-free：
Unbounded stream → C1 C2 C3 C4 C5 C6 …
```

**同樣的 500 ms chunks，可以來自預切音檔，也可以來自 continuous stream。Chunk size 只描述餵入方式，不能定義 input setting。** 500 ms 為教學示例，不是規定。

VAD 或固定長度 segmentation 可能切在語意中間；不能把 segment 一律等同完整句子。

來源：TACL 2025 §2.2、§3.1、Table 1、§5 “Be Clear about the Type of Speech Input”。

## 6. 架構與輸出策略是另外兩個維度

| 維度 | 選擇 | 分類依據 |
|---|---|---|
| Architecture | Cascade／Direct | 推論時是否經過明確產生的中間 ASR 輸出 |
| Output strategy | Incremental／Re-translation | 已顯示的譯文是否可以被修訂 |

Direct 不代表 segmentation-free，也不代表完全沒有文字 context：模型可以使用先前的目標語輸出，也可能使用 ASR supervision 或 pre-training。這些情況與「推論時繞過明確的中間 ASR 輸出」並不衝突。

在本文的 output strategy 分類中，incremental 指只追加；re-translation 允許修改已顯示內容。一般描述「輸入逐步到來」時也會使用 incremental，因此需看上下文。

例如「direct + bounded input + incremental output」同時交代三個不同維度，不能由其中一項直接推得另外兩項。

來源：TACL 2025 §3.2、Figure 2。

## 7. Buffer、policy 與 history management

| 概念 | 負責什麼？ |
|---|---|
| Speech Buffer B_S | 保留模型目前可用的語音歷史 |
| Text Buffer B_T | 保留先前已送出的目標語文字；不是中間 ASR transcript buffer |
| Hypothesis H | 模型提出的候選譯文 |
| Emitted output E | Policy 選擇這次送出的內容，也可能為空 |
| Step 4 policy | 決定現在等待，或送出哪些候選內容 |
| Step 5 trimming／reset | 決定下一輪保留哪些上下文 |

部分 trimming 保留部分歷史；reset 完全清空，可視為完全 trimming 的特例。若 segment 邊界已提供 reset，可不需要額外的部分裁剪。對長串流，仍需有能控制上下文大小的歷史管理機制。

語音與文字歷史要注意語意對齊。裁掉 buffer 不等於刪除使用者已看到的字幕；永久 commit 的說法須限定在只追加策略，re-translation 仍能修改已顯示內容。

來源：TACL 2025 §3.1，Steps 3–6。

## 8. 評估也要檢查假設

- **Computationally unaware latency**：假設模型運算時間為零，衡量來源資訊到對應輸出的延遲；也反映 policy 決策與跨語言字序。
- **Computationally aware latency**：計入實際運算時間；比較需交代硬體、程式與執行環境。
- **Unbounded evaluation**：系統輸出不一定吻合 reference 句界，句級評分的重新對齊可能出錯。
- **User experience**：除了最終品質，也要考慮等待、字幕修訂與重讀負擔。

StreamLAAL 是 StreamAtt 2024 提出的串流延遲指標，TACL 2025 引用它；不能把它解讀成單純替 LAAL 加上運算時間。此處評估工具限制依兩篇論文發表時的討論。

來源：StreamAtt 2024；TACL 2025 §3.2、§5。

## 9. 閱讀下一篇 paper 的檢查表

- [ ] 作者如何定義 SimulST／StreamST／streaming／online／real-time？
- [ ] 輸入是否在翻譯前預切？是 human／gold 還是 automatic？
- [ ] 若輸入是 unbounded，是否使用 simultaneous segmentation？
- [ ] Segment 與 chunk 分別如何定義？Chunk size 是多少？
- [ ] 模型是 direct 還是 cascade？使用哪些語音與文字 context？
- [ ] H 與 E 如何區分？Policy 何時等待、何時送出？
- [ ] Buffer 如何 trim／reset？如何維持 audio-text alignment？
- [ ] 已顯示的輸出能否修訂？如何衡量穩定性？
- [ ] 延遲是否計入運算？不同系統使用相同測量環境嗎？
- [ ] 評估是否真的涵蓋 unbounded input？如何處理 reference 對齊？

## 10. 參考文獻

1. Sara Papi, Marco Gaido, Matteo Negri, Luisa Bentivogli. 2024. *StreamAtt: Direct Streaming Speech-to-Text Translation with Attention-based Audio History Selection*. ACL, pp. 3692–3707. [論文頁面](https://aclanthology.org/2024.acl-long.202/) · [PDF](https://aclanthology.org/2024.acl-long.202.pdf) · DOI: 10.18653/v1/2024.acl-long.202。
2. Sara Papi, Peter Polák, Dominik Macháček, Ondřej Bojar. 2025. *How “Real” is Your Real-Time Simultaneous Speech-to-Text Translation System?* TACL 13, pp. 281–313. [論文頁面](https://aclanthology.org/2025.tacl-1.14/) · [PDF](https://aclanthology.org/2025.tacl-1.14.pdf) · DOI: 10.1162/tacl_a_00740。
