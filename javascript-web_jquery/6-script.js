#!/usr/bin/node
//We are creating a JavaScript script to change the text of the header> element to New Header!!!
$('div#update_header').click(() => {
    $('header').text('New Header!!!');
});
