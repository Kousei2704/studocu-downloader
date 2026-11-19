// ==UserScript==
// @name         StuDocu Unblur by Kousei
// @namespace    https://github.com/Kousei2704/studocu-downloader
// @version      1.1
// @description  Gỡ làm mờ và tắt popup trên StuDocu (.com & .vn)
// @match        *://*.studocu.com/*
// @match        *://*.studocu.vn/*
// @grant        GM_addStyle
// ==/UserScript==

(function() {
    'use strict';

    // Ép CSS gỡ blur trên toàn bộ trang
    const css = `
        * {
            filter: none !important;
            -webkit-filter: none !important;
            user-select: text !important;
        }
        [data-test-selector="document-viewer-paywall"],
        .modal-overlay,
        .paywall,
        ._95f5f1767857,
        #document-wrapper > div:has([data-test-selector="paywall"]) {
            display: none !important;
        }
        body {
            overflow: auto !important;
        }
    `;

    const style = document.createElement('style');
    style.innerHTML = css;
    document.head.appendChild(style);

    // Quét xóa các popup chặn màn hình sinh ra động
    setInterval(() => {
        document.querySelectorAll('[data-test-selector="document-viewer-paywall"], .modal-overlay, .paywall').forEach(el => el.remove());
        document.body.style.overflow = 'auto';
    }, 1000);
})();