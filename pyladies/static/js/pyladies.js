var PyLadies = $(function () {
    'use strict';

    var user = "pyladies";
    var url = "http://twitter.com/statuses/user_timeline.json?screen_name=" + user + "&count=1&callback=?";

    $.getJSON(url, function(data) {

        var tweet = data[0].text;

        // regex for url and twitter handle links
        tweet = tweet.replace(/(\b(https?|ftp|file):\/\/[\-A\-Z0\-9+&@#\/%?=~_|!:,.;]*[\-A-Z0-9+&@#\/%=~_|])/ig, '<a href="$1">$1</a>');
        tweet = tweet.replace(/(^|\s)@(\w+)/g, '$1<a href="http://www.twitter.com/$2">@$2</a>');
      
        $(".feed").html(tweet);
    });

}());