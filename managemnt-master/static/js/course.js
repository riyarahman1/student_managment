$(document).ready(function () {


    $('#create').on('click', function () {
        var coursename = $('#coursename').val();
        var code = $('#code').val();
        var description = $('#description').val();

        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        if (coursename.trim() == "" || code.trim() == "") {
            alert("Please complete the required field");
        } else if (!nameRegex.test(coursename)) {
            alert("Name can only contain letters and spaces");
        } else {
            $.ajax({
                url: 'course/create/',
                type: 'POST',
                data: {
                    coursename: coursename,
                    code: code,
                    description: description,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#coursename').val('');
                    $('#code').val('');
                    $('#description').val('');
                    alert("New Course Successfully Added");
                }
            });
        }
    });

    $(document).on('click', '.edit', function () {
        var id = $(this).attr('name');
        window.location = "edit/" + id;
    });

    $(document).on('click', '.user-edit', function (event) {
        console.log("updateddddddd");
        event.preventDefault();
        var coursename = $('input[name="coursename"]').val();
        var id = $('#editId').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        if (coursename.trim() == "" || code.trim() == "") {
            alert("Please complete the required field");
        } else if (!nameRegex.test(coursename)) {
            alert("Name can only contain letters and spaces");
        } else {
            $.ajax({
                url: 'course/' + id + '/update/',
                type: 'POST',
                data: {
                    coursename: coursename,
                    code: code,
                    description: description,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    alert('Updated!');
                    window.location = '';
                }
            });
        }
    });


});
// function Read() {
//     $.ajax({
//         async: true,
//         url: '/course',
//         type: 'GET',

//         data: {
//             res: 1,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function (response) {
//             $('#listcourse').html(response);
//         }
//     });
// }