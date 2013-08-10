jQuery(document).ready(function(){
//drop-down menu
	jQuery("div.menu ul ul li:has(ul)").find("a:first").append(" &raquo;");
});