#!/usr/bin/node
$('DIV#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
});
