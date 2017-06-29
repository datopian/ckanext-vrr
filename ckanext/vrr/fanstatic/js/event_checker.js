(function () {
    'use strict';
  

    $(document).ready(function () {

        $('#terms-of-use').on('click', function (e){
            if (e.target.checked) {
                document.getElementById('create-account-btn').disabled = false;
            } else {
                document.getElementById('create-account-btn').disabled = true;
            }
        });
    });
})($);