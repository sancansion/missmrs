#!/usr/bin/perl
#„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ
# WORK MANAGEMENT SYSTEM
# Copyright (c) MAX DESIGN OFFICE
#               ARMS DESIGN INC.
#„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ„Ÿ
require './common.cgi';
&decode;

	if($in{'mobile'}) {
		$tmpfile = './profilem.html';
	} else {
		$tmpfile = './profile.html';
	}


print "Content-type: text/html\n\n";

	local(@loop);

	open(IN,"$tmpfile") || &error("Open Error: $tmpfile");
	@loop = <IN>;
	close(IN);

	foreach (@staffdata) {
		($no, $id, $namae, $age, $hei, $bu, $wa, $hip, $cup, $hobby, $workday, $favorite, $char, $charm, $mes, $com, $enteryear, $entermon, $enterday, $taiken, $new, $ch1, $ch2, $ch3, $nosmoke, $display, $blog, $up, $st, $tim) = split(/<>/);
		last if ($in{'girlid'} eq $id);
	}

	if($blog) {
		if ($in{'mobile'}) {
			$blogurl = "<a href=\"$blogurl1m$blog$blogurl2m\"><img src=\"/images/blog.gif\" title=\"ŽÊƒ“ú‹L\" border=\"0\" /></a>";
		} else {
			$blogurl = "<a href=\"$blogurl1$blog$blogurl2\" target=\"_blank\"><img src=\"/images/blog.gif\" title=\"ŽÊƒ“ú‹L\" border=\"0\" /></a>";
		}
	} else {
		$blogurl  = "";
	}

	if($new) 			{	$newmsg = "<img src=\"$simgdir/new.gif\" />";	}
	if($taiken) 		{	$newmsg = "<img src=\"$simgdir/taiken.gif\" />";}
	if($nosmoke) 		{	$skmsg  = "<img src=\"$simgdir/tabaco.gif\" />";	}

	foreach (@loop) {
		s|!no!|$no|;
		s|!id!|$id|;
		s|!name!|$namae|;
		s|!age!|$age|;
		s|!hei!|$hei|;
		s|!bu!|$bu|;
		s|!wa!|$wa|;
		s|!hip!|$hip|;
		s|!cup!|$cup|;
		s|!hobby!|$hobby|;
		s|!workday!|$workday|;
		s|!favorite!|$favorite|;
		s|!char!|$char|;
		s|!charm!|$charm|;
		s|!mes!|$mes|;
		s|!com!|$com|;
		s|!url!|$blogurl|;
		s|!course!|$kosu|;
		s|!newmsg!|$newmsg|;
		s|!nosmoke!|$skmsg|;


		if ($in{'pick'}) {s|!pickcnt!|<img src=\"../pagecount/daycount.cgi?mode=today&dirname=girl&gname=$id\">|i;	} else {s/!pickcnt!//i;}


		if ($ch1) {s|!ch1!|<img src=\"$simgdir/feature/$ch1.jpg\" />|i;	} else {s/!ch1!//i;}
		if ($ch2) {s|!ch2!|<img src=\"$simgdir/feature/$ch2.jpg\" />|i;	} else {s/!ch2!//i;}
		if ($ch3) {s|!ch3!|<img src=\"$simgdir/feature/$ch3.jpg\" />|i;	} else {s/!ch3!//i;}

		if(-e "$imgdir/$id/$id.jpg") {
			$imgmsg = "$imgdir/$id/$id.jpg";
		} else {
			$imgmsg = "$simgdir/noimage.jpg";
		}
		s|!image!|$imgmsg|g;

		foreach $i (0 .. 3) {
			$j = $i + 1;
			$image = "!image-$j\!";

			if(-e "$imgdir/$id/$j.jpg") {
				if($in{'mobile'}) {
					$imgname[$i] = "$imgdir/$id/$imgmdir/$j.jpg";
				} else {
					$imgname[$i] = "$imgdir/$id/$j.jpg";
				}
			} else {
				if($in{'mobile'}) {
					$imgname[$i] = "";
				} else {
					$imgname[$i] = "$simgdir/noimage.jpg";
				}
			}
			s|$image|$imgname[$i]|g;
		}

		print;

	}
exit;

__END__

