(function ($, window, undefined) {
	'use strict';

	var $doc = $(document),
	Modernizr = window.Modernizr;

	$.fn.foundationAlerts ? $doc.foundationAlerts() : null;
	$.fn.foundationAccordion ? $doc.foundationAccordion() : null;
	$.fn.foundationTooltips ? $doc.foundationTooltips() : null;
	$('input, textarea').placeholder();
	$.fn.foundationButtons ? $doc.foundationButtons() : null;
	$.fn.foundationNavigation ? $doc.foundationNavigation() : null;
	$.fn.foundationTopBar ? $doc.foundationTopBar() : null;
	$.fn.foundationCustomForms ? $doc.foundationCustomForms() : null;
	$.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;

	// Hide address bar on mobile devices
	if (Modernizr.touch) {
		$(window).load(function () {
			setTimeout(function () {
				window.scrollTo(0, 1);
			}, 0);
		});
	}
})(jQuery, this);

window.$g = {}; // global variable

$(function() {
	'use strict';

	var restricteduploader = new qq.FileUploaderBasic({
		button: $('#upload_btn')[0],
		action: '/_admin/upload',
		params: {'path': $g.page.relative_path},
		debug: true,
		multiple: true,
		allowedExtensions: ['jpeg', 'jpg', 'txt', '*'],
		sizeLimit: 3 * 1024 * 1024, // 3 * 1024 * 1024 bytes
		uploadButtonText: 'Upload',
		onSubmit: function(id, fileName) {
		},
		onUpload: function(id, fileName) {},
		onProgress: function(id, fileName) {},
		onComplete: function(id, fileName, responseJson) {},
	});

	$('#mkdir_btn').click(function() {
		$('#mkdir_pnl').reveal();
	});

	$('#mkdir_pnl .submit').click(function() {
		var path = $g.page.path;
		var name = $('#mkdir_pnl input').val();
		$.post('/_admin/mkdir', {path: path, name: name},
		   	function(data) {
			// TODO
			}
		);
		return false;
	});

});
