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
