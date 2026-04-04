function assetDetailCopyToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text);
    }

    return new Promise(function (resolve, reject) {
        var textarea = document.createElement("textarea");
        textarea.value = text;
        textarea.setAttribute("readonly", "");
        textarea.style.position = "fixed";
        textarea.style.top = "-1000px";
        textarea.style.left = "-1000px";
        document.body.appendChild(textarea);
        textarea.select();

        var copied = false;
        try {
            copied = document.execCommand("copy");
        } catch (error) {
            copied = false;
        }

        document.body.removeChild(textarea);

        if (copied) {
            resolve();
        } else {
            reject(new Error("Unable to copy text"));
        }
    });
}

function assetDetailGetCopyLabelNode(button) {
    return button.querySelector("[data-copy-label]");
}

function assetDetailSetCopyButtonLabel(button, label) {
    var labelNode = assetDetailGetCopyLabelNode(button);

    if (labelNode) {
        labelNode.textContent = label;
        return;
    }

    button.textContent = label;
}

function assetDetailBindCopyButtons() {
    var buttons = document.querySelectorAll(".asset-copy-button[data-copy-text]");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            var textToCopy = button.dataset.copyText || "";
            var labelNode = assetDetailGetCopyLabelNode(button);

            if (!textToCopy) {
                return;
            }

            assetDetailCopyToClipboard(textToCopy).then(function () {
                var copiedLabel = button.dataset.copiedLabel || "Copied!";
                var defaultLabel = button.dataset.defaultLabel || (labelNode ? labelNode.textContent.trim() : button.textContent.trim());

                assetDetailSetCopyButtonLabel(button, copiedLabel);
                button.disabled = true;

                window.setTimeout(function () {
                    assetDetailSetCopyButtonLabel(button, defaultLabel);
                    button.disabled = false;
                }, 1800);
            }).catch(function () {
                console.error("Failed to copy asset release URL");
            });
        });
    });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", assetDetailBindCopyButtons);
} else {
    assetDetailBindCopyButtons();
}
