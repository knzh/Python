 <!DOCTYPE html>
<html>
<head>
    <title>xpath test</title>
</head>
<body>
<div price="99.8">
    <div>
        <ul>
            <li>时间</li>
            <li>地点</li>
            <li>任务</li>
        </ul>
    </div>
    <div id='testid' data-h="first">
        <h2>这里是个小标题</h2>
        <ol>
            <li data="one">1</li>
            <li data="two">2</li>
            <li data="three">3</li>
        </ol>
        <ul>
            <li code="84">84</li>
            <li code="104">104</li>
            <li code="223">223</li>
        </ul>
    </div>
    <div>
        <h3>这里是H3的内容
            <a href="http://www.baidu.com">百度一下</a>
            <ul>
                <li>test1</li>
                <li>test2</li>
            </ul>
        </h3>
    </div>
    <div id="go">
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
            <li>6</li>
            <li>7</li>
            <li>8</li>
            <li>9</li>
            <li>10</li>
        </ul>
    </div>
</div>
</body>
</html>
print tree.xpath('//@code')