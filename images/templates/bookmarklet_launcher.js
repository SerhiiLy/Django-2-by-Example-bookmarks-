(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild
        (document.createElement('script')
        ).src = 'https://a79d03b5c642.ngrok.io/static/js/bookmarklet.js?r='
            + Math.floor(Math.random() * 99999999999999999999);
    }
})();


