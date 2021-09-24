from flask import Flask, render_template, redirect, url_for, request, jsonify, Blueprint
import hashlib
import os
from werkzeug.utils import secure_filename
from flask import current_app as app
from flask import Flask, Response, request, render_template, redirect, url_for, Blueprint, jsonify
from flaskr.config import *
import traceback
print("nft_address: ", nft_address)

bp = Blueprint('app', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#@bp.route('/mint', methods=['GET', 'POST'])
#def minting():
#    return render_template('minting.html')

@bp.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

@bp.route('/metadata', methods=['GET', 'POST'])
def metadata():

    if request.method == "POST":

        form = request.form


        abi_json = json.dumps(nft_abi)

        nft_contract = w3.eth.contract(
            abi=abi_json,
            address=nft_address
            )

        tokenIds = nft_contract.functions.totalSupply().call()

        form_json = json.dumps(form)
        count = json.loads(form_json)['count']

        for i in range(tokenIds, tokenIds+(int)(count)):

            print("i :", i)
            with open(app.root_path+'/static/uploads/metadata/'+(str)(i)+'.json', 'w') as f:
                json.dump({
                    'name': " #"+ (str)(i),
                    'description': ".",
                    'image': request.url_root+'static/uploads/nft/0.png'
                }, f)

        print("success ")
        status = "success"
    else:
        print("failed")
        status = "uploaded error"
    return json.dumps({'status':status});


@bp.route('/metadata/<tokenId>', methods=['GET', 'POST'])
def nft_metadata(tokenId):
    try:
        print("tokenId: ", tokenId)
        abi_json = json.dumps(nft_abi)
        # print("abi_json: ", abi_json)
        nft_contract = w3.eth.contract(
                abi=abi_json,
                address=nft_address
                )
        # print("nft_contract: ", nft_contract)
        tokenIds = nft_contract.functions.totalSupply().call()
        print("tokenIds: ", tokenIds)
        if (int)(tokenId) <= (int)(tokenIds):
            print("token exist: ", './uploads/metadata/'+(str)(tokenId)+'.json')
            print("token exist: ",(str)(tokenId))
            # with open(current_app.root_path+'/static/uploads/metadata/'+(str)(tokenId)+'.json') as f:
            with open('/opt/monkeys_app/flaskr/static/uploads/metadata/'+(str)(tokenId)+'.json') as f:
                metadata = json.load(f)
                print("metadata: ", metadata)
            return jsonify(metadata)
        else:
            return redirect(url_for('app.index'))
    except:
        tb = traceback.format_exc()
        print("tb: ", tb)
        return redirect(url_for('app.index'))
    return redirect(url_for('app.index'))
