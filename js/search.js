function search(searchfield_id, searchresult_id) {
	if (!String.format) { String.format = string_format; }

	var fmt = "<p><a href='/{0}'>{1}</a> - {2}</p>\n";
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
		div.innerHTML = spinner() + '<span class="search-text">Searching...</span>';

		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
			// 4 == DONE
			if (this.readyState == 4) {
				if (this.status == 200) {
					var idx = lunr.Index.load(JSON.parse(this.responseText));
					var results = idx.search(query);
					var weighted_results = to_weighted_results(results, search_keys);

					if (!weighted_results.length) {
						div.innerHTML = "Nothing found";
						return;
					}

					div.innerHTML = "";
					for (var i = 0; i < weighted_results.length; i++) {
						var ref = weighted_results[i].ref;
						var keys = weighted_results[i].keys;

						// Sort keys so that the actual query string matches are first
						keys = sort_results(search_keys, keys);

						// Cleanup the query string so that it highlights the correct words on the pages
						// Creates the top link for all queries
						var keys_str = ""; // a list of links to each keyword: https://domain/path/to/page?q=key
						var keys_str_length = 0; // counts the _visual_ length
						for (var j = 0; j < keys.length; j++) {
							var key = keys[j];
							var key_query = is_api_reference(ref) ?
								// Added "#..." fragment helps to navigate directly to Lua functions and constants in the docs,
								// it also works for almost all C API ref elements that are in the dm* namespaces
								"q=" + encodeURIComponent(key) + "#" + encodeURIComponent(anchor_link_for_key(ref, key)) :
								"q=" + encodeURIComponent(key);

							if (keys_str_length < 64) {
								keys_str_length += key.length;
								keys_str += (keys_str.length > 0 ? ", " : "") + String.format(link_fmt, ref, key_query, key);
							}
							else {
								keys_str += ", ...";
								break; // Don't make the list too long...
							}
						}

						var str = String.format(fmt, ref, ref, keys_str);

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

	//////////////////////////

	function anchor_link_for_key(ref, key) {
		// Namespace could be present in the key, search result examples:
		// ref/stable/gui - animate, gui.animate
		// ref/stable/go - animate, go.animate
		if (key.indexOf(".") !== -1)
			return key.toLowerCase();

		// For dm* methods we do not need to prepend namespace, search result examples:
		// ref/stable/dmBuffer - dmbuffer, dmbuffer::validatebuffer
		// ref/stable/dmProfile - dm_property_u64, dm_property_u32
		if (ref.indexOf("/dm") !== -1)
			return key.toLowerCase();

		// Prepend namespace to match anchor links in API Reference
		return (get_api_namespace(ref) + "." + key).toLowerCase();
	}

	function get_api_namespace(ref) {
		var refParts = ref.split("/");
		const namespace = refParts[refParts.length - 1];
		return namespace;
	}

	function spinner() {
		return '<i class="spinner spin">' +
			'<svg width="100%" height="100%" viewBox="0 0 61 61" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">' +
				'<path d="M57.742,18.072C57.205,16.842 56.588,15.654 55.896,14.515C55.298,13.529 54.644,12.579 53.939,11.671C53.238,10.767 51.935,10.603 51.031,11.306C50.127,12.007 49.963,13.31 50.664,14.214C51.271,14.997 51.836,15.816 52.352,16.665C52.948,17.647 53.481,18.671 53.944,19.731C55.335,22.913 56.106,26.422 56.106,30.126C56.106,37.306 53.202,43.788 48.497,48.495C43.79,53.2 37.308,56.104 30.126,56.106C22.946,56.104 16.464,53.2 11.757,48.495C7.052,43.788 4.148,37.306 4.147,30.126C4.148,22.944 7.052,16.462 11.757,11.755C16.464,7.05 22.946,4.146 30.126,4.146C31.864,4.146 33.558,4.316 35.196,4.64C36.319,4.863 37.411,4.132 37.632,3.007C37.854,1.885 37.123,0.795 36,0.574C34.098,0.197 32.133,-0 30.125,-0C13.486,0.002 0.002,13.488 0,30.127C0.002,46.766 13.486,60.25 30.125,60.252C46.764,60.25 60.25,46.766 60.252,30.127C60.252,25.848 59.357,21.764 57.742,18.072ZM42.346,7.193C43.612,7.869 44.815,8.646 45.946,9.515C46.321,9.804 46.766,9.945 47.208,9.945C47.829,9.945 48.444,9.666 48.853,9.134C49.55,8.226 49.38,6.925 48.472,6.228C47.163,5.22 45.767,4.32 44.3,3.537C43.29,2.996 42.034,3.379 41.495,4.389C40.956,5.399 41.336,6.654 42.346,7.193Z" style="fill:currentColor;fill-rule:nonzero;"/>' +
			'</svg>' +
		'</i>';
	}

	function to_weighted_results(results, search_keys) {
		var weighted_results = [];
		results.forEach(function(result, index) {
			var keys = Object.keys(result.matchData.metadata);
			var keys_str = keys.join(", ");
			if (keys_str.length > 50) { keys_str = keys_str.substring(0, 50) + "..."; }

			var score = result.score + get_score_from_results(search_keys, keys);
			weighted_results.push( {score: score, keys: keys, ref: result.ref} );
		});
		weighted_results.sort(function(a, b) {
			return a.score < b.score ? 1 : -1;
		});
		return weighted_results;
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

	function string_format(format) {
		var args = Array.prototype.slice.call(arguments, 1);
		return format.replace(/{(\d+)}/g, function(match, number) {
			return typeof args[number] != 'undefined'
			? args[number]
			: match;
		});
	}

	function is_api_reference(ref) {
		return ref.match(/^ref\//);
	}
}
