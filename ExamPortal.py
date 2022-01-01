from flask import Flask, render_template, request
from DBConnection import Db

app = Flask(__name__)


# @app.route('/')  
# def default():
#     return 'Welcome to the Examination Portal'

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/login_post', methods=['post'])
def login_post():
    user_name = request.form['textfield']
    pass_word = request.form['textfield2']
    return '''<script>alert('Login Successfully');window.location='/home'</script>'''

#-----------------ADMIN---------------------------------------------------------------

@app.route('/')
def home():
    return render_template('admin/home.html')


@app.route('/incoming_requests')
def incoming_requests():
    return render_template('admin/incoming_requests.html')
@app.route('/incoming_req_post',methods=['post'])
def incoming_req_post():
    query = request.form['textfield']
    return '''<script>window.location='/incoming_requests'</script>'''

@app.route('/view_accepted')
def view_accepted():
    return render_template('admin/view_accepted.html')

@app.route('/view_rejected')
def view_rejected():
    return render_template('admin/view_rejected.html')

@app.route('/view_review')
def view_review():
    return render_template('admin/view_review.html')



#-------------------INSTITUTION-----------------------------------------------------------
@app.route('/course_management')
def course_management():
    return render_template('institution/course_management.html')
@app.route('/course_mang_post', methods=['post'])
def course_mang_post():
    course_name = request.form['Submit']
    return '''<script>alert('Course added successfully'); window.location='/course_management'</script> '''


@app.route('/department_management')
def department_management():
    return render_template('institution/department_management.html')
@app.route('/dept_mang_post', methods=['post'])
def dept_mang_post():
    dept_name = request.form['Submit']
    return '''<script>alert('Department added successfully'); window.location='/department_management'</script> '''


@app.route('/hod_management')
def hod_management():
    return render_template('institution/hod_management.html')
@app.route('/hod_mang_post', methods=['post'])
def hod_mang_post():
    hod_name = request.form['Assign']
    return '''<script>alert('HOD assigned successfully'); window.location='/hod_management'</script> '''

@app.route('/manager_management')
def manager_management():
    return render_template('institution/manager_management.html')
@app.route('/mangr_mang_post', methods=['post'])
def mangr_mang_post():
    mangr_name = request.form['Submit']
    return '''<script>alert('Added Manager successfully'); window.location='/manager_management'</script> '''


@app.route('/registration')
def registration():
    return render_template('institution/registration.html')
@app.route('/registration_post', methods=['post'])
def registration_post():
    registration = request.form['Submit']
    return '''<script>alert('Registration success'); window.location='/registration'</script> '''

@app.route('/send_reply')
def send_reply():
    return render_template('institution/send_reply.html')
@app.route('/send_reply_post', methods=['post'])
def send_reply_post():
    institute_reply = request.form['Submit']
    return '''<script>window.location='/send_reply'</script> '''


@app.route('/staff_management')
def staff_management():
    return render_template('institution/staff_management.html')
@app.route('/staff_mang_post', methods=['post'])
def staff_mang_post():
    staff_name = request.form['Submit']
    return '''<script>alert('Staff Added Successfully'); window.location='/staff_management'</script> '''


@app.route('/subject_management')
def subject_management():
    return render_template('institution/subject_management.html')
@app.route('/subj_mang_post', methods=['post'])
def subj_mang_post():
    sub_name = request.form['Submit']
    return '''<script>alert('Subject Added Successfully'); window.location='/subject_management'</script> '''


@app.route('/upload_notification')
def upload_notification():
    return render_template('institution/upload_notification.html')

@app.route('/view_complaint')
def view_complaint():
    return render_template('institution/view_complaint.html')
@app.route('/view_profile')
def view_profile():
    return render_template('institution/view_profile.html')

#-------------------------MANAGER--------------------------------------------------------------------
@app.route('/manager_view_profile')
def manager_view_profile():
    return render_template('manager/manager_view_profile.html')

@app.route('/manager_notification')
def manager_notification():
    return render_template('manager/notification.html')

@app.route('/register_student')
def register_student():
    return render_template('manager/register_student.html')

@app.route('/manager_review')
def manager_review():
    return render_template('manager/review.html')

@app.route('/view_hod_department')
def view_hod_department():
    return render_template('manager/view_hod_department.html')

@app.route('/view_staff_management')
def view_staff_management():
    return render_template('manager/view_staff_management.html')



#--------------------------HOD------------------------------------------------------------------------
@app.route('/complaint')
def complaint():
    return render_template('hod/complaint.html')
@app.route('/complaint_post',methods=['post'])
def complaint_post():
    hod_complaint = request.form['Send']
    return '''<script>alert('Complaint successfully sent to Institution');window.location='/complaint'</script>'''


@app.route('/mail_to_parent')
def mail_to_parent():
    return render_template('hod/mail_to_parent.html')

@app.route('/send_notification')
def send_notification():
    return render_template('hod/send_notification.html')
@app.route('/send_notif_post', methods=['post'])
def send_notif_post():
    hod_send_notif = request.form['Send']
    return '''<script>alert('Notification sent successfully');window.location='/send_notification'</script>'''

@app.route('/subject_allocation')
def subject_allocation():
    return render_template('hod/subject_allocation.html')
@app.route('/sub_alloc_post', methods=['post'])
def sub_alloc_post():
    sub_alloc = request.form['Assign']
    return '''<script>window.location='/subject_allocation'</script>'''

@app.route('/view_exam')
def view_exam():
    return render_template('hod/view_exam.html')

@app.route('/hod_view_profile')
def hod_view_profile():
    return render_template('hod/view_profile.html')

@app.route('/hod_view_reply')
def hod_view_reply():
    return render_template('hod/view_reply.html')

@app.route('/view_result')
def view_result():
    return render_template('hod/view_result.html')

@app.route('/view_staff')
def view_staff():
    return render_template('hod/view_staff.html')

@app.route('/view_subject_allocation')
def view_subject_allocation():
    return render_template('hod/view_subject_allocation.html')


#-----------------------TEACHER----------------------------------------------------------------
@app.route('/exam_notification')
def exam_notification():
    return render_template('teacher/exam_notification.html')

@app.route('/send_complaint')
def send_complaint():
    return render_template('teacher/send_complaint.html')

@app.route('/upload_exam')
def upload_exam():
    return render_template('teacher/upload_exam.html')

@app.route('/upload_viva_result')
def upload_viva_result():
    return render_template('teacher/upload_viva_result.html')

@app.route('/view_allocated_subject')
def view_allocated_subject():
    return render_template('teacher/view_allocated_subject.html')

@app.route('/view_notification')
def view_notification():
    return render_template('teacher/view_notification.html')

@app.route('/teacher_view_profile')
def teacher_view_profile():
    return render_template('teacher/view_profile.html')

@app.route('/teacher_view_reply')
def teacher_view_reply():
    return render_template('teacher/view_reply.html')

@app.route('/view_results')
def view_results():
    return render_template('teacher/view_results.html')

#------------------------------STUDENT-------------------------------------------------------
@app.route('/view_exam_attended')
def view_exam_attended():
    return render_template('student/view_exam_attended.html')

@app.route('/student_view_profile')
def student_view_profile():
    return render_template('student/view_profile.html')

@app.route('/student_view_staff')
def student_view_staff():
    return render_template('student/view_staff.html')

@app.route('/student_view_subject')
def student_view_subject():
    return render_template('student/view_subject.html')






if __name__ == '__main__':
    app.run(debug=True)
