$(function () {
  $('div#add_item').bind('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});

$(function () {
  $('div#remove_item').bind('click', function () {
    $('ul.my_list li:last').remove();
  });
});

$(function () {
  $('div#clear_list').bind('click', function () {
    $('ul.my_list').remove();
  });
});
