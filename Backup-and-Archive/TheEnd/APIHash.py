from flask import *
import sys
import hashlib

app = Flask(__name__)
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
@app.route("/TestHash/",methods=['GET'])
def query_records():
    PathFile=str(request.args.get('path'))
    NameFile=str(request.args.get('name'))
    md5 = hashlib.md5()
    sFile=PathFile + NameFile
    if sFile is None:
        end='wqeqweqwe'
    else:
        with open(sFile, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                end =md5.hexdigest()
    s={"name": NameFile,
                        "HashCode": end}
    return jsonify(s)

# def Handle_Hash():
#     PathFile=str(request.args.get('path'))
#     NameFile=str(request.args.get('name'))
    # md5 = hashlib.md5()
    # sFile=PathFile + NameFile
    # if sFile is None:
    #     end='wqeqweqwe'
    # else:
    #     with open(sFile, 'rb') as f:
    #         while True:
    #             data = f.read(BUF_SIZE)
    #             if not data:
    #                 break
    #             md5.update(data)
    #             end =md5.hexdigest()
#             sos=str(end)
#     return json.dumps({'name': NameFile,
#                        'email': PathFile})
app.run(host='192.0.2.1',port='2308')
