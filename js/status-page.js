(function () {
	var OPERATIONAL_STATUS = "Operational";
	var UNREACHABLE_STATUS = "Unreachable";
	var DEGRADED_STATUS = "NotFullyOperational";

	function getState(rawStatus) {
		if (rawStatus === OPERATIONAL_STATUS) {
			return "operational";
		}
		if (rawStatus === UNREACHABLE_STATUS) {
			return "unreachable";
		}
		return "degraded";
	}

	function getLabel(rawStatus) {
		if (rawStatus === DEGRADED_STATUS) {
			return "Not fully operational";
		}
		return rawStatus;
	}

	function createPlatformCard(name, rawStatus) {
		var state = getState(rawStatus);
		var card = document.createElement("article");
		card.className = "status-platform-card status-platform-card-" + state;

		var heading = document.createElement("h4");
		heading.className = "status-platform-card-title";
		heading.textContent = name;

		var pill = document.createElement("span");
		pill.className = "status-health-pill status-health-pill-" + state;
		pill.textContent = getLabel(rawStatus);

		card.appendChild(heading);
		card.appendChild(pill);
		return card;
	}

	function updateOverview(root, state, title, summary) {
		var titleNode = root.querySelector("[data-status-title]");
		var summaryNode = root.querySelector("[data-status-summary]");

		if (titleNode) {
			titleNode.className = "status-health-pill status-health-pill-" + state;
			titleNode.textContent = title;
		}

		if (summaryNode) {
			summaryNode.textContent = summary;
		}
	}

	function renderStatus(root, response) {
		var grid = root.querySelector("[data-status-grid]");
		var entries = Object.keys(response || {}).sort(function (left, right) {
			return left.localeCompare(right);
		});
		var operationalCount = 0;
		var unreachableCount = 0;

		if (!grid) {
			return;
		}

		grid.innerHTML = "";

		if (!entries.length) {
			updateOverview(root, "degraded", "No status returned", "The health report endpoint did not return any platform builders.");
			return;
		}

		entries.forEach(function (name) {
			var rawStatus = response[name];
			var state = getState(rawStatus);
			if (state === "operational") {
				operationalCount += 1;
			} else if (state === "unreachable") {
				unreachableCount += 1;
			}
			grid.appendChild(createPlatformCard(name, rawStatus));
		});

		if (unreachableCount === entries.length) {
			updateOverview(root, "unreachable", "Unreachable", "None of the " + entries.length + " reported platform builders could be reached.");
			return;
		}

		if (operationalCount === entries.length) {
			updateOverview(root, "operational", "Operational", "All " + entries.length + " reported platform builders are operational.");
			return;
		}

		updateOverview(root, "degraded", "Not fully operational", operationalCount + " of " + entries.length + " reported platform builders are operational.");
	}

	function renderError(root) {
		var grid = root.querySelector("[data-status-grid]");
		if (grid) {
			grid.innerHTML = "";
		}
		updateOverview(root, "unreachable", "Unreachable", "Could not reach the public health report endpoint.");
	}

	function loadPanel(root) {
		var url = root.getAttribute("data-status-url");
		if (!url) {
			return;
		}

		fetch(url, {
			method: "GET",
			headers: {
				Accept: "application/json"
			},
			cache: "no-store"
		})
			.then(function (response) {
				if (!response.ok) {
					throw new Error("Unexpected status " + response.status);
				}
				return response.json();
			})
			.then(function (payload) {
				renderStatus(root, payload);
			})
			.catch(function () {
				renderError(root);
			});
	}

	Array.prototype.forEach.call(document.querySelectorAll("[data-status-root]"), loadPanel);
})();
