<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta name="viewport" content="width=240px, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">

<title>��チ���Y�A���}�}�b�T�[�W�T���� �����Y�G�X�e �~�X�~�Z�X</title>
<meta name="copyright" content="��チ���Y�G�X�e �~�X�~�Z�X">
<meta name="Author" content="��チ���Y�G�X�e�u�~�X�~�Z�X�v�̌����y�[�W�ł��B�G�X�e�e�B�V�����̏Љ��X�P�W���[���A�w���X&�G�X�e�u���A�����V�X�e���A�C�x���g�Ȃǂ̏Љ�">
<meta name="keywords" content="�G�X�e,�����Y,���,�M�����n,�g��,������,����,�i��">


<meta name="robots" content="ALL">
<style type="text/css"><!--BODY{ font-family : Verdana;}--></style>
</head>
<body link="#132901" vlink="#132901" alink="#990000" bgcolor="#ffffff" text="#160f04" topmargin="0">
<a name="top"></a>

<table border="0" cellpadding="2" cellspacing="1" width="100%">
<tr>
<td bgcolor="#000000" align="center"><font size="1" color="#ffffff">��チ���Y�G�X�e�A���}�}�b�T�[�W�T����</font></td>
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
<div align="center"><img src="img/logo.gif" border="0" alt="���~�X�~�Z�X"></div>
</td>
</tr>
</table>

<div align="center"><img src="img/line01.gif" border="0"></div>

<div align="center"><img src="img/kira14.gif" width="9" height="11" border="0"><font size="1">��チ���Y�G�X�e<br>
<img src="img/kira06.gif" width="9" height="11" border="0"></font><font size="2" color="#479100"><b><u>�~�X�~�Z�X</u></b></font><font size="1"><br>
<img src="img/ico_phone2_6.gif" width="14" height="11" border="0"><a href="tel:090-3053-0184">�d�b/090-3053-0184</a><br>
<img src="img/ico_star1.gif" width="11" height="11" border="0"></font><font size="1" color="#ff0080"><font color="#ff0080"><u>11��-����5�����c�ƒ�</u></font></font></div>

<div align="center"><img src="img/line01.gif" border="0"></div>

<font color="#ffffff" size="2"><marquee bgcolor="#000000" direction="left" loop="0" style="padding-top : 2px;padding-left : 1px;padding-right : 1px;padding-bottom : 2px;">�~�X�~�Z�X�����鎊���̑̌��E�����Y�G�X�e�̐^�������y���݂�������</marquee></font>

<div align="center"><img src="img/line01.gif" border="0"></div>

<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td bgcolor="#222222" align="left"><font size="2" color="#ffffff"><img src="img/ico_search1.gif" width="14" height="14" border="0">�V�����</font></td>
</tr>
</table>

<div align="center"><img src="img/line01.gif" border="0"></div>

<?php
// ���W���[����ǂݍ���
require_once("../magpierss/rss_fetch.inc");
// �L���b�V�����Ԃ�b���ɂĐݒ�
// ��ł�30��
define("MAGPIE_CACHE_AGE", 60*1);
// �L���b�V���f�B���N�g���ւ̃p�X��ݒ�
// �L���b�V���f�B���N�g����chmod 777 (or 707 or 700)
define("MAGPIE_CACHE_DIR", "/path/2/cache/");
// ���{��o�P�Ȃ����߂�OUTPUT_ENCODING��UTF-8�ɂ���
define("MAGPIE_OUTPUT_ENCODING","Shift_JIS");
// �擾������RSS��url
$url = "http://feedblog.ameba.jp/rss/ameblo/missmrs/rss20.xml";
// �u���O�̃^�C�g����$rss->channel['title']�Ƃ����ϐ��A
// RSS��$rss->item�Ƃ����ϐ��ɓ���B
// key�l�Alink/title/description�Ŏ擾�ł���B
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

<div align="right"><font size="1"><a href="#top">��PAGE TOP</a></font></div>

<div align="center"><img src="img/line01.gif" border="0"></div>

<font color="#ffffff" size="2"><marquee bgcolor="#000000" direction="left" loop="0" style="padding-top : 2px;padding-left : 1px;padding-right : 1px;padding-bottom : 2px;">�c�Ǝ��� 11�F00 �` ��5�F00</marquee></font>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="4">
<tr>
<td bgcolor="#111111" align="center"><font color="#fffdfe" size="2"><a name="menu">MENU</a></font></td>
</tr>
</table>
<table border="0" cellpadding="2" cellspacing="1" width="100%">
<tr>
<td bgcolor="#e4dccc"><font size="2"><a href="./index.php">[1]TOP�y�[�W</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="/contents/girls/girls.cgi?mobile=1">[2]�Z���s�X�g�ꗗ</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="http://ameblo.jp/missmrs/theme-10084892532.html">[3]�o�Ώ��</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="./system.html">[4]�����V�X�e��</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="./recruit.html">[5]���l���</a></font></td>
</tr><tr>
<td bgcolor="#efeae0"><font size="2"><a href="./access.html">[6]�A�N�Z�X</a></font></td>
</tr><tr>
<td bgcolor="#e4dccc"><font size="2"><a href="mailto:missmrs@docomo.ne.jp">[7]���₢���킹</a></font></td>
</tr>
</table>

<div align="right"><font size="1"><a href="#top">��PAGE TOP</a></font></div>
<div align="center"><img src="img/line01.gif" border="0"></div>

<table border="0" width="100%" cellpadding="2" cellspacing="1">
<tr>
<td align="center" bgcolor="#000000"><img src="img/ico13..gif" border="0"><font color="#ffffff" size="2">���ӎ���</font></td>
</tr>
</table>

<table border="0" cellpadding="2" cellspacing="1" width="100%" height="3">
<tr>
<td bgcolor="#00000"></td>
</tr>
</table>

<div><font size="1" color="#cc0000">���z�[���y�[�W�Ŏg�p���Ă�����e�A�摜�̖��f�]�ڂ͋֎~�������܂��B</font></div>

<div align="center"><font size="1"><img src="img/copy.gif" border="0">���~�X�~�Z�X</font></div>

</div>

</body>
</html>