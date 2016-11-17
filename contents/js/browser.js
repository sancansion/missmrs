//ブラウザチェック
//**************************************************
//ブラウザ判別
//BrowserType			Version				OS
//1:netscape			(2, 3, 4)
//2:safari				(5)
//3:firefox, mozilla	(5)
//4:ie					(3, 4, 5, 5.5, 6)
//5:opera				(5, 6, 7, 8, 9)
//**************************************************
function clsBrowser() {
	this.BrowserType;
	this.Version;
	this.OS;

	if(navigator.appName.charAt(0)=="N"){
		if(navigator.appVersion.charAt(0)==2){
			this.BrowserType=1;
			this.Version=2;
		}else if(navigator.appVersion.charAt(0)==3){
			this.BrowserType=1;
			this.Version=3;
		}else if(navigator.appVersion.charAt(0)==4){
			this.BrowserType=1;
			this.Version=4;
		}else if(navigator.appVersion.charAt(0)==5){
			if(navigator.userAgent.indexOf("Netscape6/")!=-1 || navigator.userAgent.indexOf("Netscape/6")!=-1){
				this.BrowserType=1;
				this.Version=6;
			}else if(navigator.userAgent.indexOf("Netscape7/")!=-1 || navigator.userAgent.indexOf("Netscape/7")!=-1){
				this.BrowserType=1;
				this.Version=7;
			}else if(navigator.userAgent.indexOf("Safari")!=-1){
				this.BrowserType=2;
				this.Version=5;
			}else if(navigator.userAgent.indexOf("Firefox")!=-1){
				this.BrowserType=3;
				if(navigator.userAgent.indexOf("Firefox/1")!=-1){
					this.Version=5;
				}else if(navigator.userAgent.indexOf("Firefox/2")!=-1){
					this.Version=5;
				}
			}else if(navigator.userAgent.indexOf("Gecko")!=-1){
				this.BrowserType=3;
				this.Version=5;
			}
		}
	}else if(navigator.appName.charAt(0)=="M"){
		//old IE
		if(navigator.appVersion.charAt(0)==2 || navigator.appVersion.charAt(0)==3){
			this.BrowserType=4;
			this.Version=3;
		}else if(navigator.appVersion.charAt(0)==4){
			//old opera
			if(navigator.userAgent.indexOf("Opera")!=-1){
				this.BrowserType=5;
				if(navigator.userAgent.indexOf("Opera 7")!=-1)		this.Version=7;
				else if(navigator.userAgent.indexOf("Opera 6")!=-1)	this.Version=6;
				else												this.Version=5;
			}else{
				//current IE
				this.BrowserType=4;
				if(navigator.appVersion.indexOf("MSIE 7")!=-1)			this.Version=7;
				else if(navigator.appVersion.indexOf("MSIE 6")!=-1)		this.Version=6;
				else if(navigator.appVersion.indexOf("MSIE 5.5")!=-1)	this.Version=5.5;
				else if(navigator.appVersion.indexOf("MSIE 5")!=-1)		this.Version=5;
				else													this.Version=4;
			}
		}
	}else if(window.opera){
		//new opera
		this.BrowserType=5;
		if(navigator.userAgent.indexOf("Opera/7")!=-1)		this.Version=7;
		else if(navigator.userAgent.indexOf("Opera/8")!=-1)	this.Version=8;
		else if(navigator.userAgent.indexOf("Opera/9")!=-1)	this.Version=9;
	}else{
		this.BrowserType=navigator.appName;
		this.Version=navigator.appVersion;
	}

	//OS判別
	var ua = navigator.userAgent.toUpperCase();
	if(ua.indexOf("MAC")!=-1)		this.OS="MacOS";
	else if(ua.indexOf("WIN")!=-1)	this.OS="Windows";
	else if(ua.indexOf("X11")!=-1)	this.OS="UNIX";
}
var mclsBrowser = new clsBrowser();
