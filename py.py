from flask import Flask, request
app = Flask(__name__)

value = 1  # القيمة الافتراضية تكون صفر

@app.route('/', methods=['GET', 'POST'])
def handle_value():
    global value
    if request.method == 'GET':
        return str(value)
    elif request.method == 'POST':
        new_value = request.form.get('new_value')
        if new_value is not None:
            try:
                value = int(new_value)  # تحديث القيمة بالقيمة التي أدخلها المستخدم
                return 'تم تحديث القيمة بنجاح إلى: {}'.format(value)
            except ValueError:
                return 'خطأ: يجب إدخال قيمة صحيحة.'
        else:
            return 'خطأ: يرجى إرسال قيمة جديدة.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
