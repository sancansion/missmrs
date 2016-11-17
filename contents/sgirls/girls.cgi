#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);
#────────────────
# Copyright (c) ARMS DESIGN INC.
# webmaster@arms.vc
# http://www.arms.vc/
#────────────────
require './common.cgi';

&decode;
print "Content-type: text/html\n\n";


local($retu, $mchar, $mobmode, $cnt, @namesort, @namesort2, @staffdata);
$retu  = 3;
$ext   = ".html";

if($in{'mobile'}) {
	$mchar   = "m";
	$ext     = ".xhtml";
	$mobmode = "&mobile=1";
}

if($in{'mode'} eq 'work') {
	$tmpfile = "work$mchar$ext";

} elsif($in{'mode'} eq 'new') {
	$tmpfile = "newface$mchar$ext";

} else {
	$tmpfile = "girls$mchar$ext";
}
$m1 = "";$m2 = "";$m3 = "";$m4 = "";$m5 = "";
if ($in{'modest'} == 1) {	$m1 = 'ア'; $m2 = 'イ'; $m3 = 'ウ'; $m4 = 'エ'; $m5 = 'オ';}
if ($in{'modest'} == 2) {	$m1 = 'カ'; $m2 = 'キ'; $m3 = 'ク'; $m4 = 'ケ'; $m5 = 'コ';}
if ($in{'modest'} == 3) {	$m1 = 'サ'; $m2 = 'シ'; $m3 = 'ス'; $m4 = 'セ'; $m5 = "0x835C";}
if ($in{'modest'} == 4) {	$m1 = 'タ'; $m2 = 'チ'; $m3 = 'ツ'; $m4 = 'テ'; $m5 = 'ト';}
if ($in{'modest'} == 5) {	$m1 = 'ナ'; $m2 = 'ニ'; $m3 = 'ヌ'; $m4 = 'ネ'; $m5 = 'ノ';}
if ($in{'modest'} == 6) {	$m1 = 'ハ'; $m2 = 'ヒ'; $m3 = 'フ'; $m4 = 'ヘ'; $m5 = 'ホ';}
if ($in{'modest'} == 7) {	$m1 = 'マ'; $m2 = 'ミ'; $m3 = 'ム'; $m4 = 'メ'; $m5 = 'モ';}
if ($in{'modest'} == 8) {	$m1 = 'ヤ'; $m2 = 'ユ'; $m3 = 'ヨ';}
if ($in{'modest'} == 9) {	$m1 = 'ラ'; $m2 = 'リ'; $m3 = 'ル'; $m4 = 'レ'; $m5 = 'ロ';}
if ($in{'modest'} == 10) {	$m1 = 'ワ'; $m2 = 'ヲ';}

$scmnd = $in{'search'};

#-------------
# TEMPLATE
#-------------
	open(IN,"$tmpfile") || &error("Open Error: $tmpfile");
	while (<IN>) {
		push(@head,$_) if (!$flag);

		if (/<!-- line1 -->/) { $flag=1; }
		elsif (/<!-- line2 -->/) { $flag=2; }

		if ($flag == 1) { $loop .= $_; }
		elsif ($flag == 2) { push(@foot,$_); }
	}
	close(IN);

#-------------
# DATA
#-------------
if ($in{'mode'} eq "work") {
	&workDatGet;
} else {
	open(IN,"$logfile");
	@file = <IN>;
	close(IN);

	@file = sort { (split(/<>/, $a))[2] cmp (split(/<>/, $b))[2] } @file;

	foreach (@file) {
		($no, $id, $namae) = split(/<>/);
		if ($in{'modest'}) {
			if ( $namae =~ /^($m1|$m2|$m3|$m4|$m5)/ ){
				push (@namesort, "$_\n");
			} else {
				push (@namesort2, "$_\n");
			}
		} else {
			push (@namesort2, "$_\n");
		}
	}


	$flg = $#file + 1;

	@num = &StartRandom($flg);
	$cnt = 0;
	foreach (@namesort2) {
		$_ =~ s/\n//g;
		push(@staffdata, "$_<><>$num[$cnt]<>\n");
		$cnt++;
	}
	@staffdata = sort { (split(/<>/, $a))[30] <=> (split(/<>/, $b))[30] } @staffdata;

	push (@namesort, @staffdata);
}

	$cnt = 0;
	foreach (@namesort) {

		$msg = $loop;
		local($smemo, $newmsg, $datemsg, $imgmsg, $kosu, $imemo, $workmsg, $skmsg, $upmsg, $eucid, $eucnamae);
		($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up, $st, $tim) = split(/<>/);
		next if $display;
		$i++;

		if ($scmnd) {
			$eucid = $id;
			$eucnamae = $namae;
			&jcode'convert(*eucid, 'euc');
			&jcode'convert(*eucnamae, 'euc');

			next if(!($eucid =~ /$scmnd/) && !($eucnamae =~ /$scmnd/));
		}

		if($in{'mode'} eq 'new') {
			next if !$new;
		}


		if ($in{'mobile'}) {
			$imgmsg = "<img src=\"$imgdir/$id/$id.jpg\" width=\"60\" />";
		} else {
			$imgmsg = "<img src=\"$imgdir/$id/$id.jpg\" width=\"140\" />";
		}

		if($todaywork{$no}) {	$workmsg   = " 本日出勤";}
		if($nextwork{$no})	{	$workmsg .= " 明日出勤";		}

		if($new) 			{	$newmsg = "<img src=\"$simgdir/new.gif\" />";	 $datemsg = "$entermon/$enterday";}
		if($taiken) 		{	$newmsg = "<img src=\"$simgdir/taiken.gif\" />"; $datemsg = "$entermon/$enterday";}

		if($up) 			{	$upmsg = "<img src=\"$simgdir/up.gif\" />";		}
		if($nosmoke) 		{	$skmsg = "<img src=\"$simgdir/tabaco.gif\" />";	}

		if($blog) {
			if ($in{'mobile'}) {
				$blog = "<a href=\"$blogurl1m$blog$blogurl2m\"><img src=\"$simgdir/syame.jpg\"></a>";
			} else {
				$blog = "<a href=\"$blogurl1$blog$blogurl2\" target=\"_blank\"><img src=\"$simgdir/syame.jpg\"></a>";
			}
		}

		$coms = zanStr (82, $com);

		if (!$cnt){
			$msg =~ s|!tr!|<tr>|g;
		} else {
			$msg =~ s/!tr!//g;
		}
		$msg =~ s/!image!/$imgmsg/i;
		$msg =~ s/!id!/$id/g;
		$msg =~ s/!name!/$namae/i;
		$msg =~ s/!age!/$age/i;
		$msg =~ s/!hei!/$hei/i;
		$msg =~ s/!bust!/$bu/i;
		$msg =~ s/!cup!/$cup/i;
		$msg =~ s/!waist!/$wa/i;
		$msg =~ s/!hip!/$hip/i;
		$msg =~ s/!newmsg!/$newmsg/i;
		$msg =~ s/!entermon!/$entermon/i;
		$msg =~ s/!enterday!/$enterday/i;
		$msg =~ s/!enter!/$datemsg/i;
		$msg =~ s/!workmsg!/$workmsg/i;
		$msg =~ s/!blog!/$blog/i;
		$msg =~ s/!img!/$imgmsg/i;
		$msg =~ s/!tabaco!/$skmsg/i;
		$msg =~ s/!up!/$upmsg/i;
		$msg =~ s/!coms!/$coms/i;
		$msg =~ s/!worktime!/$tim/i;

		if ($ch1) {$msg =~ s|!ch1!|<img src=\"$simgdir/feature/$ch1.jpg\" />|i;	} else {$msg =~ s/!ch1!/$ch1/i;}
		if ($ch2) {$msg =~ s|!ch2!|<img src=\"$simgdir/feature/$ch2.jpg\" />|i;	} else {$msg =~ s/!ch2!/$ch2/i;}
		if ($ch3) {$msg =~ s|!ch3!|<img src=\"$simgdir/feature/$ch3.jpg\" />|i;	} else {$msg =~ s/!ch3!/$ch3/i;}

		$cnt++;
		if ($cnt == $retu){
			$msg =~ s|!tr2!|</tr>|g;
			$cnt = 0;
		} else {
			$msg =~ s/!tr2!//g;
		}
		push(@loop, $msg);
	}




	foreach (@head) {
		&jcode'convert(*scmnd, 'sjis');
		s|!today!|$today|;
		s|!ninzu!|$girlsninzu|;
		s|!update!|$stateupdate|;
		s|!d0!|$sname[0]|;
		s|!d1!|$sname[1]|;
		s|!d2!|$sname[2]|;
		s|!d3!|$sname[3]|;
		s|!d4!|$sname[4]|;
		s|!d5!|$sname[5]|;
		s|!d6!|$sname[6]|;
		s|!d7!|$sname[7]|;
		s|!btn0!|$bval[0]|;
		s|!btn1!|$bval[1]|;
		s|!btn2!|$bval[2]|;
		s|!btn3!|$bval[3]|;
		s|!btn4!|$bval[4]|;
		s|!btn5!|$bval[5]|;
		s|!btn6!|$bval[6]|;
		s|!btn7!|$bval[7]|;
		if($scmnd){s|!search!|「$scmnd」を検索|; } else {s|!search!||;}
		print;
	}

	print @loop;

	foreach (@foot) {
		print;
	}
	exit;



sub workDatGet {
	($nowyear, $nowmon, $nowday) = &time;
	$nowwkey = &get_week($nowday, $nowyear, $nowmon);
	$lastday = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) [$nowmon-1]
	+ ($nowmon == 2 && (($nowyear % 4 == 0 && $nowyear % 100 != 0) || $nowyear % 400 == 0));

	if ($in{'date'} eq "") {
		$viewyear = $nowyear;
		$viewmon = $nowmon;
		$viewday = $nowday;
		$flg = sprintf("%04d/%02d/%02d", $viewyear, $viewmon, $viewday);

	} else {
		($viewyear, $viewmon, $viewday) = split(/\D/, $in{'date'});
	}
	$wkey = &get_week($viewday, $viewyear, $viewmon);
	$today = "$viewmon/$viewday($week[$wkey])";

	$dispday = $nowday;
	$dispmon = $nowmon;
	$dispyear = $nowyear;
	$dispwkey = $nowwkey;

	for ($i = 0; $i <= 6; $i++){
		if ($in{'mobile'}) {
			$sname[$i] = "$gscriptm$dispyear/$dispmon/$dispday";
		} else {
			$sname[$i] = "$gscript$dispyear/$dispmon/$dispday";
		}
		$bval[$i] = "$dispmon/$dispday($week[$dispwkey])";

		$dispday++;

		if ($lastday < $dispday){	#月をまたぐとき
			++$dispmon;
			$dispday = 1;
		}
		if ($dispmon > 12){	#年をまたぐとき
			++$dispyear;
			$dispmon = 1;
		}
		$dispwkey++;
		if ($dispwkey == 7){$dispwkey = 0;}
	}

	@namesort = &workData($viewyear, $viewmon, $viewday);
}

__END__
