#!/usr/bin/perl

require './set.cgi';

#-------------
# GIRL data
#-------------
	%girlname   = ();
	@girlnodata = ();
	%checknew   = ();
	open(IN,"$girlfile");
	while(<IN>){
		($gno, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $blood, $before, $tech, $feeling, $charm, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display) = split(/<>/);

		$girlname{$gno} = $namae;
		$girlid{$gno}   = $id;
		$girlage{$gno}  = $age;
		$girlhei{$gno}  = $hei;
		$girlbu{$gno}   = $bu;
		$girlwa{$gno}   = $wa;
		$girlhip{$gno}  = $hip;
		$girlcup{$gno}  = $cup;
		$checknew{$gno} = $new;
		$checkimg{$gno} = $t;
		$checktaiken{$gno} = $taiken;
		push(@girlnodata, $gno);
	}
	close(IN);


#-------------
# WORK data
#-------------
sub workData {
	my(@commonworkdata, $data);
	my($year, $month, $day) = @_;
	$datadir = "$year$month";

	foreach $gno (@girlnodata) {
		if (-e "$workdir/$datadir/$gno.cgi") {
			open(WORK, "$workdir/$datadir/$gno.cgi");
			while (<WORK>) {
				($workday, $start, $end) = split(/<>/);
				if ($workday == $day && ($start || $end) && $girlname{$gno}) {
					$data = "$gno<>$start<>$end<>";
					push(@commonworkdata,"$data\n");
					push(@workdatano, $gno);
				}
			}
			close(WORK);
		}
	}
	$girlsninzu = $#commonworkdata + 1;
	return @commonworkdata;
}


#----------------#
#  デコード処理  #
#----------------#
sub decode {
	local($key,$val);

	&ReadParse;
	while ( ($key,$val) = each %in ) {

		if ($key !~ /^upfile/) {

			# シフトJISコード変換
			&jcode'convert(*val, 'sjis');

			# タグ処理
			$val =~ s/<>/&LT;&GT;/g;
			$val =~ s/&/&amp;/g;
			$val =~ s/"/&quot;/g;
			$val =~ s/</&lt;/g;
			$val =~ s/>/&gt;/g;

			# 改行処理
			if ($key eq "comment") {
				$val =~ s/\r\n/<br>/g;
				$val =~ s/\r/<br>/g;
				$val =~ s/\n/<br>/g;
			} else {
				$val =~ s/\r//g;
				$val =~ s/\n//g;
			}
		}
		$in{$key} = $val;
	}
	$mode = $in{'mode'};
	$page = $in{'page'};
}
sub parseInput {
	if ($ENV{'REQUEST_METHOD'} eq "GET") {
		$query_string = $ENV{'QUERY_STRING'};
	}
	elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
	}
	@a = split(/&/, $query_string);
	foreach $x (@a) {
		($key, $val) = split(/=/, $x);
		$val =~ tr/+/ /;
		$val =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
		$val =~ s/[\r\n]+/\n/g;
		&jcode'convert(*val, "sjis");
		$in{$key} = $val;
	}
	return *in;
}

#--------------#
#  HTMLヘッダ  #
#--------------#
sub header {
	if ($headflag) { return; }

	print "Content-type: text/html\n\n";
	print <<"EOM";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
	<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS">
	<title>出勤情報</title>
	<meta name="robots" content="noindex,nofollow">
	<meta name="robots" content="noarchive">
	<meta http-equiv="Content-Style-Type" content="text/css">
	<meta http-equiv="Content-Script-Type" content="text/javascript">
	<link rel="stylesheet" type="text/css" href="work.css">
</head>
<body>
<div align="center">
EOM
	$headflag=1;
}


#--------------#
#  エラー処理  #
#--------------#
sub error {
	&header;
	print <<"EOM";
<div align="center">
<h3>ERROR !</h3>
<font color="red">$_[0]</font>
<p>
<form>
<input type=button value="前画面に戻る" onClick="history.back()">
</form>
</div>
EOM
	print &HtmlBot;
	exit;
}
#--------------#
#  ロック処理  #
#--------------#
sub lock {
	local($retry)=5;
	# 1分以上古いロックは削除する
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime && $mtime < time - 60) { &unlock; }
	}
	while (!mkdir($lockfile, 0755)) {
		if (--$retry <= 0) { &error('lock error');}
		sleep(1);
	}
	$lockflag=1;
}

#--------------#
#  ロック解除  #
#--------------#
sub unlock {
	rmdir($lockfile);
	$lockflag=0;
}


#-----------------#
#  小数点         #
#-----------------#
sub round {
	my ($num, $decimals) = @_;
	my ($format, $magic);
	$format = '%.' . $decimals . 'f';
	$magic = ($num > 0) ? 0.5 : -0.5;
	sprintf($format, int(($num * (10 ** $decimals)) + $magic) / (10 ** $decimals));
}



#--------------#
#  日付処理    #
#--------------#
sub get_week {
	local($day, $year, $month) = @_;

	if ($month < 3) {
		$year--;
		$month += 12;
	}
	int ($year + int ($year/4) - int ($year/100) + int ($year/400) + int ((13*$month+8)/5) + $day) % 7;
}
sub time{
	$ENV{'TZ'} = "JST-3";
	($sec, $min, $hour, $mday, $mon, $year, $wday) = localtime();
	$year = $year + 1900;
	$mon = sprintf("%d", $mon +1);
	$mday = sprintf("%d", $mday);
	return ($year, $mon, $mday);
}



#--------------#
# make file date
#--------------#

sub makeFile {
	local($year, $month, $no, $dir) = @_;
	mkdir "$dir/$year$month", 0707;
	@files = ("$dir/$year$month");
	chmod 0777, @files;

	if (-e "$dir/$year$month/$no.cgi") {}
	else {
		open(FILE, ">$dir/$year$month/$no.cgi");
		close(FILE);

		@files = ("$dir/$year$month/$no.cgi");
		chmod 0666, @files;
	}
}


sub makePDir {
	local($name) = @_;

	mkdir "$imgdir/$name", 0707;
	@files = ("$imgdir/$name");
	chmod 0777, @files;

	mkdir "$imgdir/$name/$imgmdir", 0707;
	@files = ("$imgdir/$name/$imgmdir");
	chmod 0777, @files;
}


#-----------------#
#  更新時間取得   #
#-----------------#
sub timeset
{
	$sttime = $_[0];
	($sec,$min,$hour,$mday,$mmon,$myear,$wwday) = localtime($sttime);
	$nitizi = sprintf("%d/%d ($week[$wwday]) %2d:%02d",$mmon+1,$mday,$hour,$min);
	if ($sttime) {
		return $nitizi;
	}
}


1;

__END__

