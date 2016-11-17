#!/usr/bin/perl
#��������������������������������
# WORK MANAGEMENT SYSTEM
# Copyright (c) 
#               ARMS DESIGN INC.
#��������������������������������

require './cgi-lib.pl';
require './jcode.pl';
require './set.cgi';
require './common.cgi';


&parseInput;

#====================================================================
#girllist
#====================================================================
if ($in{'cmd'} eq "list") {
	my($nyear , $nmon , $nday) = &time;
	$datadir = "$nyear$nmon";

	open(IN,"$girlfile");
	while(<IN>){
		local($stime, $data, $data2);
		($gno, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display) = split(/<>/);
		next if($display);
		open(WORK, "$workdir/$datadir/$gno.cgi");
		while (<WORK>) {
			($workday, $start, $end) = split(/<>/);
			if ($workday == $nday) {
				$stime = $start;
			}
		}
		close(WORK);
		if ($stime) {
			$data = "$gno<>$id<>$namae<>$stime<>";
			push(@wgirldata, "$data\n");
		} else {
			$data2 = "$gno<>$id<>$namae<><>";
			push(@wgirldata2, "$data2\n");
		}

	}
	close(IN);
	@wgirldata = sort { (split(/<>/, $a))[3] <=> (split(/<>/, $b))[3] } @wgirldata;
	push(@wgirldata, @wgirldata2);


	&header;
	print <<"EOM";
	<table class="greg">
EOM

$i=0;
	foreach (@wgirldata) {
		($no, $id, $namae, $time) = split(/<>/);
		if($i == 0) {
			print "<tr>\n";
		}
		$imgmsg = "<img src=\"$imgdir/$id/$id.jpg\" width=\"80\">";
		print "<td style=\"padding:10px;\" align=\"center\"><a href=\"$workscript?cmd=mon&no=$no&name=$namae\">$imgmsg<br>$namae</a><br>$workhour{$time}</td>\n";
		$i++;
		if($i == $retu) {
			print "</tr>\n";
			$i=0;
		}
	}

	print "</table>\n";
	print "</div>\n";
	print &HtmlBot;
	exit;
}
#====================================================================
#month display
#====================================================================
if ($in{'cmd'} eq "mon") {
	&header;
print <<"EOM";
<form action="$workscript" method="post">
	<input type="hidden" name="cmd" value="list">
	<input type="submit" value="�߂�">
</form>
EOM
	# ���ݎ���
	($year , $month , $day) = &time;
print "<div align=\"center\">\n";

	for($i = 0 ; $i < 3 ; $i++){
		if($month > 12){$year++;$month=1;}
		print "<a href=\"$workscript?cmd=display&no=$in{'no'}&name=$in{'name'}&year=$year&month=$month\">$year�N$month��</a><br><br>\n";
		$month++;
	}
	print "<br><br>\n";
	print "</div>\n";
	print &HtmlBot;
	exit;

}
#====================================================================
#display
#====================================================================
if ($in{'cmd'} eq "display") {

	&makeFile($in{'year'}, $in{'month'}, $in{'no'}, $workdir);

	local($day, $start, $end) = @_;

	if(!$filecheck){$job="new";}else{$job="edit";}

	# �w�肳�ꂽ���t�ɃW�����v�p
	$ViewYear  = $in{'year'};
	$ViewMonth = $in{'month'};
	$no        = $in{'no'};

	# �j���̎擾�v�Z
	$wkey = &get_week("1", "$ViewYear", "$ViewMonth");
	$lastday = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) [$ViewMonth - 1]
	+ ($ViewMonth == 2 && (($ViewYear % 4 == 0 && $ViewYear % 100 != 0) || $ViewYear % 400 == 0));
	$k=1; # ��

	open(IN,"$workdir/$ViewYear$ViewMonth/$no.cgi");
	@sinfo=<IN>;
	close(IN);

	&header;
	print <<"EOM";
<div align="center">
<form action="$workscript" method="post">
	<input type="hidden" name="cmd" value="list">
	<input type="submit" value="�߂�">
</form>
	<font color="orange" style="font-size:12px;font-weight:bold">$in{'name'}</font>
	<form action="$workscript" method="POST">
		<input type="hidden" name="cmd" value="kettei">
		<input type="hidden" name="job" value="$job">
		<input type="hidden" name="year" value="$ViewYear">
		<input type="hidden" name="mon" value="$ViewMonth">
		<input type="hidden" name="lastday" value="$lastday">
		<input type="hidden" name="no" value="$in{'no'}">
		<input type="submit" value="UPDATE">
		<table>
EOM

	# ���t�\���e�[�u��
	foreach $k(1 .. $lastday) {
		# �F�w��
		if ($wkey == 0) { $color = $sun_color; }
		elsif ($wkey == 6) { $color = $sat_color; }
		else { $color = $nor_color; }

		$flg=0;
		foreach(@sinfo){
			($day, $start, $end) = split(/<>/);
			last if($day == $k);
		}
		print "	<tr>\n";

# ���t
#---------
		print "		<td><font color=\"$color\">$ViewMonth/$k($week[$wkey])</font></td>\n";

# �J�n
#---------
		print "		<td>\n";
		print "			<select name=s$k>\n";
		print "			<option value=\"\"></option>\n";
		for ($t = 1; $t <= 19.5; $t+=0.5){
			if($t == $start) {
				$selected = " selected";

			} else {
				$selected = "";
			}
			print "			<option value=\"$t\"$selected>$workhour{$t}</option>\n";
		}
		print "			</select>\n";
		print "		</td>\n";

		print "		<td>�`</td>\n";

# �I��
#---------
		print "		<td>\n";
		print "			<select name=e$k>\n";
		print "			<option value=\"\"></option>\n";
		for ($t = 1; $t <= 20; $t+=0.5){
			if($t == $end) {
				$selected = " selected";

			} else {
				$selected = "";
			}
			print "			<option value=\"$t\"$selected>$workhour{$t}</option>\n";
		}
		print "		</select>\n";
		print "		</td>\n";
		print "	</tr>\n";

		if ($wkey == 6) {
			print "	<tr><td colspan=\"6\"><hr></td></tr>\n";
		}

		$wkey++;
		$k++;
		if ($wkey == 7) { $wkey=0; }
	}


print <<"EOM";
	</table>
	<br>
	<input type="submit" value="UPDATE">
</form>
</div>
</body>
</html>
EOM

	exit;
}
#==========
#����
#==========
elsif ($in{'cmd'} eq "kettei") {

#==========
#FILE CHECK
#==========
	$ViewYear  = $in{'year'};
	$ViewMonth = $in{'mon'};
	$lastday   = $in{'lastday'};
	$no        = $in{'no'};

	foreach $k(1 .. $lastday) {
		$st = "s$k";
		$en = "e$k";
		push(@new,"$k<>$in{$st}<>$in{$en}<>\n");
		$k++;
	}

	# �X�V
	open(OUT,">$workdir/$ViewYear$ViewMonth/$no.cgi") || &error("Write Error: $workdir/$ViewYear$ViewMonth/$no.cgi");
	print OUT @new;
	close(OUT);

	&header;
print <<"EOM";
<div align="center">
<p>�������܂����B</p>
<form action="$workscript" method="POST">
	<input type="hidden" name="cmd" value="list">
	<input type="submit" value="TOP�ɖ߂�">
</form>
</div>
</body>
</html>
EOM


exit;
}


__END__

