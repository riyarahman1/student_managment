$(document).ready(function () {

    $('#create').on('click', function () {
        var Studentname = $('#Studentname').val();
        var studentemail = $('#studentemail').val();
        var phone = $('#phone').val();
        var address = $('#address').val();
        var created_at = $('#created_at').val();

        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        if (Studentname.length == 0 || studentemail.length == 0) {
            alert("Please complete the required field");
        } else if (!nameRegex.test(Studentname)) {
            alert("Name can only contain letters and spaces");
        } else {
            $.ajax({
                url: 'students/create/',
                type: 'POST',
                data: {
                    Studentname: Studentname,
                    studentemail: studentemail,
                    phone: phone,
                    address: address,
                    created_at: created_at,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#Studentname').val('');
                    $('#studentemail').val('');
                    $('#phone').val('');
                    $('#address').val('');
                    $('#created_at').val('');
                    alert("New Student Successfully Added");
                }
            });
        }
    });




    //////////////////////////////////////////////////////////////////////////////
    // Create Django Ajax Call
    $("form#updateUser").submit(function () {
        var Studentname = $('input[name="formStudentname"]').val().trim();
        var studentemail = $('input[name="formName"]').val().trim();
        var phone = $('input[name="formPhone"]').val().trim();
        var address = $('input[name="formAddress"]').val().trim();
        var created_at = $('input[name="formcreated_at"]').val().trim();
        if (Studentname && address) {
            // Create Ajax Call
            $.ajax({
                url: '{% url "student_update" %}',
                data: {
                    'Studentname': Studentname,
                    'studentemail': studentemail,
                    'phone': phone,
                    'address': addressaddress,
                    'created_at': created_at,
                },
                dataType: 'json',
                success: function (data) {
                    if (data.user) {
                        updateToUserTabel(data.user);
                    }
                }
            });
        } else {
            alert("All fields must have a valid value.");
        }
        $('form#updateUser').trigger("reset");
        $('#myModal').modal('hide');
        return false;
    });

    // Update Django Ajax Call
    function editUser(id) {
        if (id) {
            tr_id = "#user-" + id;
            Studentname = $(tr_id).find(".userName").text();
            address = $(tr_id).find(".userAddress").text();
            studentemail = $(tr_id).find(".userAge").text();
            phone = $(tr_id).find(".userphone").text();
            $('#form-Studentname').val(Studentname);
            $('#form-studentemail').val(studentemail);
            $('#form-address').val(address);
            $('#form-phone').val(phone);
        }
    }
    function updateToUserTabel(user) {
        $("#userTable #user-" + user.id).children(".userData").each(function () {
            var attr = $(this).attr("name");
            if (attr == "Studentname") {
                $(this).text(user.Studentname);
            } else if (attr == "address") {
                $(this).text(user.address);
            }
        });
    }

    //////////////////////////////////////////////////////////////////////////////////////////////////////        

    // corrected delete
    // $(document).on('click', '.delete', function () {
    //     var id = $(this).data('id');
    //     var row = $(this).closest('tr');
    //     var csrf_token = $(this).data('csrf-token');
    //     $.ajax({
    //         url: '/studentmgnt/students/' + id + '/delete/',
    //         type: 'DELETE',
    //         beforeSend: function (xhr) {
    //             xhr.setRequestHeader('X-CSRFToken', csrf_token);
    //         },
    //         success: function () {
    //             row.remove();
    //         },
    //         error: function (xhr, status, error) {
    //             console.log('Error:', error);
    //         }
    //     });
    // });

})