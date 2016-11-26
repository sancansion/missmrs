<?php

// 自動返信のSubject（件名）
$replySubject = '【ご応募・ご相談確認メール】';

//送信メッセージ
$replyMessage = <<< EOD
以下の内容でフォームからのお問い合わせを受け付けました。
────────────────
1.お名前
{$sfm_mail->name}

2.生年月日
{$sfm_mail->day1} 年 {$sfm_mail->day2} 月 {$sfm_mail->day3} 日

3.電話番号
{$sfm_mail->tel1} - {$sfm_mail->tel2} - {$sfm_mail->tel3}

4.メールアドレス
{$sfm_mail->email}

5.お住まい
{$sfm_mail->address}

6.経験
{$sfm_mail->ex}

7.希望面接日時
{$sfm_mail->m} 月 {$sfm_mail->d} 日 {$sfm_mail->t} 時頃

8.ご質問・ご要望など
{$sfm_mail->com}
────────────────
EOD;

?>
