//投稿記事テキストエリアのid属性名
var target_id  = 'codeSpan';

//プレビュー領域のid属性名
var preview_id = 'preview';


function getTarget(){
    return document.getElementById(target_id);
}

function getPreview(){
    return document.getElementById(preview_id);
}

//fontコードをタグに置換
function replace_tagcod_to_src(val) {

	val = val.replace(/\<太>/ig,   '<strong>');
	val = val.replace(/\<\/太>/ig, '</strong>');
	val = val.replace(/\<斜>/ig,   '<em>');
	val = val.replace(/\<\/斜>/ig, '</em>');
	val = val.replace(/\<下>/ig,   '<u>');
	val = val.replace(/\<\/下>/ig, '</u>');
	val = val.replace(/\<消>/ig,   '<del>');
	val = val.replace(/\<\/消>/ig, '</del>');
	val = val.replace(/\<点>/ig,   '<blink>');
	val = val.replace(/\<\/点>/ig, '</blink>');
	
	//netscape firefoxでマーキーにならないし消えてしまう？？？
	val = val.replace(/\<動>/ig,   '<marquee loop="-1" behavior="alternate" scrolldelay="50">');
	val = val.replace(/\<\/動>/ig, '</marquee>');
	
	val = val.replace(/\<左>/ig,   '<div align=left>');
	val = val.replace(/\<\/左>/ig, '</div>');
	val = val.replace(/\<中>/ig,   '<div align=center>');
	val = val.replace(/\<\/中>/ig, '</div>');
	val = val.replace(/\<右>/ig,   '<div align=right>');
	val = val.replace(/\<\/右>/ig, '</div>');
	
	val = val.replace(/\<特>/ig,   '<font size=+4>');
	val = val.replace(/\<\/特>/ig, '</font>');
	val = val.replace(/\<大>/ig,   '<font size=+2>');
	val = val.replace(/\<\/大>/ig, '</font>');
	val = val.replace(/\<小>/ig,   '<font size=-2>');
	val = val.replace(/\<\/小>/ig, '</font>');
	
	val = val.replace(/\<赤>/ig,   '<font color=#ff0000>');
	val = val.replace(/\<\/赤>/ig, '</font>');
	val = val.replace(/\<橙>/ig,   '<font color=#ff6600>');
	val = val.replace(/\<\/橙>/ig, '</font>');
	val = val.replace(/\<緑>/ig,   '<font color=#009900>');
	val = val.replace(/\<\/緑>/ig, '</font>');
	val = val.replace(/\<黄>/ig,   '<font color=#ffff00>');
	val = val.replace(/\<\/黄>/ig, '</font>');
	val = val.replace(/\<桃>/ig,   '<font color=#ff0066>');
	val = val.replace(/\<\/桃>/ig, '</font>');
	val = val.replace(/\<青>/ig,   '<font color=#0000ff>');
	val = val.replace(/\<\/青>/ig, '</font>');
	val = val.replace(/\<水>/ig,   '<font color=#00ffff>');
	val = val.replace(/\<\/水>/ig, '</font>');
	val = val.replace(/\<白>/ig,   '<font color=#cccccc>');
	val = val.replace(/\<\/白>/ig, '</font>');
	val = val.replace(/\<黒>/ig,   '<font color=#000000>');
	val = val.replace(/\<\/黒>/ig, '</font>');

	val = val.replace(/\<画>/ig,   '<img src=');
	val = val.replace(/\<\/画>/ig, '>');
	
	return val;
}

//コードが変更されたときにプレビュー表示
function codeChange(){
	target_obj = getTarget();
	preview_obj= getPreview();

	if(target_obj != null && preview_obj!=null){
	    var ret_val = target_obj.value;
	    	    
	    ret_val = replace_tagcod_to_src(ret_val);
	    
	    //プレビュー部に内容を表示
	    preview_obj.innerHTML = "" + ret_val;
	    
	}
}

function codeHtmlChange(){
	target_obj = getTarget();
	preview_obj= getPreview();

	if(target_obj != null && preview_obj!=null){
	    var ret_val = target_obj.value;
	    
	    ret_val = replace_tagcod_to_src(ret_val);
	    ret_val = replace_crlf_to_src(ret_val);
	    
	    //プレビュー部に内容を表示
	    preview_obj.innerHTML = "" + ret_val;
	    
	}
}

function replace_crlf_to_src(val)
{
    val = val.replace(/\x0D\x0A|\x0D|\x0A/g,　"");    
    return val;
}

//テキスト文字装飾
function updateFont(command1, command2) {
	target_obj = getTarget();
	
	//if(typeof(target_obj)=='object') {
	if(target_obj != null){
		target_obj.focus();
		if(mclsBrowser.BrowserType==4 && mclsBrowser.Version>=5.5) {	//IE && version >= 5.5
			var rng = document.selection.createRange();
			if(rng) {
				if(rng.text!=undefined) {
					rng.text = command1 + rng.text + command2;
				}
			}
		} else if(mclsBrowser.BrowserType==3 && mclsBrowser.Version >= 5) {		//mozilla
			var s1 = target_obj.value.substring(0, target_obj.selectionStart);
			var s2 = target_obj.value.substring(target_obj.selectionEnd, target_obj.value.length);
			var s3 = target_obj.value.substring(target_obj.selectionStart, target_obj.selectionEnd)
			target_obj.value = s1 + command1 + s3 + command2 + s2;
		} else if(mclsBrowser.BrowserType==2 || mclsBrowser.BrowserType==5) {	//safari && opera
			target_obj.value += command1 + command2;
		}
		else
		{
			target_obj.value += command1 + command2;
		}
		
		codeChange();
	} else {
		alert("文字を書き込む場所をクリックしてください。");
	}
}


//&#文字をエスケープしてHTMLエンコード
function sanitizer3(val) {
	val = escape_unicodeemoji(val);
	var ret_val = sanitizer(val);
	return reescape_unicodeemoji(ret_val);
}

//&#文字をエスケープしてHTMLエンコード
function sanitizer4(val) {
	val = val.replace(/<a href=\"(.*?)\">(.*?)<\/a>/ig,'$1');
	return val.replace(/&amp;#([0-9]{3,5};?)/g,'&#$1');
}

//HTMLエンコード
//独自タグは変換しない
function sanitizer(val) {
	val = val.replace(/&/ig,   '&amp;');
	val = val.replace(/\\/ig,  '&quot;');
	val = val.replace(/'/ig,   '&#039;');
	val = val.replace(/\<(\/?[^太斜下消点動左中右特大小黒赤青緑橙桃黄水白>]*)>/ig, '&lt;$1&gt;');
	val = val.replace(/\n/ig,  '<br />');
	
	return val;
}

//カラーコード指定　色変更
function changeForeColor(color_code) {
	target_focus();
	
	//赤|橙|緑|黄|桃|青|水|白|黒
	//var oColor = "#"+color_code;
    var command1;
    var command2;
    switch(color_code){
       case "red":
		    command1 = '<赤>';
		    command2 = '</赤>';
		    break;
    	case "orange":
		    command1 = '<橙>';
		    command2 = '</橙>';
	        break;
	    case "green":
		    command1 = '<緑>';
		    command2 = '</緑>';
	        break;
	    case "yellow":
		    command1 = '<黄>';
		    command2 = '</黄>';
	      break;
	    case "pink":
		    command1 = '<桃>';
		    command2 = '</桃>';
	        break;
	    case "blue":
		    command1 = '<青>';
		    command2 = '</青>';
	        break;
	    case "lblue":
		    command1 = '<水>';
		    command2 = '</水>';
	        break;
	    case "white":
		    command1 = '<白>';
		    command2 = '</白>';
	        break;
	    default:
            command1 = '<黒>';
            command2 = '</黒>';
	        break;
	
    }
    updateFont(command1, command2);
}

//テキスト装飾コマンド実行
function execom(command) {
	var command1;
	var command2;
	switch(command){
       case "bold":
		    command1 = '<太>';
		    command2 = '</太>';
		    break;
    	case "italic":
		    command1 = '<斜>';
		    command2 = '</斜>';
	        break;
	    case "underline":
		    command1 = '<下>';
		    command2 = '</下>';
	        break;
	    case "strike":
		    command1 = '<消>';
		    command2 = '</消>';
	      break;
	    case "blink":
		    command1 = '<点>';
		    command2 = '</点>';
	        break;
	    case "marquee":
		    command1 = '<動>';
		    command2 = '</動>';
	        break;
	    case "left":
		    command1 = '<左>';
		    command2 = '</左>';
	        break;
	    case "center":
		    command1 = '<中>';
		    command2 = '</中>';
	        break;
	    case "right":
		    command1 = '<右>';
		    command2 = '</右>';
	        break;
	    case "lbig":
		    command1 = '<特>';
		    command2 = '</特>';
	        break;
	    case "big":
		    command1 = '<大>';
		    command2 = '</大>';
	        break;
	    case "small":
		    command1 = '<小>';
		    command2 = '</小>';
	        break;
	    case "img":
		    command1 = '<画>';
		    command2 = '</画>';
	        break;
	    default:
            command1 = '';
            command2 = '';
	        break;
	}
	updateFont(command1, command2);
}

//入力エリアにフォーカス
function target_focus() {
	target_obj = getTarget();
	target_obj.focus();		
}

