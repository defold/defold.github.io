function search(searchfield_id, searchresult_id) {
	if (!String.format) {
		String.format = function(format) {
			var args = Array.prototype.slice.call(arguments, 1);
			return format.replace(/{(\d+)}/g, function(match, number) {
				return typeof args[number] != 'undefined'
				? args[number]
				: match;
			});
		};
	}

	var fmt = "<a href='/{0}'><p>{1}<br/>\n"
	+ "<span style='font-size: smaller; text-decoration: none;'>{2}</span></p></a>\n";

	var query = new URLSearchParams(window.location.search).get('q');
	if (query) {
		document.getElementById(searchfield_id).value = query;

		var div = document.getElementById(searchresult_id);
		div.innerHTML = "Searching...";
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
			// 4 == DONE
			if (this.readyState == 4) {
				if (this.status == 200) {
					div.innerHTML = "";
					var idx = lunr.Index.load(JSON.parse(this.responseText));
					var results = idx.search("*" + query + "*");
					results.forEach(function(result, index) {
						var keys = Object.keys(result.matchData.metadata).join(", ");
						if (keys.length > 50) { keys = keys.substring(0, 50) + "..."; }
						div.innerHTML = div.innerHTML + String.format(fmt, result.ref, result.ref, keys)
					});
				}
				else {
					div.innerHTML = "Error while searching";
				}
			}
		};
		xhttp.open("GET", "/searchindex.json", true);
		xhttp.send();
	}
}
