#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);
#��������������������������������
# WORK DISPLAY SYSTEM
# Copyright (c) 
#               ARMS DESIGN INC.
#��������������������������������
require './set.cgi';

&decode;
$title = $shopname.'�Ǘ�';
	if ($in{'pass'} ne $pass) { &error("�p�X���[�h���Ⴂ�܂�"); }

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=Shift-JIS" />
		<title>�o�ΊǗ�</title>
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<meta http-equiv="imagetoolbar" content="no">
</head>
<body bgcolor="#ffffff">

	<form action="$girlscript" method="post">
		<input type="hidden" name="pass" value="$in{'pass'}">
		<input type="submit" value="�����L���X�g���">
	</form>

	<form action="$workscript" method="post">
		<input type="hidden" name="pass" value="$in{'pass'}">
		<input type="hidden" name="cmd" value="list">
		<input type="submit" value="�X�P�W���[�����">
	</form>

</body>
</html>
EOM
exit;