def tag_cl(lst_x):
    lst_tags=['<div>','</div>','<a>','</a>','<td>','</td>','<h1>','</h1>','<li>','</li>','</button>','<button>',"<!DOCTYPE>", "<html>", "<head>", "<title>", "<meta>", "<link>", "<style>", "<script>", 
    "<body>", "<header>", "<nav>", "<main>", "<section>", "<article>", "<aside>", "<footer>", 
    "<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<p>", "<a>", "<img>", "<ul>", "<ol>", 
    "<li>", "<table>", "<tr>", "<th>", "<td>", "<div>", "<span>", "<form>", "<input>", "<button>", 
    "<select>", "<option>", "<textarea>", "<label>", "<fieldset>", "<legend>", "<iframe>", "<audio>", 
    "<video>", "<canvas>", "<svg>", "<embed>", "<object>", "<param>", "<br>", "<hr>", "<strong>", 
    "<em>", "<mark>", "<small>", "<del>", "<ins>", "<code>", "<pre>", "<blockquote>", "<cite>", 
    "<abbr>", "<address>", "<b>", "<i>", "<u>", "<sup>", "<sub>", "<time>", "<data>", "<var>", 
    "<samp>", "<kbd>", "<progress>", "<meter>", "<datalist>", "<output>", "<details>", "<summary>", 
    "<dialog>", "<canvas>", "<noscript>",'</tr>','</table>','<div','</h2>','hover','class','std100','<table','<span','style="font-size:.8em">','(ILOEST)',
    '</span>','</tr>','&#216']
    lst_clean=[]
    for data in lst_x:
        for tag in lst_tags:
            data = data.replace(tag, '')
        lst_clean.append(data)    
    return lst_clean        