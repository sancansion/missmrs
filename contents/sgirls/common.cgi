#!/usr/bin/perl
require './jcode.pl';
require './cgi-lib.pl';
use Time::Local;

require 'char.txt';
#use lib "./Unicode";
#use Unicode::Japanese;
#our @ISA = qw ( Unicode::Japanese );

	$imgdir  = '../../girls';
	$imgmdir = 'mobile';
	$pagelog = 0;
	$nextImg = "./next.gif";
	$backImg = "./back.gif";
	$simgdir = '../img';
	$gscript = 'girls.cgi?mode=work&date=';
	$gscriptm = 'girls.cgi?mode=work&mobile=1&date=';

	($year, $month, $day) = &time;
	($nyear, $nmonth, $nday) = &nexttime;

	$maindir  = "../admin";

	$logfile  = "$maindir/girls.dat";
	$workdir  = "$maindir/work";
	$datadir  = "$maindir/work/$year$month";
	$ndatadir = "$maindir/work/$nyear$nmonth";

	@week = ('日','月','火','水','木','金','土');

%workhour = ('1','11:00','1.5','11:30','2','12:00','2.5','12:30','3','13:00','3.5','13:30','4','14:00','4.5','14:30','5','15:00','5.5','15:30','6','16:00','6.5','16:30','7','17:00','7.5','17:30','8','18:00','8.5','18:30','9','19:00','9.5','19:30','10','20:00','10.5','20:30','11','21:00','11.5','21:30','12','22:00','12.5','22:30','13','23:00','13.5','23:30','14','00:00','14.5','00:30','15','01:00','15.5','01:30','16','02:00','16.5','02:30','17','03:00','17.5','03:30','18','04:00','18.5','04:30','19','05:00','20','Last','20.5','休み');

$blogurl1 = 'http://www.cityheaven.net/k/emperor/A6GirlKeitaiDiaryList/?girlId=';
$blogurl2 = '&of=y#menus';
$blogurl1m = 'http://mobile.cityheaven.net/k/emperor/B6GirlDiaryList/?start=1&girlId=';
$blogurl2m = '&PHPSESSID=0f18870c554944b3c21801467210e51c';


	open(IN,"$logfile");
	while(<IN>){
		($gno, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);
		next if ($display);
		push(@staffdata, $_);

		open(WORK, "$datadir/$gno.cgi");
		while (<WORK>) {
			($workday, $start, $end) = split(/<>/);
			if ($workday == $day && ($start || $end)) {
				$todaywork{$gno} = 1;
			}
		}
		close(WORK);
		open(WORK, "$ndatadir/$gno.cgi");
		while (<WORK>) {
			($workday, $start, $end) = split(/<>/);
			if ($workday == $nday && ($start || $end)) {
				$nextwork{$gno} = 1;
			}
		}
		close(WORK);

	}
	close(IN);


#-------------
# WORK data
#-------------
sub workData {

	my(@commonworkdata, $data);
	my($year, $month, $day) = @_;
	$datadir = "$workdir/$year$month";

	open(IN,"$logfile");
	while(<IN>){
		($gno, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);
		next if ($display);

		open(WORK, "$datadir/$gno.cgi");
		while (<WORK>) {
			($workday, $start, $end) = split(/<>/);
			if ($workday == $day && ($start || $end)) {
				if(!$end) {
					$tim = "$workhour{$start}";
				} else {
					$tim = "$workhour{$start} ～ $workhour{$end}";
				}
				push(@commonworkdata,"$gno<>$id<>$namae<>$age<>$hei<>$bu<>$wa<>$hip<>$cup<>$hobby<>$workday<>$favorite<>$char<>$charm<>$mes<>$com<>$enteryear<>$entermon<>$enterday<>$taiken<>$new<>$ch1<>$ch2<>$ch3<>$nosmoke<>$display<>$blog<>$up<>$start<>$tim\n");
			}
		}
		close(WORK);

	}
	close(IN);
	$girlsninzu = $#commonworkdata + 1;
	@commonworkdata = sort { (split(/<>/, $a))[28] <=> (split(/<>/, $b))[28] } @commonworkdata;
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

			if ($key eq "search") {
				&jcode'convert(*val, 'euc');
				&jcode'h2z_euc(*val);
				&jcode::tr(\$val, $hiragana, $katakana); 
				&jcode::tr(\$val, $hankana, $katakana); 
				&jcode::tr(\$val, 'A-Z', 'a-z'); 
				&jcode::tr(\$val, $zendai, $hansyo); 
				&jcode::tr(\$val, $zensyo, $hansyo); 
			} else {
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
	$ENV{'TZ'} = "JST-9";
	($sec, $min, $hour, $mday, $mon, $year, $wday) = localtime();
	$year = $year + 1900;
	$mon = sprintf("%d", $mon +1);
	$mday = sprintf("%d", $mday);
	return ($year, $mon, $mday);
}

sub nexttime{
	$ENV{'TZ'} = "JST-9";
	($mday, $mon, $year) = (localtime(time + 1*24*60*60))[3..5];
	$year = $year + 1900;
	$mon = sprintf("%d", $mon +1);
	$mday = sprintf("%d", $mday);
	return ($year, $mon, $mday);
}


#-----------------#
#  更新時間取得   #
#-----------------#
sub timeset
{
	$sttime = $_[0];
	($sec,$min,$hour,$mday,$mmon,$myear,$wwday) = localtime($sttime);
	$nitizi = sprintf("%d/%d ($week[$wwday]) %2d:%02d",$mmon+1,$mday,$hour,$min);
	return $nitizi;
}


#--------------#
#  random      #
#--------------#
sub StartRandom {
local($nIndex) = @_;
local($nTemp, $nLoop, @arrFlag);
	for ($i = 0; $i < $nIndex; $i++) {
		$nLoop = 0;
		$nTemp = int(rand($nIndex));
		while ($nLoop < $i) {
			if ($nTemp == $arrFlag[$nLoop]) {
				$nTemp = int(rand($nIndex));
				$nLoop = 0;

			} else {
				$nLoop++;
			}
		}
		$arrFlag[$i] = $nTemp;
	}
	return @arrFlag;
}


#--------------#
#  String      #
#--------------#
sub zanStr { 
    my ($lng, $str) = @_; 
    return $str if(length($str) <= $lng); 
    jcode'convert(*str, 'euc'); 
    $str = substr($str, 0, $lng); 
    if ($str =~ /\x8F$/ or $str =~ tr/\x8E\xA1-\xFE// % 2){
        chop $str; 
    }
    jcode'convert(*str, 'sjis');
    $str .= "\.\.\.";
    return $str;
}
1;
__END__

