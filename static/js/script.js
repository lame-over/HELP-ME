let button = document.getElementById('button');

window.onscroll = function(){
	topFunction();
}

function topFunction(){
	if (document.documentElement.scrollTop > 100){
		button.style.opacity = '1';
		button.style.visibility = 'visible';
	}else{
		button.style.opacity = '0';
		button.style.visibility = 'hidden';
	}
}

function myFunction(){
	document.documentElement.scrollTop = 0;
}

document.documentElement.setAttribute('style', 'scroll-behavior: smooth;');