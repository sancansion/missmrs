#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);
#────────────────
# WORK DISPLAY SYSTEM
# Copyright (c) 
#               ARMS DESIGN INC.
#────────────────
require './set.cgi';

&decode;
$title = $shopname.'管理';
	if ($in{'pass'} ne $pass) { &error("パスワードが違います"); }

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
		<title>出勤管理</title>
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<meta http-equiv="imagetoolbar" content="no">
</head>
<body bgcolor="#ffffff">

	<form action="$girlscript" method="post">
		<input type="hidden" name="pass" value="$in{'pass'}">
		<input type="submit" value="女性キャスト情報">
	</form>

	<form action="$workscript" method="post">
		<input type="hidden" name="pass" value="$in{'pass'}">
		<input type="hidden" name="cmd" value="list">
		<input type="submit" value="スケジュール情報">
	</form>

</body>
</html>
EOM
exit;