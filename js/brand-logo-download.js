(() => {
	const triggerBlobDownload = (url, blob) => {
		const objectUrl = URL.createObjectURL(blob);
		const link = document.createElement("a");
		const pathname = new URL(url, window.location.href).pathname;
		const filename = pathname.split("/").pop() || "defold-logo.svg";

		link.href = objectUrl;
		link.download = filename;
		document.body.appendChild(link);
		link.click();
		link.remove();
		URL.revokeObjectURL(objectUrl);
	};

	const downloadFromUrl = async (url) => {
		if (!url) {
			return;
		}

		const response = await fetch(url, { mode: "cors" });
		if (!response.ok) {
			throw new Error(`Failed to download ${url}`);
		}

		const blob = await response.blob();
		triggerBlobDownload(url, blob);
	};

	const downloadLogo = async (card) => {
		const url = card.getAttribute("href");
		const fallbackUrl = card.getAttribute("data-brand-logo-fallback");

		try {
			await downloadFromUrl(url);
		} catch (error) {
			if (fallbackUrl && fallbackUrl !== url) {
				await downloadFromUrl(fallbackUrl);
				return;
			}

			throw error;
		}
	};

	document.addEventListener("DOMContentLoaded", () => {
		const cards = document.querySelectorAll("[data-brand-logo-download='true']");
		if (!cards.length) {
			return;
		}

		cards.forEach((card) => {
			card.addEventListener("click", async (event) => {
				if (
					event.defaultPrevented ||
					event.button !== 0 ||
					event.metaKey ||
					event.ctrlKey ||
					event.shiftKey ||
					event.altKey
				) {
					return;
				}

				event.preventDefault();

				try {
					await downloadLogo(card);
				} catch (error) {
					window.location.href = card.href;
				}
			});
		});
	});
})();
