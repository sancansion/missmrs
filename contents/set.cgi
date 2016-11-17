#────────────────
# WORK MANAGEMENT SYSTEM
# Copyright (c) ARMS DESIGN INC.
# webmaster@arms.vc
# http://www.arms.vc/
#────────────────
require './cgi-lib.pl';
require './jcode.pl';
require './common.cgi';
require './password.cgi';

#-------------------
# BASIC
#-------------------
$MaxW = 300;	# 横幅
$MaxH = 450;	# 縦幅
$cgi_lib'maxdata = 102400000;

$imgdir = '../../girls';
$imgmdir = 'mobile';
$imgno  = 5;
$retu = 8;
$ext = '.cgi';

$shopname  = "EM";
$shopcolor = "#D1CEFF";

$girlscript  = './girls.cgi';				# 女の子情報スクリプト
$girlfile    = './girls.dat';				# 女の子情報ファイル

$workscript  = './work.cgi';				# 出勤登録スクリプト
$workdir     = 'work';

$backurl = "admin.cgi";

@statemes = ('',
'オススメ','イチオシ！','超美形','エロエロ','SEXY','キャバ系','ギャル系','癒し系','モデル系','グラマー','スレンダー'
);


@week = ('日','月','火','水','木','金','土');
$nor_color = "#000000";                   # 平日の文字色
$sat_color = "#0000ff";                   # 土曜日の文字色
$sun_color = "#ff0000";                   # 日曜日の文字色
$spe_color = "#ff0000";                   # 祝日、振替休日の文字色
$today_color = '#FAF0E6';                 # カレンダーの本日テーブル背景色
$table_color = '#F5FFFA';                 # カレンダーの通常テーブル背景色

%workhour = ('1','11:00','1.5','11:30','2','12:00','2.5','12:30','3','13:00','3.5','13:30','4','14:00','4.5','14:30','5','15:00','5.5','15:30','6','16:00','6.5','16:30','7','17:00','7.5','17:30','8','18:00','8.5','18:30','9','19:00','9.5','19:30','10','20:00','10.5','20:30','11','21:00','11.5','21:30','12','22:00','12.5','22:30','13','23:00','13.5','23:30','14','00:00','14.5','00:30','15','01:00','15.5','01:30','16','02:00','16.5','02:30','17','03:00','17.5','03:30','18','04:00','18.5','04:30','19','05:00','20','Last','20.5','休み');

$backForm = "PREV";
$nextForm = "NEXT";

$lockfile = './lock/lock.lock';			# ロックファイル名

$blogurl1 = 'http://www.cityheaven.net/k/emperor/A6GirlKeitaiDiaryList/?girlId=';
$blogurl2 = '&of=y#menus';


1;
__END__

