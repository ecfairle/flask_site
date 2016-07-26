$(document).ready(function() {
  	$menuLeft = $('.pushmenu-left');
	$nav_list = $('#nav_list');
	  
	$('#menu_button').on('click','#nav_list',function() {
	 	$(this).toggleClass('active');
	  	$('.pushmenu-push').toggleClass('pushmenu-push-toright');
	    $menuLeft.toggleClass('pushmenu-open');
	});

	/*
		Login with ajax request: definitely bad practice but interesting
	*/
	/*$('#login_form').on('submit',function(){
	  	$.ajax({
	        type: 'POST',
	        url: '/login',
	        data: $('form').serialize(),
	        beforeSend: function() {
                $('#main_block').animate({opacity:0, top: '+=100px'},30);
            },
	        success: function(msg,s,req) {
	        	alert(msg.getElementById('home_container'));
	            $('#main_block').load(msg + '#home_container', function(){
	            	$('#main_block').animate({opacity:1, top: '-=100px'},30, function(){
	            		$('#menu_button').html('<div class="menuIcon">\
	            		<a id="nav_list" href="#">&#9776;</a></div>');
	            	});
	            });	            
	            history.pushState({Title: 'index', Url: 'index'},'index','index');
	        },
	        error: function(msg) {
	        	alert('---');
	        }
	    });
	  	return false;
	});*/


	window.onpopstate = function(e){
	    if(e.state){
	        document.getElementById("content").innerHTML = e.state.html;
	        document.title = e.state.pageTitle;
	    }
	};

	$menu_items = $('#home,#about');
	$menu_items.on('click',function(){
		$('#main_block').animate({opacity:0},5);
		$('#main_block').load($(this).attr('url') + ' #home_container', 
			function(){
	        $('#main_block').animate({opacity:1},5);
			}
	   	);
		$(".links li a.active").removeClass("active");
		$(this).addClass("active");
		return false;
	});
});