#��������������������������������
# WORK MANAGEMENT SYSTEM
# Copyright (c) ARMS DESIGN INC.
# webmaster@arms.vc
# http://www.arms.vc/
#��������������������������������
require './cgi-lib.pl';
require './jcode.pl';
require './common.cgi';
require './password.cgi';

#-------------------
# BASIC
#-------------------
$MaxW = 300;	# ����
$MaxH = 450;	# �c��
$cgi_lib'maxdata = 102400000;

$imgdir = '../../girls';
$imgmdir = 'mobile';
$imgno  = 5;
$retu = 8;
$ext = '.cgi';

$shopname  = "EM";
$shopcolor = "#D1CEFF";

$girlscript  = './girls.cgi';				# ���̎q���X�N���v�g
$girlfile    = './girls.dat';				# ���̎q���t�@�C��

$workscript  = './work.cgi';				# �o�Γo�^�X�N���v�g
$workdir     = 'work';

$backurl = "admin.cgi";

@statemes = ('',
'�I�X�X��','�C�`�I�V�I','�����`','�G���G��','SEXY','�L���o�n','�M�����n','�����n','���f���n','�O���}�[','�X�����_�['
);


@week = ('��','��','��','��','��','��','�y');
$nor_color = "#000000";                   # �����̕����F
$sat_color = "#0000ff";                   # �y�j���̕����F
$sun_color = "#ff0000";                   # ���j���̕����F
$spe_color = "#ff0000";                   # �j���A�U�֋x���̕����F
$today_color = '#FAF0E6';                 # �J�����_�[�̖{���e�[�u���w�i�F
$table_color = '#F5FFFA';                 # �J�����_�[�̒ʏ�e�[�u���w�i�F

%workhour = ('1','11:00','1.5','11:30','2','12:00','2.5','12:30','3','13:00','3.5','13:30','4','14:00','4.5','14:30','5','15:00','5.5','15:30','6','16:00','6.5','16:30','7','17:00','7.5','17:30','8','18:00','8.5','18:30','9','19:00','9.5','19:30','10','20:00','10.5','20:30','11','21:00','11.5','21:30','12','22:00','12.5','22:30','13','23:00','13.5','23:30','14','00:00','14.5','00:30','15','01:00','15.5','01:30','16','02:00','16.5','02:30','17','03:00','17.5','03:30','18','04:00','18.5','04:30','19','05:00','20','Last','20.5','�x��');

$backForm = "PREV";
$nextForm = "NEXT";

$lockfile = './lock/lock.lock';			# ���b�N�t�@�C����

$blogurl1 = 'http://www.cityheaven.net/k/emperor/A6GirlKeitaiDiaryList/?girlId=';
$blogurl2 = '&of=y#menus';


1;
__END__

