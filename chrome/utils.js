// Inject to soundcloud
function isPlaying() {
	var cls = ".playControl";
	return $(cls).length != 0 ? $(cls)[0].title == "Pause current" : false;
}

function getTrack() {
	var cls = "a.playbackSoundBadge__titleLink";
	return $(cls).length != 0 ? ( getTitle() + " By " + getArtist() ) : null;
}

function getTitle() {
	return $("a.playbackSoundBadge__titleLink")[0].title;
}

function getArtist() {
	return $("a.playbackSoundBadge__lightLink")[0].title;
}

function getArtwork() {
	return $(".playbackSoundBadge span.sc-artwork").css("background-image");
}

function getLink() {
	var cls = ".playbackSoundBadge__titleLink.sc-truncate";
	return $(cls).length != 0 ? $(cls)[0].href : null;
}

function isLiked() {
	var cls = ".playControls__soundBadge .sc-button-like";
	return $(cls).length != 0 ? $(cls)[0].title == "Unlike" : false;
}

function getCurrentTime() {
	return $(".playbackTimeline__timePassed span[aria-hidden]").text();
}

function getEndTime() {
	return $(".playbackTimeline__duration span[aria-hidden]").text();
}

function getVolume() {
	return Number($(".volume__sliderWrapper").attr("aria-valuenow"))*100;
}

function isMuted() {
	var cls = ".volume";
	return $(cls).length != 0 ? $(cls)[0].className.includes("muted") : false;
}
