jQuery(document).ready(function(){
//search box
	var tl_keyword='Search';
	jQuery(".mainsearch .keyword").val(tl_keyword);
	jQuery(".mainsearch").hover(
		function () {
			jQuery(".mainsearch .keyword").css('visibility', 'visible');
			jQuery(this).addClass("mainsearch_hover");
		},	
		function () {
			if(jQuery(".mainsearch .keyword").val()==tl_keyword){
				jQuery(".mainsearch .keyword").css('visibility', 'hidden');
				jQuery(this).removeClass("mainsearch_hover");
			}
	});
	jQuery(".mainsearch .keyword").bind("focus", function(){
  		if(jQuery(this).val()==tl_keyword) jQuery(this).val('');
	});
	
	jQuery(".mainsearch .keyword").bind("blur", function(){
  		if(jQuery(this).val()==''){
  			jQuery(this).val(tl_keyword);
  			jQuery(this).css('visibility', 'hidden');
  			jQuery(".mainsearch").removeClass("mainsearch_hover");
  		}
	});
});
