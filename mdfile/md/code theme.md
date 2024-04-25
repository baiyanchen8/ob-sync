---
title: code theme
tags: [範本]

---

<!--  
here is my theme for dark mode 
its modify strong and mermaid .etc
so ,look by yourself
-->
<style>
/* 全域樣式設定 */
html, body, .ui-content,.navbar {
    background-color: #222; /* 全域背景色 */
    color: #F0F0F0; /* 全域文字色 */
}
.dropdown-menu {
  background: #222;
}
.dropdown-menu li a{
	color: #F0F0F1;
}
/* TOC（目錄）樣式 */
.ui-toc-dropdown {
  /* ... TOC 樣式設定 ... */
	background: #222;
	color:#fff;
}

.ui-toc-dropdown .nav > li > a {
  /* ... TOC 鏈接樣式設定 ... */
	color:#fff;
}

.ui-toc-dropdown .nav > li > a:hover {
  /* ... TOC 鏈接懸停樣式設定 ... */
	color:#fff;
}

.ui-toc-dropdown .nav > .active:focus > a,
.ui-toc-dropdown .nav > .active:hover > a,
.ui-toc-dropdown .nav > .active > a {
  /* ... TOC 鏈接激活樣式設定 ... */
	color:#fff;
}

/* TOC Menu（目錄選單）樣式 */
.ui-toc-dropdown .nav > li > a {
  /* ... TOC Menu 鏈接樣式設定 ... */
	background:#222;
	color:#fff;
}

.ui-toc-dropdown .nav > li > a:hover {
  /* ... TOC Menu 鏈接懸停樣式設定 ... */
	color:#fff;
}

.ui-toc-dropdown .nav > .active:focus > a,
.ui-toc-dropdown .nav > .active:hover > a,
.ui-toc-dropdown .nav > .active > a {
  /* ... TOC Menu 鏈接激活樣式設定 ... */
	color:#fff;
}
	
.markdown-body pre.mermaid {
  background-color: #777;
	border-radius: 13px;
}

/* 表格樣式設定 */
.markdown-body table {
  display: table;
  text-align: left;
  border-collapse: collapse; /* 合併表格邊框 */
  width: 100%; /* 設定表格寬度，可根據需要調整 */
  margin: 0 auto; /* 讓表格置中 */
	margin-bottom: 16px; /* 在表格底部添加 16px 的空行，根據需要調整 */

}

.markdown-body table thead tr {
  background-color: #44475a; /* 表格頭部背景色 */
}

.markdown-body table tr th {
  font-weight: bold;
  border: 1px solid #f8f8f2; /* 表格邊框色 */
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

.markdown-body table tbody tr {
  border: 1px solid #f8f8f2; /* 表格邊框色 */
  margin: 0;
  padding: 0;
}

.markdown-body table tbody tr:nth-child(2n) {
  background-color: #282a36; /* 表格偶數行背景色 */
}

.markdown-body table tbody tr:nth-child(2n + 1) {
  background-color: #343746; /* 表格奇數行背景色 */
}

.markdown-body table tr td {
  border: 1px solid #f8f8f2; /* 表格邊框色 */
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

.markdown-body table tr th:first-child,
.markdown-body table tr td:first-child {
  border-left-width: 1px;
}

.markdown-body table tr th:last-child,
.markdown-body table tr td:last-child {
  border-right-width: 1px;
}

/* 標題樣式設定 */
.markdown-body h1,
.markdown-body h2,
.markdown-body h3{
    color: #ddd; /* 標題文字色 */
		
}

.markdown-body h4,
.markdown-body h5,
.markdown-body h6{
	font-weight:750;
}
.markdown-body h1,
.markdown-body h2 {
    border-bottom-color: #ffffff69; /* 標題底線色 */
}

.markdown-body h1 .octicon-link,
.markdown-body h2 .octicon-link,
.markdown-body h3 .octicon-link,
.markdown-body h4 .octicon-link,
.markdown-body h5 .octicon-link,
.markdown-body h6 .octicon-link {
    color: #fff; /* 標題連結色 */
}

/* 圖片樣式設定 */
.markdown-body img {
    background-color: transparent;
}

/* 強調文字樣式設定 */
.markdown-body strong {
    color: #8B85E1; /* 強調文字色 */
}
/*斜體字*/
.markdown-body em {
    color: #f28500; /* 文字色 */
		font-weight:450;
}
.markdown-body em strong {
		font-style: normal; /* 移除斜體 */
    background: #F0F0F1;
    -webkit-background-clip: text;
    color: transparent;
    font-weight: 700;
    font-size: 125%;
}

/* 引用區塊樣式設定 */
.markdown-body blockquote.part.in-view {
    color: #F0F0F0; /* 引用區塊文字色 */
    font-weight: 500; /* 引用區塊文字粗細 */
}


/* 文字底色樣式設定 */
.markdown-body mark {
    border-radius: 4px;
    color: #282a36; /* 文字底色文字色 */
    background-color: #f1fa8c; /* 文字底色背景色 */
		font-weight: 600;
    margin: 0px 2px;
    padding: 0px 4px 1px 4px;
}

/* 詳細內容樣式設定 */
.markdown-body details{
    padding: 5px 10px;
    border: 0px solid #37352f;
    border-radius: 1px;
    background-color: #333333; /* 詳細內容背景色 */
		margin-bottom: 8px;
		border-radius: 8px; /* 設定邊角弧度 */
}

/* 代碼樣式設定 */
.markdown-body code,
.markdown-body tt {
    color: #eee; /* 代碼文字色 */
    background-color: rgba(230, 230, 230, 0.36); /* 代碼背景色 */
}

/* 連結樣式設定 */
a,
.open-files-container li.selected a {
    color: #5EB7E0; /* 連結文字色 */
}
</style>