<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta name="viewport" content="width=240px, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">

<title>大阪メンズアロママッサージサロン メンズエステ ミスミセス</title>
<meta name="copyright" content="大阪メンズエステ ミスミセス">
<meta name="Author" content="大阪メンズエステ「ミスミセス」の公式ページです。エステティシャンの紹介やスケジュール、ヘルス&エステ講座、料金システム、イベントなどの紹介">
<meta name="keywords" content="エステ,メンズ,大阪,ギャル系,携帯,美少女,激安,格安">


<meta name="robots" content="ALL">
<style type="text/css"><!--BODY{ font-family : Verdana;}--></style>
</head>
<body link="#132901" vlink="#132901" alink="#990000" bgcolor="#ffffff" text="#160f04" topmargin="0">
<a name="top"></a>

<table border="0" cellpadding="2" cellspacing="1" width="100%">
<tr>
<td bgcolor="#000000" align="center"><font size="1" color="#ffffff">大阪メンズエステアロママッサージサロン</font></td>
</tr>
</table>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="1">
<tr>
<td bgcolor="#000000"></td>
</tr>
</table>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="1">
<tr>
<td bgcolor="#212121">
<div align="center"><img src="img/logo.gif" border="0" alt="大阪ミスミセス"></div>
</td>
</tr>
</table>

<div align="center"><img src="img/line01.gif" border="0"></div>

<div align="center"><img src="img/kira14.gif" width="9" height="11" border="0"><font size="1">大阪メンズエステ<br>
<img src="img/kira06.gif" width="9" height="11" border="0"></font><font size="2" color="#479100"><b><u>ミスミセス</u></b></font><font size="1"><br>
<img src="img/ico_phone2_6.gif" width="14" height="11" border="0"><a href="tel:090-3053-0184">電話/090-3053-0184</a><br>
<img src="img/ico_star1.gif" width="11" height="11" border="0"></font><font size="1" color="#ff0080"><font color="#ff0080"><u>11時-翌朝5時迄営業中</u></font></font></div>

<div align="center"><img src="img/line01.gif" border="0"></div>

<font color="#ffffff" size="2"><marquee bgcolor="#000000" direction="left" loop="0" style="padding-top : 2px;padding-left : 1px;padding-right : 1px;padding-bottom : 2px;">ミスミセスが贈る至福の体験・メンズエステの真髄をお楽しみください</marquee></font>

<div align="center"><img src="img/line01.gif" border="0"></div>

<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td bgcolor="#222222" align="left"><font size="2" color="#ffffff"><img src="img/ico_search1.gif" width="14" height="14" border="0">新着情報</font></td>
</tr>
</table>

<div align="center"><img src="img/line01.gif" border="0"></div>

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
define("MAGPIE_OUTPUT_ENCODING","Shift_JIS");
// 取得したいRSSのurl
$url = "http://feedblog.ameba.jp/rss/ameblo/missmrs/rss20.xml";
// ブログのタイトルは$rss->channel['title']という変数、
// RSSは$rss->itemという変数に入る。
// key値、link/title/descriptionで取得できる。
$rss = fetch_rss( $url );
//var_dump ($rss);
$max_lines = 2;
$line = 0;
//echo "". mb_convert_encoding($rss->channel['title'],"UTF-8","auto");
foreach ($rss->items as $item) {
$link = mb_convert_encoding($item['link'],"Shift_JIS","auto");
$title = mb_convert_encoding($item['title'],"Shift_JIS","auto");
$description = mb_convert_encoding($item['description'],"Shift_JIS","auto");
$date = date("Y/m/d", intval($item['date_timestamp']));
if (preg_match("/PR$/", $title) != 0) continue;
if (preg_match("/^PR:.+$/", $title) != 0) continue;
if ($line++ == $max_lines) break;
//echo "<a href=$link>$title</a><br />$description";
echo "<table><tr><td>$date</td><td><a href=\"$link\" target=\"_blank\">$title</a></td></tr></table><div align=\"center\"><img src=\"img/line01.gif\" border=\"0\"></div>";
}
?>

<div align="right"><font size="1"><a href="#top">▲PAGE TOP</a></font></div>

<div align="center"><img src="img/line01.gif" border="0"></div>

<font color="#ffffff" size="2"><marquee bgcolor="#000000" direction="left" loop="0" style="padding-top : 2px;padding-left : 1px;padding-right : 1px;padding-bottom : 2px;">営業時間 11：00 〜 翌5：00</marquee></font>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="4">
<tr>
<td bgcolor="#111111" align="center"><font color="#fffdfe" size="2"><a name="menu">MENU</a></font></td>
</tr>
</table>
<table border="0" cellpadding="2" cellspacing="1" width="100%">
<tr>
<td bgcolor="#e4dccc"><font size="2"><a href="./index.php">[1]TOPページ</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="/contents/girls/girls.cgi?mobile=1">[2]セラピスト一覧</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="http://ameblo.jp/missmrs/theme-10084892532.html">[3]出勤情報</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="./system.html">[4]料金システム</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="./recruit.html">[5]求人情報</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="./access.html">[6]アクセス</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="mailto:missmrs@docomo.ne.jp">[7]お問い合わせ</a></font></td>
</tr>
</table>

<div align="right"><font size="1"><a href="#top">▲PAGE TOP</a></font></div>
<div align="center"><img src="img/line01.gif" border="0"></div>

<table border="0" width="100%" cellpadding="2" cellspacing="1">
<tr>
<td align="center" bgcolor="#000000"><img src="img/ico13..gif" border="0"><font color="#ffffff" size="2">注意事項</font></td>
</tr>
</table>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="3">
<tr>
<td bgcolor="#00000"></td>
</tr>
</table>

<div><font size="1" color="#cc0000">当ホームページで使用している内容、画像の無断転載は禁止いたします。</font></div>

<div align="center"><font size="1"><img src="img/copy.gif" border="0">大阪ミスミセス</font></div>

</div>

</body>
</html>
