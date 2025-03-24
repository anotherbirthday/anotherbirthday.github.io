from flask import Flask, render_template, request, send_file
import markdown
import os

app = Flask(__name__)

def generate_html(version, content, prev_page, next_page):
    # Базовый шаблон HTML
    template = f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head>

<meta charset="utf-8">
<meta name="generator" content="quarto-1.6.32">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">

<title>BDay page v{version} – BDay page</title>

<style>
code{{white-space: pre-wrap;}}
span.smallcaps{{font-variant: small-caps;}}
div.columns{{display: flex; gap: min(4vw, 1.5em);}}
div.column{{flex: auto; overflow-x: auto;}}
div.hanging-indent{{margin-left: 1.5em; text-indent: -1.5em;}}
ul.task-list{{list-style: none;}}
ul.task-list li input[type="checkbox"] {{
  width: 0.8em;
  margin: 0 0.8em 0.2em -1em;
  vertical-align: middle;
}}
</style>

<script src="site_libs/quarto-nav/quarto-nav.js"></script>
<script src="site_libs/quarto-nav/headroom.min.js"></script>
<script src="site_libs/clipboard/clipboard.min.js"></script>
<script src="site_libs/quarto-search/autocomplete.umd.js"></script>
<script src="site_libs/quarto-search/fuse.min.js"></script>
<script src="site_libs/quarto-search/quarto-search.js"></script>
<meta name="quarto:offset" content="./">
{f'<link href="./{prev_page}" rel="prev">' if prev_page else ''}
{f'<link href="./{next_page}" rel="next">' if next_page else ''}
<link href="./icon.png" rel="icon" type="image/png">
<script src="site_libs/quarto-html/quarto.js"></script>
<script src="site_libs/quarto-html/popper.min.js"></script>
<script src="site_libs/quarto-html/tippy.umd.min.js"></script>
<script src="site_libs/quarto-html/anchor.min.js"></script>
<link href="site_libs/quarto-html/tippy.css" rel="stylesheet">
<link href="site_libs/quarto-html/quarto-syntax-highlighting-2486e1f0a3ee9ee1fc393803a1361cdb.css" rel="stylesheet" id="quarto-text-highlighting-styles">
<script src="site_libs/bootstrap/bootstrap.min.js"></script>
<link href="site_libs/bootstrap/bootstrap-icons.css" rel="stylesheet">
<link href="site_libs/bootstrap/bootstrap-266a3a263fb7da8914d00535ab3f7aee.min.css" rel="stylesheet" append-hash="true" id="quarto-bootstrap" data-mode="light">
<script id="quarto-search-options" type="application/json">{{
  "location": "sidebar",
  "copy-button": false,
  "collapse-after": 3,
  "panel-placement": "start",
  "type": "overlay",
  "limit": 50,
  "keyboard-shortcut": [
    "f",
    "/",
    "s"
  ],
  "language": {{
    "search-no-results-text": "No results",
    "search-matching-documents-text": "matching documents",
    "search-copy-link-title": "Copy link to search",
    "search-hide-matches-text": "Hide additional matches",
    "search-more-match-text": "more match in this document",
    "search-more-matches-text": "more matches in this document",
    "search-clear-button-title": "Clear",
    "search-text-placeholder": "",
    "search-detached-cancel-button-title": "Cancel",
    "search-submit-button-title": "Submit",
    "search-label": "Search"
  }}
}}</script>

<link rel="stylesheet" href="styles.css">
</head>

<body class="nav-sidebar floating">

<div id="quarto-search-results"></div>
  <header id="quarto-header" class="headroom fixed-top">
    <nav class="quarto-secondary-nav">
      <div class="container-fluid d-flex">
        <button type="button" class="quarto-btn-toggle btn" data-bs-toggle="collapse" role="button" data-bs-target=".quarto-sidebar-collapse-item" aria-controls="quarto-sidebar" aria-expanded="false" aria-label="Toggle sidebar navigation" onclick="if (window.quartoToggleHeadroom) {{ window.quartoToggleHeadroom(); }}">
          <i class="bi bi-layout-text-sidebar-reverse"></i>
        </button>
          <nav class="quarto-page-breadcrumbs" aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="./v{version}.html">Version {version}</a></li></ol></nav>
          <a class="flex-grow-1" role="navigation" data-bs-toggle="collapse" data-bs-target=".quarto-sidebar-collapse-item" aria-controls="quarto-sidebar" aria-expanded="false" aria-label="Toggle sidebar navigation" onclick="if (window.quartoToggleHeadroom) {{ window.quartoToggleHeadroom(); }}">      
          </a>
      </div>
    </nav>
  </header>
<!-- content -->
<div id="quarto-content" class="quarto-container page-columns page-rows-contents page-layout-article">
<!-- sidebar -->
  <nav id="quarto-sidebar" class="sidebar collapse collapse-horizontal quarto-sidebar-collapse-item sidebar-navigation floating overflow-auto">
    <div class="pt-lg-2 mt-2 text-left sidebar-header">
    <div class="sidebar-title mb-0 py-0">
      <a href="./">BDay page</a> 
        <div class="sidebar-tools-main">
  <a href="" class="quarto-reader-toggle quarto-navigation-tool px-1" onclick="window.quartoToggleReader(); return false;" title="Toggle reader mode">
  <div class="quarto-reader-toggle-btn">
  <i class="bi"></i>
  </div>
</a>
</div>
    </div>
      </div>
    <div class="sidebar-menu-container"> 
    <ul class="list-unstyled mt-1">
        <li class="sidebar-item">
  <div class="sidebar-item-container"> 
  <a href="./index.html" class="sidebar-item-text sidebar-link">
 <span class="menu-text">Version 24</span></a>
  </div>
</li>
        <li class="sidebar-item">
  <div class="sidebar-item-container"> 
  <a href="./v23.html" class="sidebar-item-text sidebar-link">
 <span class="menu-text">Version 23</span></a>
  </div>
</li>
        <li class="sidebar-item">
  <div class="sidebar-item-container"> 
  <a href="./v22.html" class="sidebar-item-text sidebar-link">
 <span class="menu-text">Version 22</span></a>
  </div>
</li>
    </ul>
    </div>
</nav>
<div id="quarto-sidebar-glass" class="quarto-sidebar-collapse-item" data-bs-toggle="collapse" data-bs-target=".quarto-sidebar-collapse-item"></div>
<!-- margin-sidebar -->
    <div id="quarto-margin-sidebar" class="sidebar margin-sidebar">
        <nav id="TOC" role="doc-toc" class="toc-active">
    <h2 id="toc-title">On this page</h2>
   
  <ul>
  <li><a href="#твоя-разносторонность-the-way-you-think" id="toc-твоя-разносторонность-the-way-you-think" class="nav-link active" data-scroll-target="#твоя-разносторонность-the-way-you-think">Твоя разносторонность / The way you think</a></li>
  <li><a href="#твоё-доверие" id="toc-твоё-доверие" class="nav-link" data-scroll-target="#твоё-доверие">Твоё доверие</a></li>
  <li><a href="#твоя-поддержка" id="toc-твоя-поддержка" class="nav-link" data-scroll-target="#твоя-поддержка">Твоя поддержка</a></li>
  <li><a href="#по-традиции-список-твоих-фраз-которые-заставили-почувствовать-тепло-улыбнуться-или-просто-звучали-слишком-уж-хорошо" id="toc-по-традиции-список-твоих-фраз-которые-заставили-почувствовать-тепло-улыбнуться-или-просто-звучали-слишком-уж-хорошо" class="nav-link" data-scroll-target="#по-традиции-список-твоих-фраз-которые-заставили-почувствовать-тепло-улыбнуться-или-просто-звучали-слишком-уж-хорошо">По традиции список твоих фраз, которые заставили почувствовать тепло, улыбнуться, или просто звучали слишком уж хорошо:</a></li>
  </ul>
</nav>
    </div>
<!-- main -->
<main class="content" id="quarto-document-content">

<header id="title-block-header" class="quarto-title-block default">
<div class="quarto-title">
<h1 class="title">BDay page v{version}</h1>
</div>



<div class="quarto-title-meta">

    
  
    
  </div>
  

</header>

{markdown.markdown(content)}

<div class="float" id="btnConfetti">
  <img src="icon.png">
</div>

<nav class="page-navigation">
  <div class="nav-page nav-page-previous">
    {f'<a href="./{prev_page}" class="pagination-link"><i class="bi bi-arrow-left-short"></i> <span class="nav-page-text">Version {prev_page.replace("v", "").replace(".html", "")}</span></a>' if prev_page else ''}
  </div>
  <div class="nav-page nav-page-next">
    {f'<a href="./{next_page}" class="pagination-link"><span class="nav-page-text">Version {next_page.replace("v", "").replace(".html", "")}</span> <i class="bi bi-arrow-right-short"></i></a>' if next_page else ''}
  </div>
</nav>

</main>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
<script src="confetti.js"></script>
<script src="menu.js"></script>

<footer class="footer">
  <div class="nav-footer">
    <div class="nav-footer-left">
    </div>   
    <div class="nav-footer-center">
      <p>Gern gemacht</p>
    </div>
    <div class="nav-footer-right">
      &nbsp;
    </div>
  </div>
</footer>

</body></html>'''
    
    return template

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    version = request.form['version']
    content = request.form['content']
    prev_page = request.form['prev_page']
    next_page = request.form['next_page']
    
    html_content = generate_html(version, content, prev_page, next_page)
    
    # Создаем файл
    filename = f'v{version}.html'
    with open(os.path.join('docs', filename), 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return f'Page generated successfully: {filename}'

if __name__ == '__main__':
    app.run(debug=True) 