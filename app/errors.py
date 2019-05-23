from flask import render_template, request, jsonify
from app import app


@app.errorhandler(403)
def forbidden(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '无访问权限', 'code': '403', 'data': ''})
    return render_template('error/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '请求的资源不存在', 'code': '404', 'data': ''})
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '服务器内部错误', 'code': '500', 'data': ''})
    return render_template('error/500.html'), 500


@app.errorhandler(405)
def request_args_error(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '请求的参数缺失或异常', 'code': '405', 'data': ''})
    return render_template('error/414.html'), 405


@app.errorhandler(406)
def request_not_find(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '请求的内容为空', 'code': '406', 'data': ''})
    return render_template('error/406.html'), 406


@app.errorhandler(407)
def request_not_find(e):
    if request.url.find('api') != -1:
        return jsonify({'error': '请求的内容有冲突', 'code': '407', 'data': ''})
    return render_template('error/407.html'), 407
