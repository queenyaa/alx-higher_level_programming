document.addEventListener('DOMContentLoaded', function () {
	function fetchTranslation() {
		const lang = $('input#language_code').val();
		$.get(
			'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
        function (content) {
			$('div#hello').text(content.hello);
		},
			'json'
		);
	}

	$('input#btn_translate').on('click', fetchTranslation);
	$('input#language_code').on('keypress', function (event) {
		if (event.key === 'Enter') {
			fetchTranslation();
		}
	});
});
