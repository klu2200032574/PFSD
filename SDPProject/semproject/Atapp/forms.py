from django import forms
from .models import Book, Contact

class DateInput(forms.DateInput):
    input_type = "date"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}    # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {"dept_id":"Enter ID","dept_name":"Enter Name","dept_location":"Select Location","dept_hod":"Provide HOD"}


