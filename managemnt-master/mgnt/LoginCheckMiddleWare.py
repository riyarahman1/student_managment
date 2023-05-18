class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        # Check whether the user is logged in or not
        if user.is_authenticated:
            # Check user type and redirect accordingly
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif (
                    modulename == "student_management_app.views"
                    or modulename == "django.views.static"
                ):
                    pass
                else:
                    return redirect("admin_home")

            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif (
                    modulename == "student_management_app.views"
                    or modulename == "django.views.static"
                ):
                    pass
                else:
                    return redirect("staff_home")

            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews":
                    pass
                elif (
                    modulename == "student_management_app.views"
                    or modulename == "django.views.static"
                ):
                    pass
                else:
                    return redirect("student_home")

        # Redirect to login page if the user is not authenticated
        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            else:
                return redirect("login")
