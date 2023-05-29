from django import forms


class FeedbackForm(forms.Form):
    user_email = forms.EmailField(label="Ваш email", widget=forms.EmailInput(attrs={"placeholder": "name@example.com"}))
    feedback = forms.CharField(label="Ваш відгук", widget=forms.Textarea(attrs={"placeholder": "Напишіть свій відгук тут..."}))

    def clean_user_email(self):
        cf = self.cleaned_data['user_email']
        return cf

    def clean_feedback(self):
        cf = self.cleaned_data['feedback']
        return cf
