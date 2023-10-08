function createCopyToClipboardButtonFor(codeElement) {
    var container = document.createElement('div');
    container.classList.add('clipboard-container');
    var button = document.createElement('div');
    container.appendChild(button);
    button.classList.add('clipboard-button');
    button.onclick = copyToClipboardAndAnnounce(codeElement);
    button.innerHTML =
        // MIT license of the icons: https://github.com/primer/octicons/blob/main/LICENSE
        '<svg class="clipboard-copy-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>' +
        '<svg class="clipboard-check-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>';
    return container;

    ////////////////////////////////

    function copyToClipboardAndAnnounce(codeElement) {
        var timeout;
        return function () {
            var button = this;
            if (timeout) return; // ignore multiple clicks
            
            copyNode(codeElement, {
                success: showCheckIconAndThenReset(button),
                error: logError(),
            });
        }
    
        function showCheckIconAndThenReset(button) {
            return () => {
                button.classList.add('clipboard-copy-success');
                timeout = setTimeout(() => {
                    button.classList.remove('clipboard-copy-success');
                    timeout = null;
                }, 2000);
            };
        }
    }
    
    function copyNode(node, callbacks) {
        var resolve = callbacks.success;
        var reject = callbacks.error
    
        // copy in modern browsers
        if ('clipboard' in navigator) {
            var textToCopy = node.textContent && node.textContent.trim() || '';
            return navigator.clipboard.writeText(textToCopy).then(resolve).catch(reject);
        }
    
        // copy in older browsers
        var selection = getSelection();
        if (selection == null)
            return reject();
        selection.removeAllRanges();
        var range = document.createRange();
        range.selectNodeContents(node);
        selection.addRange(range);
        document.execCommand('copy');
        selection.removeAllRanges();
        return resolve();
    }
    
    function logError() {
        return () => {
            console.error('Failed to copy code to clipboard');
        };
    }
}