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

	// upload
	var restricteduploader = new qq.FileUploaderBasic({
		button: $('#upload_btn')[0],
		action: '/_admin/upload',
		params: {'path': $g.page.path},
		debug: true,
		multiple: true,
		allowedExtensions: ['jpeg', 'jpg', 'txt', 'png'],
		sizeLimit: 3 * 1024 * 1024, // 3 * 1024 * 1024 bytes
		uploadButtonText: 'Upload',
		onSubmit: function(id, fileName) { // TODO
		},
		onUpload: function(id, fileName) {}, // TODO
		onProgress: function(id, fileName) {}, // TODO
		onComplete: function(id, fileName, responseJson) {
			window.location.reload(); // TODO
		},
	});

	// mkdir
	$('#mkdir_btn').click(function() {
		$('#mkdir_pnl').reveal();
	});

	$('#mkdir_pnl .submit').click(function() {
		var path = $g.page.path;
		var name = $('#mkdir_pnl input').val();
		$.post('/_admin/mkdir', {path: path, name: name},
		   	function(data) {
				window.location.reload();// TODO
			}
		).error(function() {
			alert('Error'); // TODO
		});
		return false;
	});

	// delete
	$('.hover-toggle').hover(
		function() {$(this).find('.hover-toggle-btn').removeClass('hidden')},
		function() {$(this).find('.hover-toggle-btn').addClass('hidden')}
	);
	$('.hover-toggle-btn').click(function () {
		$.post('/_admin/delete', {path: $g.page.path, name: $(this).parents('.item').find('.name').html()},
		   	function(data) {
				window.location.reload();
			}
		);
	});

});