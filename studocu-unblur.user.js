// ==UserScript==
// @name         StuDocu Unblur by Kousei
// @match        *://*.studocu.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    setInterval(() => {
        document.querySelectorAll('[data-test-selector="document-viewer-paywall"], .modal-overlay, .paywall').forEach(e => e.remove());
        document.querySelectorAll('[style*="filter: blur"], .blurred-container').forEach(e => {
            e.style.filter = 'none';
            e.style.userSelect = 'auto';
        });
        document.body.style.overflow = 'auto';
    }, 1500);
})();