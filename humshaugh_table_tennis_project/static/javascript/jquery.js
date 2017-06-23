$(document).ready(function() {
	$(document).scroll(function(e) { 
		//grab position of scrollbar
		var position=$(document).scrollTop();
		//when position match a height
		var desired_height = 220;
		if(position>=desired_height)
		{
		  //grab element 
			$('#news_block_2').css({'position': 'fixed',			
									'top': '10px',
									'right': '0'
			});
		} else {
			$('#news_block_2').css({'position': 'relative',						
									'top' : '0'
			});
		}
	});
	
});