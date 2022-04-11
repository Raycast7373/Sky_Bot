from flask import Flask

import os
BadID = 'NONE'
ClusterID = os.getenv('Cluster_ID')
DiscordToken = os.getenv('Discord_Token')
RevoltToken = os.getenv('Revolt_Token')

print("ClusterID: ",ClusterID)
print("DiscordToken: ",DiscordToken)
print("RevoltToken: ",RevoltToken)

try:
    int(ClusterID)
    print("ID is a number!")
    IsClusterIDNum = True
    if 0 <= number <= 16:
        print("Number is Valid!")
        IDVALID = 'TRUE'
    else:
        print("Number isn't Valid!!! ERROR")
        IDVALID = 'FALSE'
except ValueError:
    print("Error! Invalid ID detected,ID is not a number! terminating...")
    IsClusterIDNum = False

#if ClusterID == BadID:
#    print("Error! Invalid ID detected, terminating...")
#    ERROR = 'TRUE'
#else:
#    print("No ClusterID error found! Starting...")
#    ERROR = 'FALSE'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ClusterID:'
    return ClusterID
    return 'DiscordToken:'
    return DiscordToken
    return 'RevoltToken:'
    return RevoltToken
    return 'IsClusterIDNum:'
    return IsClusterIDNum
    return 'IDVALID:'
    return IDVALID

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
