import json
import boto3
import os

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


table_name='my_table_name'
file_name=table_name+'.txt'
s3 = boto3.resource('s3',aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY) #replace access keys here
s3client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
Bucket='my_bucket'
Key='txt file path on s3 with file name'

json_file='json_file_path_on_aws'
temp_json_file='/tmp/'+json_file.split('/')[-1]

s3.Bucket(Bucket).download_file(Key,'/tmp/'+file_name)
s3.Bucket(Bucket).download_file(json_file,temp_json_file)


f=open("/tmp/"+file_name,"a+")
col=[]
for line in f:
    if len(line.strip()) > 0:
        col.append(line.strip().replace("\n",""))

json_file=open(temp_json_file,'r+')
for row in json_file:
    for key, value in json.loads(row).iteritems():
        if key not in col:
            col.append(key)
            f.write(key+"\n")
f.close()
json_file.close()

s3client.put_object(Bucket=Bucket,Body=open("/tmp/"+file_name,'r+'),Key=Key)
os.remove("/tmp/"+file_name)
os.remove(temp_json_file)
