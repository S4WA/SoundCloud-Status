function post2local() {
	$.ajax({
		url: "http://localhost:8000/",
		type: "post",
		data: {
			"artist": getArtist(),
			"title": getTitle(),
			"playing": isPlaying()
		}
	})
	// .done( (data) => {
	// 	console.log("done:", data)
	// } )
	// .fail( (data) => {
	// 	console.log("fail:", data)
	// } )
}