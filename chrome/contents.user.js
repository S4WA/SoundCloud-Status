// ==UserScript==
// @name         SoundCloud-Status
// @homepage     https://github.com/S4WA/soundcloud-status
// @version      1.0.0
// @description  oof
// @author       DripNyan
// @match        https://soundcloud.com/*
// @require      https://code.jquery.com/jquery-3.4.1.min.js
// ==/UserScript==

var start_time = Date.now(), last_title = "";

function post2local() {
	$.ajax({
		url: "http://localhost:8000/",
		type: "post",
		data: {
			"artist": getArtist(),
			"title": getTitle(),
			"playing": isPlaying(),
			// "start_time": start_time,
			// "current_time": getCurrentTime(),
			// "end_time": getEndTime(),
			"artwork": getArtwork()
		}
	})
}

window.onload = () => {
	$.ajax({
		url: "http://localhost:8000/",
		type: "post",
		data: {},
		complete: (xhr, responseText, thrownError) => {
			local_available = (xhr.status == "200");
		}
	});

	setInterval(() => {
		if (last_title != getTitle()) {
			last_title = getTitle();
			start_time = Date.now();
		}
		post2local();
	}, 100);
}

function isPlaying() {
	var cls = ".playControl";
	return $(cls).length != 0 ? $(cls)[0].title == "Pause current" : false;
}

function getTitle() {
	return $("a.playbackSoundBadge__titleLink")[0].title;
}

function getArtist() {
	return $("a.playbackSoundBadge__lightLink")[0].title;
}

function getCurrentTime() {
	return $(".playbackTimeline__timePassed span[aria-hidden]").text();
}

function getEndTime() {
	return $(".playbackTimeline__duration span[aria-hidden]").text();
}

function getArtwork() {
	return $(".playbackSoundBadge span.sc-artwork").css("background-image");
}