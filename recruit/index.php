<?php

/*----------------------------------------------------------------------------------
	�ե�����᡼�� - sformmmail2
	(c)sapphirus.biz
----------------------------------------------------------------------------------*/


/* �ɲå��ץ�������� */

// ��ե���ˤ�볰�����Ѥ����¡ʤ���:1/���ʤ�:0��
$refCheck = 1;

// ʸ�������������1�ˤ��ƤߤƲ�����
$ill_char = 0;

// ��ɽ�פʤɤ�ʸ���Τ��Ȥˡ�\�פ��դ��Ƥ��ޤ�����1�ˤ��ƤߤƲ�����
$ill_slash = 0;

// https�Ǥ����Ѥξ��1�ˤ��Ʋ�����
// ���ɥᥤ���secure�⤷����ssl���ޤޤ����Ͼ�����ꤵ��ޤ�
$use_ssl = 0;

// ����ե������ɤ߹���
include_once('sfm_config.php');

// HTML&�᡼��ƥ�ץ졼������
$temp_html = array(
	'form'			=> 'sfm_form.html' // ���ϥե�������
,	'confirm'		=> 'sfm_confirm.html' // ��ǧ������
,	'completion'	=> 'sfm_completion.html' // ������λ����
,	'mail'			=> 'sfm_mail_tmpl.php' // �᡼��������
,	'reply'			=> 'sfm_reply_tmpl.php' // ��ư�ֿ��᡼����
);

// ���顼ɽ������
$temp_err = array(
	'__Error_Input_Data__'		=> '<span style="color:red;">̤���ϤǤ�</span>'
,	'__Error_Marge_Data__'		=> 'Error'
,	'__Error_Mail_Address__'	=> 'Error'
,	'__Error_Mail_Check__'		=> 'Error'
,	'__Error_Max_Text__'		=> "Error"
);

// ƱNAME��ʣ�����ܤη������
$name_marge = array(
	'tel'		=> '-'
,	'fax'		=> '-'
,	'zip'		=> '-'
,	'address'	=> "\n"
);

// submitɽ������
function printSubmit() {
	if($_SESSION['SFM']['InputErr']) {
		// ���顼���������HTML����
		$submit = <<< EOD
<input type="button" value="���" onclick="history.back()" class="back" />
EOD;
	} else {
		// ���ܤ�����������HTML����
		$submit = <<< EOD
<input type="hidden" name="mode" id="mode" value="SEND" />
<input type="button" value="���" onclick="history.back()" class="back" />
<input type="submit" value="����" class="mail" />
EOD;
	}
	return $submit;
}


/* �ᥤ��ץ���� */

$scriptVersion = '2.51';
$sfm_class = new sfmClass();

// �������󥳡��ɤ�����
if (!extension_loaded('mbstring')) {
	Err('Error: mbstring�ؿ������ѤǤ��ޤ���');
}
$internalEnc = 'EUC-JP';
mb_language('ja');
mb_internal_encoding($internalEnc);

if (!isset($mailTo[0])) {
	Err('������᡼�륢�ɥ쥹�����ꤵ��Ƥޤ���');
}
$mode = (isset($_POST['mode'])) ? $_POST['mode'] : '';
$script_name = preg_replace('/.+\/(.*)/', "$1", $_SERVER['REQUEST_URI']);

// �⡼�ɤˤ��ʬ��
switch ($mode) {
case 'SEND': // �᡼������
	session_cache_limiter('nocache');
	session_start();
	if (!isset($_SESSION['SFM'])) {
		Err('���å����ǡ���������ޤ���');
	}
	$sfm_mail = $sfm_class->formDataMail();
	$sfm_userinfo = $sfm_class->userInfo();
	$mailTo = (isset($mailTo[$_SESSION['SFM']['mailToNum']])) ? $mailTo[$_SESSION['SFM']['mailToNum']] : $mailTo[0];
	// ������˥᡼������
	$mailFrom = (!isset($_SESSION['SFM']['email'])) ? 'S.B. Formmail' : $_SESSION['SFM']['email'];
	include_once($temp_html['mail']);
	$sfm_class->sendMail($mailTo, $mailSubject, $mailMessage, $mailFrom, $mailBcc);
	// �᡼�뼫ư�ֿ�
	if (
		(isset($_POST['autoReply']) || isset($_SESSION['SFM']['autoReply'])) &&
		isset($_SESSION['SFM']['email']) && is_file($temp_html['reply'])
	) {
		include_once($temp_html['reply']);
		$replyAddress = ($replyAddress) ? $replyAddress : $mailTo;
		if ($replyName) {
			$replyAddress = "{$replyName} <{$replyAddress}>";
		}
		$sfm_class->sendMail($_SESSION['SFM']['email'], $replySubject, $replyMessage, $replyAddress, $replyBcc);
	}
	unset($_SESSION['SFM']);
	include_once($temp_html['completion']);
	break;

case 'CONFIRM': // �ǡ��������ȳ�ǧ
	if (
		(isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] == 'on') ||
		(preg_match('/secure|ssl/i', $_SERVER['HTTP_HOST'])) ||
		($use_ssl == 1)
	) {
		$protcol = 'https://';
	} else {
		$protcol = 'http://';
	}
	if ($_SERVER['HTTP_REFERER'] != $protcol.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'] && $refCheck) {
		Err('�����������ѤϽ���ޤ���');
	}
	session_cache_limiter('nocache');
	session_start();
	unset($_SESSION['SFM']);
	$error = $email = '';
	foreach ($_POST as $key => $value) {
		$name = preg_replace('/(.+)_s$/', "$1", $key);
		if ($value == 'none') $value = '';
		if (is_array($value)) {
			$value = $sfm_class->valueMarge($key, $value, $name_marge);
			if ($value == '__Error_Marge_Data__') {
				$error = 1;
			}
		}
		if (!$ill_slash) {
			$value = (!get_magic_quotes_gpc()) ? addslashes($value) : $value;
		}
		if (!$ill_char) {
			$value = mb_convert_encoding($value, $internalEnc, $baseEnc);
		}
		$value = mb_convert_kana($value, 'KV', $internalEnc);
		if (preg_match('/_s$/', $key) && $value == '') {
			$_SESSION['SFM'][$name] = '__Error_Input_Data__';
			$error = 1;
		} elseif ($name == 'email' && $value) {
			if (!preg_match("/^[\w\-\.]+\@[\w\-\.]+\.([a-z]+)$/", $value)) {
				$_SESSION['SFM']['email'] = '__Error_Mail_Address__';
				$error = $email = 1;
			} else {
				$_SESSION['SFM']['email'] = $email = $value;
			}
		} elseif ($name == 'emailcheck') {
			if ($email != 1 && $email != $value) {
				$_SESSION['SFM']['email'] = '__Error_Mail_Check__';
				$error = 1;
			}
		} elseif ($maxText && strlen($value) > $maxText) {
			$_SESSION['SFM'][$name] = '__Error_Max_Text__';
			$error = 1;
		} else {
			$_SESSION['SFM'][$name] = $value;
		}
	}
	$_SESSION['SFM']['InputErr'] = $error;
	$sfm_script = $script_name.((SID) ? '?'.strip_tags(SID) : '');
	$sfm_html = $sfm_class->formDataHtml();
	$sfm_submit = mb_convert_encoding(printSubmit(), $baseEnc, $internalEnc);
	include_once($temp_html['confirm']);
	break;

default: // ���ϥե�����ɽ��
	session_cache_limiter('private_no_expire');
	session_start();
	unset($_SESSION['SFM']);
	$sfm_script = $script_name;
	include_once($temp_html['form']);
}
exit;


// ���饹���
class sfmClass
{
	function sfmClass() {
		// ��С����ץ������б�
		$_SERVER['HTTP_HOST'] = isset($_SERVER['HTTP_X_FORWARDED_HOST']) ?
		$_SERVER['HTTP_X_FORWARDED_HOST'] : $_SERVER['HTTP_HOST'];
		$_SERVER['REMOTE_ADDR'] = isset($_SERVER['HTTP_X_FORWARDED_FOR']) ?
		$_SERVER['HTTP_X_FORWARDED_FOR'] : $_SERVER['REMOTE_ADDR'];
		$_SERVER['SERVER_NAME'] = isset($_SERVER['HTTP_X_FORWARDED_SERVER']) ?
		$_SERVER['HTTP_X_FORWARDED_SERVER'] : $_SERVER['SERVER_NAME'];
	}
	// ƱNAME��ʣ�����ܤη�����
	function valueMarge($key, $val, $name_marge) {
		$name = preg_replace('/(.+)_s$/', "$1", $key);
		$rep = (array_key_exists($name, $name_marge)) ? $name_marge[$name] : "\t";
		$set_err = 0;
		foreach ($val as $tmp_key => $tmp_val) {
			if ($tmp_val == 'none') $tmp_val = '';
			if (preg_match('/_s$/', $key) && ($tmp_val == '')) $set_err = 1;
			if ($tmp_val == '') unset($val[$tmp_key]);
		}
		if ($set_err == 1 && array_values($val)) return '__Error_Marge_Data__';
		$val = implode($rep, $val);
		return $val;
	}
	// HTML�ǡ�����Ǽ
	function formDataHtml() {
		if (!isset($_SESSION['SFM'])) return false;
		$arr = $_SESSION['SFM'];
		$array_data = array();
		foreach ($arr as $key => $val) {
			$array_data[$key] = $this->valDataHtml($val);
		}
		if (!isset($array_data['autoReply'])) $array_data['autoReply'] = '&nbsp;';
		return (object) $array_data;
	}
	// HTML�ǡ�������
	function valDataHtml($val) {
		global $temp_err, $baseEnc, $internalEnc;
		$val = (get_magic_quotes_gpc()) ? stripslashes($val) : $val;
		$val = str_replace("\t", "\n", $val); // ɽ���Ѥ�ʣ�����ܤ����
		$val = htmlspecialchars($val, ENT_QUOTES, 'EUC-JP');
		$val = nl2br($val);
		$val = (preg_match('/__Error_.+__/', $val)) ? "<span class=\"ERR\">{$temp_err[$val]}</span>" : $val;
		$val = ($val != '') ? $val : '&nbsp;';
		$val =  mb_convert_encoding($val, $baseEnc, $internalEnc);
		return $val;
	}
	// MAIL�ǡ�����Ǽ
	function formDataMail() {
		if (!isset($_SESSION['SFM'])) return false;
		$arr = $_SESSION['SFM'];
		$array_data = array();
		foreach ($arr as $key => $val) {
			$array_data[$key] = $this->valDataMail($val);
		}
		return (object) $array_data;
	}
	// MAIL�ǡ�������
	function valDataMail($val) {
		$val = (get_magic_quotes_gpc()) ? stripslashes($val) : $val;
		$val = str_replace("\t", ',', $val); // �᡼���Ѥ�ʣ�����ܤ򥫥�޶��ڤ�
		return $val;
	}
	// �᡼����������
	function sendMail($mailTo, $mailSubject, $mailMessage, $mailFrom, $mailBcc) {
		global $scriptVersion, $returnPath;
		if (preg_match('/(.+)(\s<.+\@.+>)$/', $mailFrom, $tmp)) {
			$tmp[1] = mb_encode_mimeheader($tmp[1]);
			$mailFrom = $tmp[1].$tmp[2];
		}
		$mailHeader  = "From: {$mailFrom}\n";
		if ($mailBcc) {
			$mailHeader .= "Bcc: {$mailBcc}\n";
		}
		$php_ver = phpversion();
		$mailHeader .= "X-Mailer: Sapphirus.Biz Formmail/{$scriptVersion}(PHP/{$php_ver})";
		$mailMessage = preg_replace('/\r\n|\r/', "\n", $mailMessage);
		if (isset($returnPath) && $returnPath) {
			mb_send_mail($mailTo, $mailSubject, $mailMessage, $mailHeader, "-f{$returnPath}");
		} else {
			mb_send_mail($mailTo, $mailSubject, $mailMessage, $mailHeader);
		}
		return true;
	}
	// �桼�����������
	function userInfo() {
		$remote_addr = @gethostbyaddr($_SERVER['REMOTE_ADDR']);
		$info  = "{$remote_addr}\n";
		$info .= "{$_SERVER['HTTP_USER_AGENT']}\n";
		$info .= date("Y/m/d - H:i:s");
		return $info;
	}
}


// ���顼ɽ��HTML
function Err($err) {
	echo <<< EOM
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=euc-jp" />
<title>Error: {$err}</title>
</head>
<body style="font-size: 12px; line-height: 1.8em">
<strong>Error: </strong>{$err}<br>
<input type="button" value="���" onclick="history.back()">
</body>
</html>

EOM;
	exit;
}


// HTML�ǡ��������ʵ�ƥ�ץ졼���ѡ�
function FORM_DATA_H($name) {
	global $sfm_class;
	$val = (isset($_SESSION['SFM'][$name])) ? $sfm_class->valDataHtml($_SESSION['SFM'][$name]) : '&nbsp;';
	return $val;
}
// MAIL�ǡ��������ʵ�ƥ�ץ졼���ѡ�
function FORM_DATA_M($name) {
	global $sfm_class;
	$val = (isset($_SESSION['SFM'][$name])) ? $sfm_class->valDataMail($_SESSION['SFM'][$name]) : '&nbsp;';
	return $val;
}
// �桼������������ʵ�ƥ�ץ졼���ѡ�
function USERINFO() {
	global $sfm_class;
	$val = $sfm_class->userInfo();
	return $val;
}

?>
