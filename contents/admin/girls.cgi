#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);
#��������������������������������
# INFORMATION MANAGEMENT SYSTEM
# Copyright (c) ARMS DESIGN INC.
# webmaster@arms.vc
# http://www.arms.vc/
#��������������������������������
require './set.cgi';
require './thumbnail.cgi';
$title = '���̎q���ҏW';

&decode;
&admin;

sub admin {
	local($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $up, $enteryear, $entermon, $enterday, $new, $f, $del);

	# ���e�t�H�[��
	if ($in{'job'} eq "form") {

		&form;

	# ���e����
	} elsif ($in{'job'} eq "form2") {

		if ($in{'id'} eq "") { &error("ID����͂��Ă�������"); }

		local($no, @file);

		&makePDir("$in{'id'}");
		# �摜�A�b�v
		if ($in{'upfile1'} || $in{'upfile2'} || $in{'upfile3'} || $in{'upfile4'} || $in{'upfile5'}) {
			&upload($in{'id'});
		}

		open(IN,"$girlfile") || &error("Open Error: $girlfile");
		@file = <IN>;
		close(IN);

		# �̔�
		($no) = split(/<>/, $file[0]);
		$no++;
		# �X�V
		unshift(@file,"$no<>$in{'id'}<>$in{'namae'}<>$in{'age'}<>$in{'hei'}<>$in{'bu'}<>$in{'wa'}<>$in{'hip'}<>$in{'cup'}<>$in{'hobby'}<>$in{'workday'}<>$in{'favorite'}<>$in{'char'}<>$in{'charm'}<>$in{'mes'}<>$in{'com'}<>$in{'enteryear'}<>$in{'entermon'}<>$in{'enterday'}<>$in{'taiken'}<>$in{'new'}<>$in{'ch1'}<>$in{'ch2'}<>$in{'ch3'}<>$in{'nosmoke'}<>$in{'display'}<>$in{'blog'}<>$in{'up'}<>\n");
		open(OUT,">$girlfile") || &error("Write Error: $girlfile");
		print OUT @file;
		close(OUT);

	# �폜
	} elsif ($in{'job'} eq "dele" && $in{'no'}) {

		local($i, $j, $f);
		local(@new)=();
		open(IN,"$girlfile") || &error("Open Error: $girlfile");
		while (<IN>) {
			$f=0;
			($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);

			foreach $del ( split(/\0/, $in{'no'}) ) {
				if ($no == $del) {
					$f++;
					foreach $i (1 .. $imgno) {
						unlink("$imgdir/$id/$i.jpg");
						unlink("$imgdir/$id/$imgmdir/$i.jpg");
					}
					unlink("$imgdir/$id/$id.jpg");
					unlink("$imgdir/$id/$imgmdir/$id.jpg");
					rmdir ("$imgdir/$id/$imgmdir");
					rmdir ("$imgdir/$id");
					last;
				}
			}
			if (!$f) { push(@new, $_); }
		}
		close(IN);

		# �X�V
		open(OUT,">$girlfile") || &error("Write Error: $girlfile");
		print OUT @new;
		close(OUT);

	# �C���t�H�[��
	} elsif ($in{'job'} eq "edit" && $in{'no'}) {

		local(@no) = split(/\0/, $in{'no'});

		open(IN,"$girlfile") || &error("Open Error: $girlfile");
		while (<IN>) {
			($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);
			last if ($no[0] == $no);
		}
		close(IN);

		# �C�����
		&form($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up);

	# �C�����s
	} elsif ($in{'job'} eq "edit2" && $in{'no'}) {

		if ($in{'id'} eq "") { &error("ID����͂��Ă�������"); }
		# �摜�A�b�v
		&makePDir("$in{'id'}");
		# �摜�A�b�v
		if ($in{'upfile1'} || $in{'upfile2'} || $in{'upfile3'} || $in{'upfile4'} || $in{'upfile5'}) {
			&upload($in{'id'});
		}
		if ($in{'del1'}) {	unlink("$imgdir/$in{'id'}/1.jpg");	unlink("$imgdir/$in{'id'}/$imgmdir/1.jpg");	}
		if ($in{'del2'}) {	unlink("$imgdir/$in{'id'}/2.jpg");	unlink("$imgdir/$in{'id'}/$imgmdir/2.jpg");	}
		if ($in{'del3'}) {	unlink("$imgdir/$in{'id'}/3.jpg");	unlink("$imgdir/$in{'id'}/$imgmdir/3.jpg");	}
		if ($in{'del4'}) {	unlink("$imgdir/$in{'id'}/4.jpg");	unlink("$imgdir/$in{'id'}/$imgmdir/4.jpg");	}
		if ($in{'del5'}) {	unlink("$imgdir/$in{'id'}/$in{'id'}.jpg");	unlink("$imgdir/$in{'id'}/$imgmdir/$in{'id'}.jpg");	}

		local(@new)=();
		open(IN,"$girlfile") || &error("Open Error: $girlfile");
		while (<IN>) {
			s/\n$//;
			($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);

			if ($in{'no'} == $no) {

				$_ = "$no<>$in{'id'}<>$in{'namae'}<>$in{'age'}<>$in{'hei'}<>$in{'bu'}<>$in{'wa'}<>$in{'hip'}<>$in{'cup'}<>$in{'hobby'}<>$in{'workday'}<>$in{'favorite'}<>$in{'char'}<>$in{'charm'}<>$in{'mes'}<>$in{'com'}<>$in{'enteryear'}<>$in{'entermon'}<>$in{'enterday'}<>$in{'taiken'}<>$in{'new'}<>$in{'ch1'}<>$in{'ch2'}<>$in{'ch3'}<>$in{'nosmoke'}<>$in{'display'}<>$in{'blog'}<>$in{'up'}<>";
			}
			push(@new,"$_\n");
		}
		close(IN);

		# �X�V
		open(OUT,">$girlfile") || &error("Write Error: $girlfile");
		print OUT @new;
		close(OUT);
	}

	&header;
	print <<"EOM";
	<form action="$girlscript" method="post">
		<input type="hidden" name="pass" value="$in{'pass'}">
		<input type="hidden" name="mode" value="admin">
		<input type="hidden" name="job" value="form">
		<input type="submit" value="�V�K�쐬" style="width:130px;height:32px;margin-bottom:5px;">
	</form>
		<table class="greg">
EOM
$i=0;

	# ���O�W�J
	open(IN,"$girlfile") || &error("Open Error: $girlfile");
	@staffdata = <IN>;
	close(IN);

	@staffdata = sort {	(split(/<>/, $a))[25] <=> (split(/<>/, $b))[25] || 
							(split(/<>/, $a))[0] <=> (split(/<>/, $b))[0] 
						} @staffdata;

	foreach (@staffdata) {
		local($newcom, $cls, $newcom, $upcom, $nscom);
		($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = split(/<>/);
		if ($i == 0) {
			print "			<tr>\n";
		}
		if($display)	{	$cls = " style=\"background-color:#999;\"";	}
		if ($new) {			$newcom = " new";	} elsif ($taiken) {	$newcom = " �̌�";		}
		if ($up) {			$upcom = " up";	}
		if ($nosmoke) {		$nscom = " ��i��";	}
		print <<"EOM";
				<td style="padding:10px;"$cls>
					<img src="$imgdir/$id/$id.jpg" width="80"><br>
					<form action="$girlscript" method="post">
					<input type="checkbox" name="no" value="$no">
					$namae($age)<br>
					<input type="hidden" name="pass" value="$in{'pass'}">
					<input type="hidden" name="mode" value="admin">
					<input type="hidden" name="job" value="dele">
					<input type="submit" value="�폜" style="width:80px;height:32px;margin-top:5px;">
					</form>
					<form action="$girlscript" method="post">
					<input type="hidden" name="pass" value="$in{'pass'}">
					<input type="hidden" name="mode" value="admin">
					<input type="hidden" name="job" value="edit">
					<input type="hidden" name="no" value="$no">
					<input type="submit" value="�C��" style="width:80px;height:32px;">
					</form>
				</td>
EOM
		$i++;
		if ($i == $retu) {
			print "			</tr>\n";
			$i = 0;
		}
	}
		print <<"EOM";
		</table>
	</form>
</div>
EOM
	print &HtmlBot;
	exit;
}

#----------------#
#  ���e�t�H�[��  #
#----------------#
sub form {
	local($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up) = @_;

	# ���s�͕���
	$com =~ s/<br>/\r/ig;

	# �p�����[�^��`
	local($job) = $in{'job'} . '2';
	if($new)	{	$newchecked    = " checked";}	else{	$newchecked    = "";}
	if($taiken)	{	$taikenchecked = " checked";}	else{	$taikenchecked = "";}
	if($nosmoke){	$nschecked     = " checked";}	else{	$nschecked     = "";}
	if($display){	$dispchecked   = " checked";}	else{	$dispchecked   = "";}
	if($up)		{	$upchecked    = " checked";}	else{	$upchecked    = "";}

	# �t�H�[���\��
	&header;
	print <<"EOM";
<form action="$girlscript" method="post">
	<input type="hidden" name="pass" value="$in{'pass'}">
	<input type="submit" value="�߂�">
</form>
<form action="$girlscript" method="post" enctype="multipart/form-data">
	<input type="hidden" name="mode" value="admin">
	<input type="hidden" name="pass" value="$in{'pass'}">
	<input type="hidden" name="job" value="$job">
	<input type="hidden" name="no" value="$no">
	<table>
		<tr>
			<td align="left">���O</td>
			<td align="left"><input type="text" name="namae" value="$namae" size="20"></td>
		</tr>
		<tr>
			<td>�ӂ肪��</td>
			<td><input type="text" name="charm" value="$charm" size="20"></td>
		</tr>
		<tr>
			<td align="left">���[�}��<font color="red">�I���p�����I</font><br></td>
			<td align="left"><input type="text" name="id" value="$id" size="20"></td>
		</tr>
		<tr>
			<td>�N��</td>
			<td><input type="text" name="age" value="$age" size="5"></td>
		</tr>
		<tr><!--
			<td align="left">\�\\����<font color="red">�I���p�����I</font><br></td>
			<td align="left"><input type="text" name="bu" value="$bu" size="5"></td>
		</tr>
		<tr>
			<td>�g��</td>
			<td><input type="text" name="hei" value="$hei" size="5"></td>
		</tr>
		<tr>
			<td>�T�C�Y</td>
			<td>
				W<input type="text" name="wa" value="$wa" size="5">
				H<input type="text" name="hip" value="$hip" size="5">
				Cup<input type="text" name="cup" value="$cup" size="5">
			</td>
		</tr>
		<tr>
			<td>�</td>
			<td><input type="text" name="hobby" value="$hobby" size="40"></td>
		</tr>
		<tr>
			<td>���i</td>
			<td><input type="text" name="char" value="$char" size="40"></td>
		</tr>
		<tr>
			<td>�o�Γ�</td>
			<td><input type="text" name="workday" value="$workday" size="40"></td>
		</tr>
		<tr>
			<td>�D���ȃ^�C�v</td>
			<td><input type="text" name="favorite" value="$favorite" size="40"></td>
		</tr>
		<tr>
			<td>���̎q�R�����g</td>
			<td><textarea name="mes" cols="50" rows="6" wrap="soft">$mes</textarea></td>
		</tr>-->
		<tr>
			<td>�R�����g</td>
			<td><textarea name="com" cols="50" rows="6" wrap="soft">$com</textarea></td>
		</tr><!--
		<tr>
			<td>���X��</td>
			<td><input type="text" name="enteryear" value="$enteryear" size="4">�N<input type="text" name="entermon" value="$entermon" size="2">��<input type="text" name="enterday" value="$enterday" size="2">��</td>
		</tr>
		<tr>
			<td>�̌�</td>
			<td><input type="checkbox" name="taiken" value="1"$taikenchecked></td>
		</tr>
		<tr>
			<td>NEW</td>
			<td><input type="checkbox" name="new" value="1"$newchecked></td>
		</tr>
		<tr>
			<td>�摜�t�o</td>
			<td><input type="checkbox" name="up" value="1"$upchecked></td>
		</tr>
		<tr>
			<td>��i��</td>
			<td><input type="checkbox" name="nosmoke" value="1"$nschecked></td>
		</tr>-->
		<tr><td>�u���O</td><td><input type="text" name="blog" value="$blog" size="40"></td></tr>
		<tr><td>��\\��</td><td><input type="checkbox" name="display" value="1"$dispchecked></td></tr><!--
		<tr>
			<td>�n��</td>
			<td>
EOM
		print "			<select name=\"ch1\">\n";
		foreach $a (0 .. $#statemes) {
			if($a == $ch1) {		$selected = " selected";	} else {	$selected = "";		}
			print "			<option value=\"$a\"$selected>$statemes[$a]</option>\n";
		}
		print "			</select>\n";
		print "			<select name=\"ch2\">\n";
		foreach $a (0 .. $#statemes) {
			if($a == $ch2) {		$selected = " selected";	} else {	$selected = "";		}
			print "			<option value=\"$a\"$selected>$statemes[$a]</option>\n";
		}
		print "			</select>\n";
		print "			<select name=\"ch3\">\n";
		foreach $a (0 .. $#statemes) {
			if($a == $ch3) {		$selected = " selected";	} else {	$selected = "";		}
			print "			<option value=\"$a\"$selected>$statemes[$a]</option>\n";
		}
		print "			</select></td></tr>-->\n";

		foreach $j (1 .. 1) {
			print <<"EOM";
		<tr><td>�摜$j(300�~450)</td><td><input type="file" name="upfile$j" size="45">&emsp;<input type="checkbox" name="del$j" value="1">�폜[<img src=\"$imgdir/$id/$j.jpg" width="10">�摜$j]</td></tr>
EOM
	}
		print <<"EOM";
		<tr>
			<td align="left">�ꗗ�摜(140�~210)</td>
		<td align="left"><input type="file" value="http://rady-e.net/contents/img/noimage.jpg" name="upfile$imgno" size="45">&emsp;<input type="checkbox" name="del$imgno" value="1">�폜[<img src="$imgdir/$id/$id.jpg" width="10">�摜]</td>
		</tr>
	</table>
	<p>
	<input type="submit" value="���M����">
</form>
EOM
	print &HtmlBot;
	exit;
}

#--------------------#
#  �摜�A�b�v���[�h  #
#--------------------#
sub upload {
	local($id) = @_;
	local($tail, $fnam, $macbin, $f, $i, $flag, $imgfile,
		$upfile, $length, $W, $H, $W2, $H2,@tail,@fnam,@name,@upfile);

	# �摜����
	$macbin=0;
	@tail=();
	@fnam=();
	@name=();
	foreach (@in) {
		if (/(.*)Content-type:(.*)/i) {
			$tail = $2;
			$tail =~ s/\r//g;
			$tail =~ s/\n//g;
			push(@tail, $tail);
		}
		if (/.*name=\"(.*)\";.*filename=\"(.*)\"/i) {
			$fnam = $2;
			$fnam =~ s/\r//g;
			$fnam =~ s/\n//g;
			push(@fnam, $fnam);
			push(@name, $1);
		}
		if (/application\/x-macbinary/i) { $macbin=1; }
	}

	# �t�@�C���`����F��
	$f=0;
	$i=0;
	@upfile=();
	foreach (0 .. $#tail) {
		$i++;
		$flag=0;
		if ($tail[$_] =~ /image\/gif/i) { $tail=".gif"; $flag=1; }
		elsif ($tail[$_] =~ /image\/jpeg/i) { $tail=".jpg"; $flag=1; }
		elsif ($tail[$_] =~ /image\/x-png/i) { $tail=".png"; $flag=1; }
		if (!$flag) {
			if ($fnam[$_] =~ /\.gif$/i) { $tail=".gif"; $flag=1; }
			elsif ($fnam[$_] =~ /\.jpe?g$/i) { $tail=".jpg"; $flag=1; }
			elsif ($fnam[$_] =~ /\.png$/i) { $tail=".png"; $flag=1; }
		}

		if ($name[$_] eq "upfile$i") {
			$upfile = $in{"upfile$i"};
			if ($i == $imgno) {
				$imgfile = "$imgdir/$id/$id$tail";
			} else {
				$imgfile = "$imgdir/$id/$i$tail";
			}
		}

		# �A�b�v���[�h����
		if ($flag) { $f++; }
		else { push(@upfile,("","","")); next; }

		# �}�b�N�o�C�i���΍�
		if ($macbin) {
			$length = substr($upfile,83,4);
			$length = unpack("%N", $length);
			$upfile = substr($upfile,128, $length);
		}

		# �f�[�^������
		open(OUT,">$imgfile") || &error("�摜�A�b�v���s");
		binmode(OUT);
		binmode(STDOUT);
		print OUT $upfile;
		close(OUT);

		chmod (0666, $imgfile);

		# �摜�T�C�Y�擾
		if ($tail eq ".jpg") { ($W, $H) = &j_size($imgfile); }
		elsif ($tail eq ".gif") { ($W, $H) = &g_size($imgfile); }
		elsif ($tail eq ".png") { ($W, $H) = &p_size($imgfile); }

		# �摜�\���k��
		if ($W > $MaxW || $H > $MaxH) {
			$W2 = $MaxW / $W;
			$H2 = $MaxH / $H;
			if ($W2 < $H2) { $key = $W2; }
			else { $key = $H2; }
			$W = int ($W * $key) || 1;
			$H = int ($H * $key) || 1;
		}
		push(@upfile,($tail, $W, $H));
		if ($i < 5) {
			&make_thumbnail($i, $id, $tail);
		}
	}
	return @upfile;
}

#------------------#
#  JPEG�T�C�Y�F��  #
#------------------#
sub j_size {
	local($jpeg) = @_;
	local($t, $m, $c, $l, $W, $H);

	open(JPEG, "$jpeg") || return (0,0);
	binmode JPEG;
	read(JPEG, $t, 2);
	while (1) {
		read(JPEG, $t, 4);
		($m, $c, $l) = unpack("a a n", $t);

		if ($m ne "\xFF") {
			$W = $H = 0;
			last;
		} elsif ((ord($c) >= 0xC0) && (ord($c) <= 0xC3)) {
			read(JPEG, $t, 5);
			($H, $W) = unpack("xnn", $t);
			last;
		} else {
			read(JPEG, $t, ($l - 2));
		}
	}
	close(JPEG);
	return ($W, $H);
}

#-----------------#
#  GIF�T�C�Y�F��  #
#-----------------#
sub g_size {
	local($gif) = @_;
	local($data);

	open(GIF,"$gif") || return (0,0);
	binmode(GIF);
	sysread(GIF, $data,10);
	close(GIF);

	if ($data =~ /^GIF/) { $data = substr($data,-4); }

	$W = unpack("v",substr($data,0,2));
	$H = unpack("v",substr($data,2,2));
	return ($W, $H);
}

#-----------------#
#  PNG�T�C�Y�F��  #
#-----------------#
sub p_size {
	local($png) = @_;
	local($data);

	open(PNG, "$png") || return (0,0);
	binmode(PNG);
	read(PNG, $data, 24);
	close(PNG);

	$W = unpack("N", substr($data, 16, 20));
	$H = unpack("N", substr($data, 20, 24));
	return ($W, $H);
}

__END__

