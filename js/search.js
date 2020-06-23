
function get_score(key, result) {
	if (key === result) {
		return 1.0;
	}

	if (result.startsWith(key))
		return 0.6;
	if (result.endsWith(key))
		return 0.5;
	if (result.includes(key))
		return 0.4;

	return 0.0;
}

// sorts the result list based on a score
// the score is based on the search keys
function sort_results(search_keys, results) {
	var weighted_results = []
	for(var r=0; r<results.length; ++r) {
		var max_score = 0.0;
		for (var s=0; s<search_keys.length;++s) {

			var score = get_score(search_keys[s], results[r]);
			if (score > max_score)
				max_score = score;
		}

		weighted_results.push( {score: max_score, value: results[r]} );
	}

	weighted_results.sort(function(a, b) {
		return a.score < b.score ? 1 : -1;
	});
	var sorted_keys = []
	for(var i=0; i < weighted_results.length; i++) {
		sorted_keys.push(weighted_results[i].value);
	}
	return sorted_keys;
}

// For each result, calculate a score.
// Return the sum of these scores
function get_score_from_results(search_keys, results) {
	var out_score = 0.0;
	for(var r=0; r<results.length; ++r) {

		// If the result contains several searck keys, we want it to score higher
		var combined_result_score = 0;
		var search_key_count = 0;
		for (var s=0; s<search_keys.length;++s) {

			var result_score = get_score(search_keys[s], results[r]);
			if (result_score > 0) {
				search_key_count++;
				combined_result_score += result_score;
			}
		}
		out_score += search_key_count * combined_result_score;
	}
	return out_score;
}

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

	var fmt = "<p><a href='/{0}?{2}'>{1}</a> - {3}</p>\n";
	var link_fmt = "<a href='/{0}?{1}'>{2}</a>";
	var query_fmt = "*{0}*^{1}";

	var query = new URLSearchParams(window.location.search).get('q');
	if (query) {
		document.getElementById(searchfield_id).value = query;

		var search_keys = query.split(/[\s]/);
		if (!search_keys) {
			search_keys = [query];
		}

		var patched_search_keys = []
		for(var i=0; i<search_keys.length; i++){
			var token = search_keys[i];
			while (token.startsWith("*"))
				token=token.substring(1,token.length);
			while (token.endsWith("*"))
				token=token.substring(0,token.length-1);

			patched_search_keys[i] = String.format(query_fmt, token, search_keys.length-i);
		}
		query = patched_search_keys.join(" ");
		console.log("query", query);

		var div = document.getElementById(searchresult_id);
		div.innerHTML = "Searching...";
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
			// 4 == DONE
			if (this.readyState == 4) {
				if (this.status == 200) {
					div.innerHTML = "";
					var idx = lunr.Index.load(JSON.parse(this.responseText));
					var results = idx.search(query);
					var weighted_results = []
					results.forEach(function(result, index) {
						var keys = Object.keys(result.matchData.metadata)
						var keys_str = keys.join(", ");
						if (keys_str.length > 50) { keys_str = keys_str.substring(0, 50) + "..."; }
						//console.log("result", result, index, keys);

						var score = result.score + get_score_from_results(search_keys, keys);
						weighted_results.push( {score: score, keys: keys, ref: result.ref} );
					});

					weighted_results.sort(function(a, b) {
						return a.score < b.score ? 1 : -1;
					});

					for(var i=0; i < weighted_results.length; i++) {
						var ref = weighted_results[i].ref;
						var keys = weighted_results[i].keys;

						// Sort keys so that the actual query string matches are first
						keys = sort_results(search_keys, keys);

						// Cleanup the query string so that it highlights the correct words on the pages
						// Creates the top link for all queries
						var keys_str = ""; // a list of links to each keyword: https://domain/path/to/page?q=key
						var keys_str_length = 0; // counts the _visual_ length
						var is_truncated = false;
						for(var j=0; j<keys.length; j++){
							var key = keys[j];
							var key_query = "q="+encodeURIComponent(key);

							if (keys_str_length < 64) {
								keys_str_length += key.length;
								keys_str += (keys_str.length > 0 ? ", " : "") + String.format(link_fmt, ref, key_query, key);
							}
							else {
								is_truncated = true;
							}
						}

						// Don't make the list too long...
						if (is_truncated)
							keys_str += ", ..."

						// Since the key words already their own query,
						// it seems best to just make the page link to the top of the page
						var page_query = "";

						var str = String.format(fmt, ref, ref, page_query, keys_str);

						div.innerHTML = div.innerHTML + str;
					}
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
