<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta name="viewport" content="width=320px, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
<title>大阪メンズアロママッサージサロン メンズエステ ミスミセス</title>
<meta name="copyright" content="大阪メンズエステ ミスミセス">
<meta name="Author" content="大阪メンズエステ「ミスミセス」の公式ページです。エステティシャンの紹介やスケジュール、ヘルス&エステ講座、料金システム、イベントなどの紹介">
<meta name="keywords" content="エステ,メンズ,大阪,ギャル系,携帯,美少女,激安,格安">
<link rel="stylesheet" type="text/css" href="./index.css" media="all">
<meta name="robots" content="ALL">
</head>
<body link="#132901" vlink="#132901" alink="#990000" bgcolor="#ffffff" text="#160f04" topmargin="0">
<a name="top"></a>

<div style="width:100%;background:#212121;overflow:hidden;">
<div style="float:left;margin:3px 0 3px 5px;"><img src="img/logo.gif" border="0" width="120" alt="大阪ミスミセス"></div>
<div  class="headmenu"><a href="tel:090-3053-0184">090-3053-0184</a></div>
</div>

<div style="padding:5px 0;background:#000000;width:100%;color:#fff;overflow:hidden;">大阪メンズエステ ミスミセス</div>

<font color="#ffffff" size="2"><marquee bgcolor="#000000" direction="left" loop="0" style="padding-top : 5px;padding-left : 1px;padding-right : 1px;padding-bottom : 5px;">ミスミセスが贈る至福の体験・メンズエステの真髄をお楽しみください</marquee></font>

<div class="tel">営業時間:11時-翌朝5時まで</div>

<div style="margin-bottom:5px;padding:5px 0;background:#000;width:100%;color:#fff;overflow:hidden;">新着情報</div>

<div style="margin:5px 0;overflow:hidden;">
<?php
// モジュールを読み込む
require_once("../magpierss/rss_fetch.inc");
// キャッシュ期間を秒数にて設定
// 例では30分
define("MAGPIE_CACHE_AGE", 60*1);
// キャッシュディレクトリへのパスを設定
// キャッシュディレクトリをchmod 777 (or 707 or 700)
define("MAGPIE_CACHE_DIR", "/path/2/cache/");
// 日本語バケないためにOUTPUT_ENCODINGをUTF-8にする
define("MAGPIE_OUTPUT_ENCODING","UTF-8");
// 取得したいRSSのurl
$url = "http://blog.livedoor.jp/missmrs02/atom.xml";
// ブログのタイトルは$rss->channel['title']という変数、
// RSSは$rss->itemという変数に入る。
// key値、link/title/descriptionで取得できる。
$rss = fetch_rss( $url );
//var_dump ($rss);
$max_lines = 9;
$line = 0;
//echo "". mb_convert_encoding($rss->channel['title'],"UTF-8","auto");
foreach ($rss->items as $item) {
$link = mb_convert_encoding($item['link'],"UTF-8","auto");
$title = mb_convert_encoding($item['title'],"UTF-8","auto");
$description = mb_convert_encoding($item['description'],"UTF-8","auto");
$date = date("Y/m/d H:i", intval($item['date_timestamp']));
if (preg_match("/PR$/", $title) != 0) continue;
if (preg_match("/^PR:.+$/", $title) != 0) continue;
if ($line++ == $max_lines) break;
//echo "<a href=$link>$title</a><br />$description";
echo "<div style=\"margin:5px 0;overflow:hidden;\"><a href=\"$link\" target=\"_blank\"><div class=\"news\"><div class=\"n_time\"><!--$date--></div><div class=\"n_tit\">$title</div></a></div>";
}
?>
</div>

<div style="padding:5px 0;background:#000000;width:100%;color:#fff;overflow:hidden;">MENU</div>
<div style="margin-right:5px;width:100%;overflow:hidden;">
<div class="menu"><a href="./index.php">トップページ</a></div>
<div class="menu"><a href="/contents/sgirls/girls.cgi?mobile=1">セラピスト一覧</a></div>
<div class="menu"><a href="http://blog.livedoor.jp/missmrs02/" target="_blank">出勤情報</a></div>
<div class="menu"><a href="./system.html">料金システム</a></div>
</div>

<div style="margin:10px 0 5px;padding:5px 0;background:#000000;width:100%;color:#fff;overflow:hidden;">アクセス</div>
<div class="tel"><a href="./access.html#1">南森町店</a></div>
<div class="tel"><a href="./access.html#2">扇町店</a></div>
<div class="tel"><a href="./access.html#3">天神橋六丁目店</a></div>
<div class="tel"><a href="./access.html#4">長堀橋店</a></div>

<div align="right"><font size="1"><a href="#top">▲PAGE TOP</a></font></div>

<div style="margin-bottom:0px;padding:5px 0;background:#000000;width:100%;color:#fff;font-size:12px;overflow:hidden;">Copyright (C) MissMrs.</div>

</div>

</body>
</html>
