# 樂齡資訊整合系統
## 作品概述
本專案為一款專為年長者設計的應用程式，整合台北社區大學的開放資料與網路爬蟲技術，將分散於各處的課程資訊統整至單一平台。透過簡化的操作流程與放大的視覺設計，降低年長者取得學習資源的門檻，讓他們能更便利地瀏覽課程、查詢開課時間及報名資訊，促進終身學習與社區參與。
## 實作方式
採用 Java 語言進行 Android 原生開發，後端資料擷取部分使用 Python 建立爬蟲系統。透過 Requests 函式庫串接台北社區大學的 Open Data API，並結合 BeautifulSoup 與 Selenium WebDriver 處理動態網頁內容，將爬取的課程資料儲存至 SQLite 資料庫。Android 端讀取預先建置的資料庫檔案取得課程資訊，介面設計著重於大字體、高對比色彩及直覺式操作，採用卡片式排版呈現課程內容。

## 系統展示
### 課程列表
<div align="center">
<img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/front%20page.png width=200/> <img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/community%20college_course%20list.png width=200/> <img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/community%20college_course%20list_2.png width=200/>
</div>

### 收藏
<div align="center">
<img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/favorites.png width=200/>
</div>

### 個人化課表
<div align="center">
<img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/schedule.png width=200/> <img src=https://github.com/inorihayuri7240/LiveAndLearn/blob/main/system%20picture/schedule_2.png width=200/>
</div>
