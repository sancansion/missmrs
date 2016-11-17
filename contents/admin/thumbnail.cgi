#!/usr/lib
use CGI::Carp qw(fatalsToBrowser);
use Image::Magick;

sub make_thumbnail {
	($no, $id, $tail) = @_;

$file_dir = "../../girls/$id/";
$thumbnail_dir = "../../girls/$id/mobile/";
$inimage = "$no$tail";
$img_max_width = 200;

		my $image = Image::Magick->new;
		$image->Read("$file_dir$inimage");
		$image->Set(quality=>85);
		$image->Thumbnail(geometry=>$img_max_width);
		$image->Write("$thumbnail_dir$inimage");

}
1;
