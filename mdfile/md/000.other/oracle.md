---
title: oracle
tags: [範本]

---

<style>
	/* Variables */
:root {
  /*dracula official spec colors */
  --dracula-background: rgb(40, 42, 54);
  --dracula-current-line: rgb(68, 71, 90);
  --dracula-foreground: rgb(248, 248, 242);
  --dracula-comment: rgb(98, 114, 164);
  --dracula-cyan: rgb(139, 233, 253);
  --dracula-green: rgb(80, 250, 123);
  --dracula-orange: rgb(255, 184, 108);
  --dracula-pink: rgb(255, 121, 198);
  --dracula-purple: rgb(189, 147, 249);
  --dracula-red: rgb(255, 85, 85);
  --dracula-yellow: rgb(241, 250, 140);

  /* dracula custom colors for typora */
  --dracula-foreground-fade: rgba(248, 248, 242, 0.5);
  --dracula-background-dark: rgb(32, 34, 39);

  /* background */
  --background-primary: #282a36;
  --background-primary-alt: #44475a;
  --background-secondary: #282a36;
  --background-secondary-alt: #1a1e24;

  /* text */
  --text-normal: #f8f8f2;
  --text-title-h1: #bd93f9;
  --text-title-h2: #bd93f8;
  --text-title-h3: #bd93f7;
  --text-title-h4: #bd93f6;
  --text-title-h5: #bd93f5;
  --text-title-h6: #bd93f4;
  --text-link: #8be9fd;
  --markup-code: #ffb86c;
  --text-tag: #50fa7b;
  --text-a: #ff79c6;
  --text-a-hover: #ff79c0;
  --text-mark: #f1fa8c;

  /* other */
  --interactive-accent: #f1fa8c;
  --interactive-accent-rgb: #f1fa8c;
  --blockquote-border: #b294bb;

  /* table color */
  --table-border-color: var(--dracula-foreground);
  --table-thead-color: var(--dracula-current-line);
  --table-bg-color: var(--dracula-background);
  --table-bg-darker-color: var(--dracula-background-dark);
}

/* Navigation */
.navbar {
  background: var(--dracula-background);
}

.navbar-default {
  box-shadow: 0 5px 10px 0 rgb(0 0 0 / 15%);
  border-color: var(--dracula-background);
}

.navbar-default .navbar-brand {
  color: var(--text-color1);
}

.navbar-default .navbar-brand:hover {
  color: var(--dracula-purple);
}

.navbar-default .navbar-nav > li > a {
  color: var(--text-color1);
}

.navbar-default .navbar-nav > li > a:hover {
  color: var(--dracula-purple);
}

.ui-toc-dropdown .nav > li > a {
  color: rgb(169, 162, 143);
}

.ui-toc-dropdown .nav > li > a:hover {
  color: rgb(241, 250, 140);
}

.ui-toc-dropdown .nav > .active:focus > a,
.ui-toc-dropdown .nav > .active:hover > a,
.ui-toc-dropdown .nav > .active > a {
  color: rgb(255, 255, 255);
}

.ui-infobar,
.community-button {
  color: white;
}

.community-button:hover {
  background: var(--dracula-purple);
  color: var(--dracula-background);
}

.ui-comment-app .open-comments {
  background: var(--background-primary);
}

.dropdown-menu {
  background: var(--background-primary-alt);
}

.ui-notification .notification-menu-item:hover {
  background: var(--background-secondary);
}

/* Body */
html,
body,
.ui-content {
  font-family: 'Open Sans', 'Clear Sans', 'Helvetica Neue', Helvetica, Arial,
    sans-serif;
  font-size: 15px;
  color: var(--text-normal);
  background: var(--background-primary);
  line-height: 1.6;
}

/* Buttons */
.btn-default {
  border-color: var(--dracula-purple);
  background: var(--dracula-background);
  color: rgb(188, 194, 205);
}

.btn-default.active {
  border-color: var(--dracula-purple);
  background: var(--dracula-purple);
  color: var(--dracula-background);
}

.btn-default.active:hover {
  border-color: var(--dracula-purple);
  background: rgb(145, 116, 191);
}

.btn-default:hover {
  border-color: var(--dracula-purple);
  background: rgb(70, 63, 93);
  color: rgb(255, 255, 255);
}

.btn-primary {
  background: var(--dracula-cyan);
  color: rgb(10, 30, 15);
}

.btn-primary:hover {
  background: rgb(110, 177, 194);
  color: rgb(10, 30, 15);
}

/* Headings */
.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
  padding-bottom: 0em;
  border-bottom: none;
}

.markdown-body h1 {
  font-weight: 500;
  font-size: 28px;
  font-weight: bold;
  color: var(--text-title-h1);
}

.markdown-body h2 {
  font-weight: 500;
  font-size: 26px;
  font-weight: bold;
  color: var(--text-title-h2);
}

.markdown-body h3 {
  font-weight: 500;
  font-size: 23px;
  font-weight: bold;
  color: var(--text-title-h3);
}

.markdown-body h4 {
  font-weight: 500;
  font-size: 20px;
  font-weight: bold;
  color: var(--text-title-h4);
}

.markdown-body h5 {
  font-weight: 500;
  font-size: 18px;
  font-weight: bold;
  color: var(--text-title-h5);
}

.markdown-body h6 {
  font-weight: 500;
  font-size: 16px;
  font-weight: bold;
  color: var(--text-title-h6);
}

/* list */
.markdown-body ul,
.markdown-body ol {
  padding-left: 30px;
}

/* Hyperlinks */
.markdown-body a {
  color: var(--text-link);
}

.markdown-body a:hover {
  color: var(--text-link);
}

/* Blockquote Area */
.markdown-body blockquote {
  color: var(--interactive-accent) !important;
  font-style: italic;
  border-color: var(--blockquote-border) !important;
}

.markdown-body blockquote p {
  display: inline;
}

/* Tables */
.markdown-body table {
  display: table;
  text-align: left;
}

.markdown-body table thead tr {
  background-color: var(--table-thead-color);
}

.markdown-bodytable tr th {
  font-weight: bold;
  border-left: 1px solid var(--table-border-color);
  border-right: 1px solid var(--table-border-color);
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

.markdown-body table tbody tr {
  border-top: 1px solid var(--table-border-color);
  margin: 0;
  padding: 0;
}

.markdown-body table tbody tr:nth-child(2n) {
  background-color: var(--table-bg-darker-color);
}

.markdown-body table tbody tr:nth-child(2n + 1) {
  background-color: var(--table-bg-color);
}

.markdown-body table tr td {
  border-left: 1px solid var(--table-border-color);
  border-right: 1px solid var(--table-border-color);
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

.markdown-body table tr th:first-child,
.markdown-body table tr td:first-child {
  border-left-width: 0px;
}

.markdown-body table tr th:last-child,
.markdown-body table tr td:last-child {
  border-right-width: 0px;
}

/* Codeblock */
.markdown-body code {
  border: 1px solid #525660;
  border-radius: 4px;
  color: var(--markup-code) !important;
  background-color: var(--background-primary-alt);
  bottom: -0.1px;
}

/* Keyboard Buttons */
.markdown-body kbd {
  background: var(--bg-color5);
  color: var(--text-color1);
  font-family: 'Lucida Console';
  border-color: var(--menu-divider-color);
}

.markdown-body pre code {
  padding: 5px;
  line-height: normal;
  display: block;
  background-color: var(--background-primary-alt);
}

.markdown-body pre {
  background-color: var(--background-primary-alt);
  border-radius: 5px;
  padding: 5px;
}

/* Text */
.markdown-body strong {
  color: var(--markup-code);
  font-weight: 700;
}

.markdown-body em {
  color: var(--interactive-accent);
}

/* Images */
.markdown-body img {
  background-color: transparent;
}

/* Mark */
.markdown-body mark {
  border-radius: 4px;
  color: var(--background-primary);
  background-color: var(--text-mark);
  margin: 0px 2px;
  padding: 0px 4px 1px 4px;
}

/* horizontal divider */
.markdown-body hr {
  height: 1px;
  background-color: var(--text-normal);
  border: 0px;
}

/* Details */
.markdown-body details {
  padding: 5px 10px;
  border: 0px solid #37352f;
  border-radius: 1px;
  background-color: rgb(56, 58, 89);
}

.markdown-body summary {
  color: rgb(248, 248, 242);
  font-weight: bold;
  cursor: pointer;
  padding: 4px;
}

/* prism.js dracula */
/*
* Dracula Theme for Prism.JS
*
* @author Gustavo Costa
* e-mail: gusbemacbe@gmail.com
*
* @contributor Jon Leopard
* e-mail: jonlprd@gmail.com
*
* @license MIT 2016-2020
*/

/* Scrollbars */

:root {
  --background: #282a36;
  --comment: #6272a4;
  --foreground: #f8f8f2;
  --selection: #44475a;

  --cyan: #8be9fd;
  --green: #50fa7b;
  --orange: #ffb86c;
  --pink: #ff79c6;
  --purple: #bd93f9;
  --red: #ff5555;
  --yellow: #f1fa8c;

  /* Transparency */

  /** 30% of transparency **/
  --background-30: #282a3633;
  --comment-30: #6272a433;
  --foreground-30: #f8f8f233;
  --selection-30: #44475a33;

  --cyan-30: #8be9fd33;
  --green-30: #50fa7b33;
  --orange-30: #ffb86c33;
  --pink-30: #ff79c633;
  --purple-30: #bd93f933;
  --red-30: #ff555533;
  --yellow-30: #f1fa8c33;

  /** 40% of transparency **/
  --background-40: #282a3666;
  --comment-40: #6272a466;
  --foreground-40: #f8f8f266;
  --selection-40: #44475a66;

  --cyan-40: #8be9fd66;
  --green-40: #50fa7b66;
  --orange-40: #ffb86c66;
  --pink-40: #ff79c666;
  --purple-40: #bd93f966;
  --red-40: #ff555566;
  --yellow-40: #f1fa8c66;
}

pre::-webkit-scrollbar {
  width: 14px;
}

pre::-webkit-scrollbar-track {
  background-color: var(--comment);
  border-radius: 0px;
}

pre::-webkit-scrollbar-thumb {
  background-color: var(--purple);
  border-radius: 0px;
}

/* Selection */

pre[class*='language-']::-moz-selection,
pre[class*='language-'] ::-moz-selection,
code[class*='language-']::-moz-selection,
code[class*='language-'] ::-moz-selection {
  text-shadow: none;
  background-color: var(--selection);
}

pre[class*='language-']::selection,
pre[class*='language-'] ::selection,
code[class*='language-']::selection,
code[class*='language-'] ::selection {
  text-shadow: none;
  background-color: var(--selection);
}

/* Line numbers */

pre.line-numbers {
  position: relative;
  padding-left: 3.8em;
  counter-reset: linenumber;
}

pre.line-numbers > code {
  position: relative;
  white-space: inherit;
}

.line-numbers .line-numbers-rows {
  position: absolute;
  pointer-events: none;
  top: 0;
  font-size: 100%;
  left: -3.8em;
  width: 3em; /* works for line-numbers below 1000 lines */
  letter-spacing: -1px;
  border-right: 1px solid #999;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.line-numbers-rows > span {
  pointer-events: none;
  display: block;
  counter-increment: linenumber;
}

.line-numbers-rows > span:before {
  content: counter(linenumber);
  color: #999;
  display: block;
  padding-right: 0.8em;
  text-align: right;
}

/* Toolbar for copying */

div.code-toolbar {
  position: relative;
}

div.code-toolbar > .toolbar {
  position: absolute;
  top: 0.3em;
  right: 0.2em;
  transition: opacity 0.3s ease-in-out;
  opacity: 0;
}

div.code-toolbar:hover > .toolbar {
  opacity: 1;
}

div.code-toolbar > .toolbar .toolbar-item {
  display: inline-block;
  padding-right: 20px;
}

div.code-toolbar > .toolbar a {
  cursor: pointer;
}

div.code-toolbar > .toolbar button {
  background: none;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  padding: 0;
  -webkit-user-select: none; /* for button */
  -moz-user-select: none;
  -ms-user-select: none;
}

div.code-toolbar > .toolbar a,
div.code-toolbar > .toolbar button,
div.code-toolbar > .toolbar span {
  color: var(--foreground);
  font-size: 0.8em;
  padding: 0.5em;
  background: var(--comment);
  border-radius: 0.5em;
}

div.code-toolbar > .toolbar a:hover,
div.code-toolbar > .toolbar a:focus,
div.code-toolbar > .toolbar button:hover,
div.code-toolbar > .toolbar button:focus,
div.code-toolbar > .toolbar span:hover,
div.code-toolbar > .toolbar span:focus {
  color: inherit;
  text-decoration: none;
  background-color: var(--green);
}

/* Remove text shadow for printing */

@media print {
  code[class*='language-'],
  pre[class*='language-'] {
    text-shadow: none;
  }
}

code[class*='language-'],
pre[class*='language-'] {
  color: var(--foreground);
  background: var(--background);
  text-shadow: none;
  font-family: PT Mono, Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono',
    monospace;
  text-align: left;
  white-space: pre;
  word-spacing: normal;
  word-break: normal;
  word-wrap: normal;
  line-height: 1.5;

  -moz-tab-size: 4;
  -o-tab-size: 4;
  tab-size: 4;

  -webkit-hyphens: none;
  -moz-hyphens: none;
  -ms-hyphens: none;
  hyphens: none;
}

/* Code blocks */

pre[class*='language-'] {
  background: var(--background);
  border-radius: 0.5em;
  padding: 1em;
  margin: 0.5em 0;
  overflow: auto;
  height: auto;
}

:not(pre) > code[class*='language-'],
pre[class*='language-'] {
  background: var(--background);
}

/* Inline code */
:not(pre) > code[class*='language-'] {
  padding: 4px 7px;
  border-radius: 0.3em;
  white-space: normal;
}

/* Code box limit */

.limit-300 {
  height: 300px !important;
}

.limit-300 {
  height: 400px !important;
}

.limit-500 {
  height: 500px !important;
}

.limit-600 {
  height: 600px !important;
}

.limit-700 {
  height: 700px !important;
}

.limit-800 {
  height: 800px !important;
}

.language-css {
  color: var(--purple);
}

.token {
  color: var(--pink);
}

.language-css .token {
  color: var(--pink);
}

.token.script {
  color: var(--foreground);
}

.token.bold {
  font-weight: bold;
}

.token.italic {
  font-style: italic;
}

.token.atrule,
.token.attr-name,
.token.attr-value {
  color: var(--green);
}

.language-css .token.atrule {
  color: var(--purple);
}

.language-html .token.attr-value,
.language-markup .token.attr-value {
  color: var(--yellow);
}

.token.boolean {
  color: var(--purple);
}

.token.builtin,
.token.class-name {
  color: var(--cyan);
}

.token.comment {
  color: var(--comment);
}

.token.constant {
  color: var(--purple);
}

.language-javascript .token.constant {
  color: var(--orange);
  font-style: italic;
}

.token.entity {
  color: var(--pink);
}

.language-css .token.entity {
  color: var(--green);
}

.language-html .token.entity.named-entity {
  color: var(--purple);
}

.language-html .token.entity:not(.named-entity) {
  color: var(--pink);
}

.language-markup .token.entity.named-entity {
  color: var(--purple);
}

.language-markup .token.entity:not(.named-entity) {
  color: var(--pink);
}

.token.function {
  color: var(--green);
}

.language-css .token.function {
  color: var(--cyan);
}

.token.important,
.token.keyword {
  color: var(--pink);
}

.token.prolog {
  color: var(--foreground);
}

.token.property {
  color: var(--orange);
}

.language-css .token.property {
  color: var(--cyan);
}

.token.punctuation {
  color: var(--pink);
}

.language-css .token.punctuation {
  color: var(--orange);
}

.language-html .token.punctuation,
.language-markup .token.punctuation {
  color: var(--foreground);
}

.token.selector {
  color: var(--pink);
}

.language-css .token.selector {
  color: var(--green);
}

.token.regex {
  color: var(--red);
}

.language-css .token.rule:not(.atrule) {
  color: var(--foreground);
}

.token.string {
  color: var(--yellow);
}

.token.tag {
  color: var(--pink);
}

.token.url {
  color: var(--cyan);
}

.language-css .token.url {
  color: var(--orange);
}

.token.variable {
  color: var(--comment);
}

.token.number {
  color: rgba(189, 147, 249, 1);
}

.token.operator {
  color: rgba(139, 233, 253, 1);
}

.token.char {
  color: rgba(255, 135, 157, 1);
}

.token.symbol {
  color: rgba(255, 184, 108, 1);
}

.token.deleted {
  color: #e2777a;
}

.token.namespace {
  color: #e2777a;
}

/* Line Highlighter */
.highlight-line {
  color: inherit;
  display: inline-block;
  text-decoration: none;

  border-radius: 4px;
  padding: 2px 10px;
}

.highlight-line:empty:before {
  content: ' ';
}

.highlight-line:not(:last-child) {
  min-width: 100%;
}

.highlight-line .highlight-line:not(:last-child) {
  min-width: 0;
}

.highlight-line-isdir {
  color: var(--foreground);
  background-color: var(--selection-30);
}

.highlight-line-active {
  background-color: var(--comment-30);
}

.highlight-line-add {
  background-color: var(--green-30);
}

.highlight-line-remove {
  background-color: var(--red-30);
}
.markdown-body .alert-info {
  display: flex;
  justify-content: space-between;
  max-width: 700px;
  margin: 20px auto;
}

.markdown-body .alert-info .text {
  flex: 1;
  padding: 10px;
  box-sizing: border-box;
}

.markdown-body .alert-info  img{
  flex: 1;
  text-align: center;
}

.markdown-body .alert-info  img {
  max-width: 100%;
  height: auto;
}

</style>
	