$(#contact-form).submit(function(e) {
    var fname = $('first_name')
    var lname = $('last_name')
    var phone = $('phone_number')
    var email = $('email_address')
    var reason = $('reason')
    var other_reason = $('other_reason')
    var message = $('contact_message')

if (!fname.value || !lname.value || !phone.value || !email.value || !reason.value || !message.value) {
    alertify.error('Please check your inputs')
} else {
    e.preventDefault()
    $(this).get(0).reset()
    alertify.success('Message Sent')
}
});