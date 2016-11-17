<?php

/*----------------------------------------------------------------------------------
	フォームメール - sformmmail2
	(c)sapphirus.biz
----------------------------------------------------------------------------------*/


/* 追加オプション設定 */

// リファラによる外部使用の制限（する:1/しない:0）
$refCheck = 1;

// 文字化けする場合は1にしてみて下さい
$ill_char = 0;

// 「表」などの文字のあとに「\」が付いてしまう場合は1にしてみて下さい
$ill_slash = 0;

// httpsでの利用の場合1にして下さい
// ※ドメインにsecureもしくはsslが含まれる場合は常に設定されます
$use_ssl = 0;

// 設定ファイル読み込み
include_once('sfm_config.php');

// HTML&メールテンプレート設定
$temp_html = array(
	'form'			=> 'sfm_form.html' // 入力フォーム用
,	'confirm'		=> 'sfm_confirm.html' // 確認画面用
,	'completion'	=> 'sfm_completion.html' // 送信完了画面
,	'mail'			=> 'sfm_mail_tmpl.php' // メール送信用
,	'reply'			=> 'sfm_reply_tmpl.php' // 自動返信メール用
);

// エラー表示設定
$temp_err = array(
	'__Error_Input_Data__'		=> '<span style="color:red;">未入力です</span>'
,	'__Error_Marge_Data__'		=> 'Error'
,	'__Error_Mail_Address__'	=> 'Error'
,	'__Error_Mail_Check__'		=> 'Error'
,	'__Error_Max_Text__'		=> "Error"
);

// 同NAMEの複数項目の結合設定
$name_marge = array(
	'tel'		=> '-'
,	'fax'		=> '-'
,	'zip'		=> '-'
,	'address'	=> "\n"
);

// submit表示項目
function printSubmit() {
	if($_SESSION['SFM']['InputErr']) {
		// エラーがある場合のHTML出力
		$submit = <<< EOD
<input type="button" value="戻る" onclick="history.back()" class="back" />
EOD;
	} else {
		// 項目が正しい場合のHTML出力
		$submit = <<< EOD
<input type="hidden" name="mode" id="mode" value="SEND" />
<input type="button" value="戻る" onclick="history.back()" class="back" />
<input type="submit" value="送信" class="mail" />
EOD;
	}
	return $submit;
}


/* メインプログラム */

$scriptVersion = '2.51';
$sfm_class = new sfmClass();

// 内部エンコードを設定
if (!extension_loaded('mbstring')) {
	Err('Error: mbstring関数が利用できません');
}
$internalEnc = 'EUC-JP';
mb_language('ja');
mb_internal_encoding($internalEnc);

if (!isset($mailTo[0])) {
	Err('受取先メールアドレスが設定されてません');
}
$mode = (isset($_POST['mode'])) ? $_POST['mode'] : '';
$script_name = preg_replace('/.+\/(.*)/', "$1", $_SERVER['REQUEST_URI']);

// モードによる分岐
switch ($mode) {
case 'SEND': // メール送信
	session_cache_limiter('nocache');
	session_start();
	if (!isset($_SESSION['SFM'])) {
		Err('セッションデータがありません');
	}
	$sfm_mail = $sfm_class->formDataMail();
	$sfm_userinfo = $sfm_class->userInfo();
	$mailTo = (isset($mailTo[$_SESSION['SFM']['mailToNum']])) ? $mailTo[$_SESSION['SFM']['mailToNum']] : $mailTo[0];
	// 指定先にメール送信
	$mailFrom = (!isset($_SESSION['SFM']['email'])) ? 'S.B. Formmail' : $_SESSION['SFM']['email'];
	include_once($temp_html['mail']);
	$sfm_class->sendMail($mailTo, $mailSubject, $mailMessage, $mailFrom, $mailBcc);
	// メール自動返信
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

case 'CONFIRM': // データ処理と確認
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
		Err('外部から利用は出来ません');
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

default: // 入力フォーム表示
	session_cache_limiter('private_no_expire');
	session_start();
	unset($_SESSION['SFM']);
	$sfm_script = $script_name;
	include_once($temp_html['form']);
}
exit;


// クラス定義
class sfmClass
{
	function sfmClass() {
		// リバースプロクシに対応
		$_SERVER['HTTP_HOST'] = isset($_SERVER['HTTP_X_FORWARDED_HOST']) ?
		$_SERVER['HTTP_X_FORWARDED_HOST'] : $_SERVER['HTTP_HOST'];
		$_SERVER['REMOTE_ADDR'] = isset($_SERVER['HTTP_X_FORWARDED_FOR']) ?
		$_SERVER['HTTP_X_FORWARDED_FOR'] : $_SERVER['REMOTE_ADDR'];
		$_SERVER['SERVER_NAME'] = isset($_SERVER['HTTP_X_FORWARDED_SERVER']) ?
		$_SERVER['HTTP_X_FORWARDED_SERVER'] : $_SERVER['SERVER_NAME'];
	}
	// 同NAMEの複数項目の結合処理
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
	// HTMLデータ格納
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
	// HTMLデータ整形
	function valDataHtml($val) {
		global $temp_err, $baseEnc, $internalEnc;
		$val = (get_magic_quotes_gpc()) ? stripslashes($val) : $val;
		$val = str_replace("\t", "\n", $val); // 表示用に複数項目を改行
		$val = htmlspecialchars($val, ENT_QUOTES, 'EUC-JP');
		$val = nl2br($val);
		$val = (preg_match('/__Error_.+__/', $val)) ? "<span class=\"ERR\">{$temp_err[$val]}</span>" : $val;
		$val = ($val != '') ? $val : '&nbsp;';
		$val =  mb_convert_encoding($val, $baseEnc, $internalEnc);
		return $val;
	}
	// MAILデータ格納
	function formDataMail() {
		if (!isset($_SESSION['SFM'])) return false;
		$arr = $_SESSION['SFM'];
		$array_data = array();
		foreach ($arr as $key => $val) {
			$array_data[$key] = $this->valDataMail($val);
		}
		return (object) $array_data;
	}
	// MAILデータ整形
	function valDataMail($val) {
		$val = (get_magic_quotes_gpc()) ? stripslashes($val) : $val;
		$val = str_replace("\t", ',', $val); // メール用に複数項目をカンマ区切り
		return $val;
	}
	// メール送信処理
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
	// ユーザー情報取得
	function userInfo() {
		$remote_addr = @gethostbyaddr($_SERVER['REMOTE_ADDR']);
		$info  = "{$remote_addr}\n";
		$info .= "{$_SERVER['HTTP_USER_AGENT']}\n";
		$info .= date("Y/m/d - H:i:s");
		return $info;
	}
}


// エラー表示HTML
function Err($err) {
	echo <<< EOM
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=euc-jp" />
<title>Error: {$err}</title>
</head>
<body style="font-size: 12px; line-height: 1.8em">
<strong>Error: </strong>{$err}<br>
<input type="button" value="戻る" onclick="history.back()">
</body>
</html>

EOM;
	exit;
}


// HTMLデータ整形（旧テンプレート用）
function FORM_DATA_H($name) {
	global $sfm_class;
	$val = (isset($_SESSION['SFM'][$name])) ? $sfm_class->valDataHtml($_SESSION['SFM'][$name]) : '&nbsp;';
	return $val;
}
// MAILデータ整形（旧テンプレート用）
function FORM_DATA_M($name) {
	global $sfm_class;
	$val = (isset($_SESSION['SFM'][$name])) ? $sfm_class->valDataMail($_SESSION['SFM'][$name]) : '&nbsp;';
	return $val;
}
// ユーザー情報取得（旧テンプレート用）
function USERINFO() {
	global $sfm_class;
	$val = $sfm_class->userInfo();
	return $val;
}

?>
