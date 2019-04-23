from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User

class RegisterForm(Form):
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少要两个字符，最多10个字符')])
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮件格式不规范')])
    password = PasswordField(validators=[DataRequired(), Length(6, 32, message='密码不可以为空')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('数据库已经注册了该电子邮件')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该用户名已经被注册了')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮件格式不规范')])
    password = PasswordField(validators=[DataRequired(), Length(6, 32, message='密码不可以为空')])

