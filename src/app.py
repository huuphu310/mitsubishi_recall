from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/checkVin')
def checkVin():
    return render_template('check.html')


@app.route('/check',methods=['POST','GET'])
def check():
    try:
        _vinNumber = request.form['vinNumber']
        mess_true = 'Số vin ' + _vinNumber + ' nằm trong diện triệu hồi, hãy liên hệ với đại lý để được kiểm tra và thay thế.'
        if len(_vinNumber) == 17 and _vinNumber[:3] == 'RLA':
            vin_left = _vinNumber[:10]
            vin_right = int(_vinNumber[-7:])
            if vin_left == 'RLA0TGF2MH' and 1000003 <= vin_right <= 1000032:
                return mess_true
            if vin_left == 'RLA0TGF2MJ' and 1000001 <= vin_right <= 1001259:
                return mess_true
            if vin_left == 'RLA0TGF2XH' and 1000005 <= vin_right <= 1000034:
                return mess_true
            if vin_left == 'RLA0TGF2XJ' and 1000001 <= vin_right <= 1000839:
                return mess_true
            if vin_left == 'RLA0TGF3MH' and 1000006 <= vin_right <= 1000035:
                return mess_true
            if vin_left == 'RLA0TGF3MJ' and 1000001 <= vin_right <= 1000479:
                return mess_true
            if vin_left == 'RLA1TGF2MJ' and 1000001 <= vin_right <= 1000301:
                return mess_true
            if vin_left == 'RLA1TGF2MK' and 1000001 <= vin_right <= 1000930:
                return mess_true
            if vin_left == 'RLA1TGF2XJ' and 1000001 <= vin_right <= 1000391:
                return mess_true
            if vin_left == 'RLA1TGF2XK' and 1000001 <= vin_right <= 1000540:
                return mess_true
            if vin_left == 'RLA1TGF3MJ' and 1000001 <= vin_right <= 1000271:
                return mess_true
            if vin_left == 'RLA1TGF3MK' and 1000001 <= vin_right <= 1000270:
                return mess_true
            else:
                return 'Số vin ' + _vinNumber + ' KHÔNG nằm trong diện triệu hồi'
        if len(_vinNumber) == 17 and _vinNumber[:3] == 'MK2':
            vin_left = _vinNumber[:11]
            vin_right = int(_vinNumber[-6:])
            if vin_left == 'MK2XRNC1WKN' and 9406 <= vin_right <= 11202:
                return mess_true
            if vin_left == 'MK2XNNC1WKN' and 55045 <= vin_right <= 60293:
                return mess_true
        else:
            return 'Số vin không hợp lệ'
    except Exception as e:
        return 'Số vin không hợp lệ'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
